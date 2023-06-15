def decode(hex_string: str):
    """Find the single-byte XOR key for a given hex string."""

    # Convert hex string to bytes
    bytes_string = bytes.fromhex(hex_string)

    # Create a list of all possible keys
    keys = [bytes([i]) for i in range(256)]

    # Create a list of all possible plaintexts
    plaintexts = [xor(bytes_string, key) for key in keys]

    # Create a list of all possible scores
    scores = [score(plaintext) for plaintext in plaintexts]

    # Return the plaintext with the highest score
    try:
        return plaintexts[scores.index(max(scores))].decode("utf-8")
    except UnicodeDecodeError:
        return ""


def xor(bytes_string: bytes, key: bytes):
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
