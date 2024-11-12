import dataclasses
import enum
from typing import Self

from teltek.codec._error import CodecException

_PREAMBLE = 4 * b"\0"


class CodecId(enum.IntEnum):
    CODEC_8 = 0x08
    CODEC_8E = 0x8E
    CODEC_12 = 0x0C


@dataclasses.dataclass(kw_only=True, frozen=True)
class MessageFrame:
    codec_id: CodecId
    data: bytes
    crc16: int

    @classmethod
    def build(cls, codec_id: CodecId, data: bytes) -> Self:
        crc16 = _crc16_ibm(codec_id.to_bytes(1, byteorder="big") + data)
        return cls(
            codec_id=codec_id,
            data=data,
            crc16=crc16,
        )

    def encode(self) -> bytes:
        codec_id = self.codec_id.to_bytes(1, byteorder="big")
        data_size = (len(codec_id) + len(self.data)).to_bytes(4, byteorder="big")
        crc16 = self.crc16.to_bytes(4, byteorder="big")
        return _PREAMBLE + data_size + codec_id + self.data + crc16

    @classmethod
    def decode(cls, payload: bytes) -> Self:
        if payload[:4] != _PREAMBLE:
            raise CodecException(f"expected preamble but got {payload[:4]}")
        data_size = int.from_bytes(payload[4:8], byteorder="big")
        data = payload[8:-4]
        if len(data) != data_size:
            raise CodecException(f"expected {data_size} byte(s) but got {len(data)}")
        crc16 = int.from_bytes(payload[-4:], byteorder="big")
        if _crc16_ibm(data) != crc16:
            raise CodecException(
                f"crc16 expected {crc16} but calculated {_crc16_ibm(data)}"
            )
        codec_id = CodecId(data[0])
        return cls(
            codec_id=codec_id,
            data=data[1:],
            crc16=crc16,
        )


def _crc16_ibm(data: bytes) -> int:
    crc = 0
    for b in data:
        crc = crc ^ b
        for _ in range(8):
            carry = crc & 1
            crc = crc >> 1
            if carry:
                crc = crc ^ 0xA001
    return crc
