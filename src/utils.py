import base64


def hex2bytes(hex_string: str):
    return bytes.fromhex(hex_string)


def hex2base64(hex_string: str):
    return base64.b64encode(hex2bytes(hex_string)).decode("utf-8")


def xor(a: str, b: str):
    assert len(a) == len(b)

    _xor = [_a ^ _b for _a, _b in zip(hex2bytes(a), hex2bytes(b))]

    return bytes(_xor).hex()


def repeating_xor(bytes_string: bytes, key: bytes):
    """XOR a bytes string with a key."""

    # Create a list of the XORed bytes
    xored_bytes = [
        bytes_string[i] ^ key[i % len(key)] for i in range(len(bytes_string))
    ]

    # Return the XORed bytes as a bytes string
    return bytes(xored_bytes)


def score(bytes_string: bytes):
    """Score a bytes string based on character frequency."""

    # Create a list of all characters in the bytes string
    characters = [chr(byte) for byte in bytes_string]

    # Create a list of all characters that are in the English alphabet
    english_alphabet = [chr(i) for i in range(97, 123)]

    # Create a list of all characters that are not in the English alphabet
    non_english_alphabet = [
        character.lower()
        for character in characters
        if character not in english_alphabet
    ]

    # Return the score
    return len(characters) - len(non_english_alphabet)
