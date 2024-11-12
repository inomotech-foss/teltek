from teltek.codec import Codec12, Codec12Type, CodecId, MessageFrame


def test_encode_request():
    expected = bytes.fromhex("000000000000000F0C010500000007676574696E666F0100004312")
    assert _encode_request("getinfo") == expected


def test_decode_response():
    raw = bytes.fromhex(
        "00000000000000900C010600000088494E493A323031392F372F323220373A3232205254433A323031392F372F323220373A3533205253543A32204552523A"
        "312053523A302042523A302043463A302046473A3020464C3A302054553A302F302055543A3020534D533A30204E4F4750533A303A3330204750533A312053"
        "41543A302052533A332052463A36352053463A31204D443A30010000C78F"
    )
    expected = "INI:2019/7/22 7:22 RTC:2019/7/22 7:53 RST:2 ERR:1 SR:0 BR:0 CF:0 FG:0 FL:0 TU:0/0 UT:0 SMS:0 NOGPS:0:30 GPS:1 SAT:0 RS:3 RF:65 SF:1 MD:0"
    assert _decode_request(raw) == expected


def _encode_request(command: str) -> bytes:
    msg = Codec12(type=Codec12Type.REQUEST, content=command)
    return msg.to_message().encode()


def _decode_request(data: bytes) -> str:
    frame = MessageFrame.decode(data)
    assert frame.codec_id == CodecId.CODEC_12
    msg = Codec12.from_message(frame)
    assert msg.type == Codec12Type.RESPONSE
    return msg.content
