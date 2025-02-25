import dataclasses
from typing import Self

from teltek.codec._error import CodecException
from teltek.codec._frame import CodecId, MessageFrame


@dataclasses.dataclass(kw_only=True, frozen=True)
class Codec8e:
    avl_data: "list[Codec8eAvlData]"

    def encode(self) -> bytes:
        records = len(self.avl_data).to_bytes(1, byteorder="big")
        return records + b"".join(avl.encode() for avl in self.avl_data) + records

    @classmethod
    def decode(cls, body: bytes) -> Self:
        # min size according to docs
        if len(body) < 45:
            raise CodecException(
                f"expected at least 45 bytes for codec8e, got {len(body)}"
            )

        records = body[0]
        records2 = body[-1]
        if records != records2:
            raise CodecException(
                f"first quantity {records} does not match last quantity {records2}"
            )

        avl_data: list[Codec8eAvlData] = []
        remaining_body = body[1:-1]
        for _ in range(records):
            (data, consumed) = Codec8eAvlData.decode(remaining_body)
            avl_data.append(data)
            remaining_body = remaining_body[consumed:]

        if remaining_body:
            raise CodecException(
                f"leftover bytes after decoding codec8e: {remaining_body!r}"
            )

        return cls(avl_data=avl_data)

    def to_frame(self) -> MessageFrame:
        return MessageFrame.build(CodecId.CODEC_8E, self.encode())

    @classmethod
    def from_frame(cls, frame: MessageFrame) -> Self:
        if frame.codec_id != CodecId.CODEC_8E:
            raise CodecException(f"expected codec8e but got {frame.codec_id}")
        return cls.decode(frame.data)


@dataclasses.dataclass(kw_only=True, frozen=True)
class Codec8eGpsElement:
    longitude: int
    latitude: int
    altitude: int
    angle: int
    satellites: int
    speed: int

    def encode(self) -> bytes:
        return (
            self.longitude.to_bytes(4, byteorder="big")
            + self.latitude.to_bytes(4, byteorder="big")
            + self.altitude.to_bytes(2, byteorder="big")
            + self.angle.to_bytes(2, byteorder="big")
            + self.satellites.to_bytes(1, byteorder="big")
            + self.speed.to_bytes(2, byteorder="big")
        )

    @classmethod
    def decode(cls, body: bytes) -> Self:
        if len(body) != 15:
            raise CodecException(
                f"expected 15 bytes for gps element but got {len(body)}"
            )
        return cls(
            longitude=int.from_bytes(body[0:4], byteorder="big"),
            latitude=int.from_bytes(body[4:8], byteorder="big"),
            altitude=int.from_bytes(body[8:10], byteorder="big"),
            angle=int.from_bytes(body[10:12], byteorder="big"),
            satellites=int.from_bytes(body[12:13], byteorder="big"),
            speed=int.from_bytes(body[13:15], byteorder="big"),
        )


@dataclasses.dataclass(kw_only=True, frozen=True)
class Codec8eIoElement:
    event_io_id: int
    n1: dict[int, int]
    n2: dict[int, int]
    n4: dict[int, int]
    n8: dict[int, int]
    nx: dict[int, bytes]

    def encode(self) -> bytes:
        total_count = (
            len(self.n1) + len(self.n2) + len(self.n4) + len(self.n8) + len(self.nx)
        )
        return (
            self.event_io_id.to_bytes(2, "big")
            + total_count.to_bytes(2, "big")
            + self._encode_fixed_io(self.n1, 1)
            + self._encode_fixed_io(self.n2, 2)
            + self._encode_fixed_io(self.n4, 4)
            + self._encode_fixed_io(self.n8, 8)
            + self._encode_dynamic_io(self.nx)
        )

    @staticmethod
    def _encode_fixed_io(ios: dict[int, int], n: int) -> bytes:
        count = len(ios).to_bytes(2, "big")
        return count + b"".join(
            id.to_bytes(2, "big") + value.to_bytes(n, "big")
            for id, value in ios.items()
        )

    @staticmethod
    def _encode_dynamic_io(ios: dict[int, bytes]) -> bytes:
        count = len(ios).to_bytes(2, "big")
        return count + b"".join(
            id.to_bytes(2, "big") + len(value).to_bytes(2, "big") + value
            for id, value in ios.items()
        )

    @classmethod
    def decode(cls, body: bytes) -> tuple[Self, int]:
        if len(body) < 4:
            raise CodecException(
                f"expected at least 4 bytes for io element but got {len(body)}"
            )

        event_io_id = int.from_bytes(body[0:2], "big")
        total_count = int.from_bytes(body[2:4], "big")

        offset = 4
        (n1, consumed) = cls._decode_fixed_io(body[offset:], 1)
        offset += consumed
        (n2, consumed) = cls._decode_fixed_io(body[offset:], 2)
        offset += consumed
        (n4, consumed) = cls._decode_fixed_io(body[offset:], 4)
        offset += consumed
        (n8, consumed) = cls._decode_fixed_io(body[offset:], 8)
        offset += consumed

        (nx, consumed) = cls._decode_dynamic_io(body[offset:])
        offset += consumed

        if total_count != len(n1) + len(n2) + len(n4) + len(n8) + len(nx):
            raise CodecException(
                f"total count {total_count} does not match sum of all io counts"
            )

        return cls(event_io_id=event_io_id, n1=n1, n2=n2, n4=n4, n8=n8, nx=nx), offset

    @staticmethod
    def _decode_fixed_io(remaining: bytes, n: int) -> tuple[dict[int, int], int]:
        count = int.from_bytes(remaining[0:2], "big")
        required_len = 2 + count * (2 + n)
        if len(remaining) < required_len:
            raise CodecException(
                f"expected at least {required_len} bytes for fixed io (n={n}) but got {len(remaining)}"
            )

        offset = 2
        ios: dict[int, int] = {}
        for _ in range(count):
            id = int.from_bytes(remaining[offset : offset + 2], "big")
            offset += 2
            value = int.from_bytes(remaining[offset : offset + n], "big")
            offset += n
            ios[id] = value
        return ios, offset

    @staticmethod
    def _decode_dynamic_io(remaining: bytes) -> tuple[dict[int, bytes], int]:
        count = int.from_bytes(remaining[0:2], "big")
        offset = 2
        ios: dict[int, bytes] = {}
        for _ in range(count):
            id = int.from_bytes(remaining[offset : offset + 2], "big")
            offset += 2
            value_len = int.from_bytes(remaining[offset : offset + 2], "big")
            offset += 2
            value = remaining[offset : offset + value_len]
            offset += value_len

            if len(value) != value_len:
                raise CodecException(
                    f"expected {value_len} byte(s) for dynamic io value, got {len(value)}"
                )

            ios[id] = value

        return ios, offset


@dataclasses.dataclass(kw_only=True, frozen=True)
class Codec8eAvlData:
    timestamp: int
    priority: int
    gps: Codec8eGpsElement
    io: Codec8eIoElement

    def encode(self) -> bytes:
        return (
            self.timestamp.to_bytes(8, byteorder="big")
            + self.priority.to_bytes(1, byteorder="big")
            + self.gps.encode()
            + self.io.encode()
        )

    @classmethod
    def decode(cls, body: bytes) -> tuple[Self, int]:
        if len(body) < 24:
            raise CodecException(
                f"expected at least 24 bytes for avl data but got {len(body)}"
            )
        io, consumed = Codec8eIoElement.decode(body[24:])
        return cls(
            timestamp=int.from_bytes(body[0:8], byteorder="big"),
            priority=int.from_bytes(body[8:9], byteorder="big"),
            gps=Codec8eGpsElement.decode(body[9:24]),
            io=io,
        ), consumed + 24
