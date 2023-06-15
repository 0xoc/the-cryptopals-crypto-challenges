import base64


def hex2bytes(hex_string: str):
    return bytes.fromhex(hex_string)


def hex2base64(hex_string: str):
    return base64.b64encode(hex2bytes(hex_string)).decode("utf-8")


def xor(a: str, b: str):
    assert len(a) == len(b)

    _xor = [_a ^ _b for _a, _b in zip(hex2bytes(a), hex2bytes(b))]

    return bytes(_xor).hex()
