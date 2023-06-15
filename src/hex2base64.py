import base64


def hex2base64(hex_string: str):
    return base64.b64encode(bytes.fromhex(hex_string)).decode("utf-8")
