from teltek.codec import (
    Codec8e,
    CodecId,
    MessageFrame,
    Codec8eAvlData,
    Codec8eGpsElement,
    Codec8eIoElement,
)
import base64


def test_decode_real():
    raw = base64.b64decode(
        "AAAAAAAAALOOBAAAAZU9bVvgAASXaI4cMBpEAekBNRIAAAHBAAEAAAAAAAEBwQAycEAAAAAAAAABlT1tV/gABJdojhwwGkQB6QE1EgAAAcEAAQAAAAAAAQHBADJwPwAAAAAAAAGVPW1UEAAEl2iOHDAaRAHpATUSAAABwQABAAAAAAABAcEAMnA9AAAAAAAAAZU9bUxAAASXaI4cMBpEAekBNRIAAAHBAAEAAAAAAAEBwQAycDwAAAAABAAAwR8="
    )
    expected = Codec8e(
        avl_data=[
            Codec8eAvlData(
                timestamp=1740492332000,
                priority=0,
                gps=Codec8eGpsElement(
                    longitude=77031566,
                    latitude=472914500,
                    altitude=489,
                    angle=309,
                    satellites=18,
                    speed=0,
                ),
                io=Codec8eIoElement(
                    event_io_id=449, n1={}, n2={}, n4={449: 3305536}, n8={}, nx={}
                ),
            ),
            Codec8eAvlData(
                timestamp=1740492331000,
                priority=0,
                gps=Codec8eGpsElement(
                    longitude=77031566,
                    latitude=472914500,
                    altitude=489,
                    angle=309,
                    satellites=18,
                    speed=0,
                ),
                io=Codec8eIoElement(
                    event_io_id=449, n1={}, n2={}, n4={449: 3305535}, n8={}, nx={}
                ),
            ),
            Codec8eAvlData(
                timestamp=1740492330000,
                priority=0,
                gps=Codec8eGpsElement(
                    longitude=77031566,
                    latitude=472914500,
                    altitude=489,
                    angle=309,
                    satellites=18,
                    speed=0,
                ),
                io=Codec8eIoElement(
                    event_io_id=449, n1={}, n2={}, n4={449: 3305533}, n8={}, nx={}
                ),
            ),
            Codec8eAvlData(
                timestamp=1740492328000,
                priority=0,
                gps=Codec8eGpsElement(
                    longitude=77031566,
                    latitude=472914500,
                    altitude=489,
                    angle=309,
                    satellites=18,
                    speed=0,
                ),
                io=Codec8eIoElement(
                    event_io_id=449, n1={}, n2={}, n4={449: 3305532}, n8={}, nx={}
                ),
            ),
        ]
    )
    assert _decode_frame(raw) == expected


def test_decode():
    raw = bytes.fromhex(
        "000000000000004A8E010000016B412CEE000100000000000000000000000000000000010005000100010100010011001D00010010015E2C880002000B000000003544C87A000E000000001DD7E06A00000100002994"
    )
    expected = Codec8e(
        avl_data=[
            Codec8eAvlData(
                timestamp=1560166592000,
                priority=1,
                gps=Codec8eGpsElement(
                    longitude=0,
                    latitude=0,
                    altitude=0,
                    angle=0,
                    satellites=0,
                    speed=0,
                ),
                io=Codec8eIoElement(
                    event_io_id=1,
                    n1={1: 1},
                    n2={17: 0x1D},
                    n4={16: 0x015E2C88},
                    n8={11: 0x3544C87A, 14: 0x1DD7E06A},
                    nx={},
                ),
            )
        ]
    )
    assert _decode_frame(raw) == expected


def _decode_frame(data: bytes) -> Codec8e:
    frame = MessageFrame.decode(data)
    assert frame.codec_id == CodecId.CODEC_8E
    inner = Codec8e.from_frame(frame)
    # ensure roundtrip
    assert inner.encode() == frame.data
    return inner
