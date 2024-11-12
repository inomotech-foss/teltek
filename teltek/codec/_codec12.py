import dataclasses
import enum
from typing import Self

from teltek.codec._error import CodecException
from teltek.codec._frame import CodecId, MessageFrame


class Codec12Type(enum.IntEnum):
    REQUEST = 0x05
    RESPONSE = 0x06


@dataclasses.dataclass(kw_only=True, frozen=True)
class Codec12:
    type: Codec12Type
    content: str

    def encode(self) -> bytes:
        count = b"\x01"  # quantity is always 1 apparently
        type = self.type.to_bytes(1, byteorder="big")
        content = self.content.encode("utf-8")
        content_len = len(content).to_bytes(4, byteorder="big")
        return count + type + content_len + content + count

    @classmethod
    def decode(cls, body: bytes) -> Self:
        # (2 * 1b for count) + (1b for type) + (4b for length)
        if len(body) < 7:
            raise CodecException("not enough bytes for codec12 data")
        count = body[0]
        count2 = body[-1]
        if count != count2:
            raise CodecException(
                f"first quantity {count} does not match last quantity {count2}"
            )

        type = Codec12Type(body[1])
        content_len = int.from_bytes(body[2:6], byteorder="big")
        content = body[6 : 6 + content_len].decode("utf-8")
        return cls(type=type, content=content)

    def to_frame(self) -> MessageFrame:
        return MessageFrame.build(CodecId.CODEC_12, self.encode())

    @classmethod
    def from_frame(cls, frame: MessageFrame) -> Self:
        if frame.codec_id != CodecId.CODEC_12:
            raise CodecException(f"expected codec12 but got {frame.codec_id}")
        return cls.decode(frame.data)
