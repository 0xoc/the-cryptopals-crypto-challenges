from src.utils import repeating_xor, score


def decode(hex_string: str):
    """Find the single-byte XOR key for a given hex string."""

    # Convert hex string to bytes
    bytes_string = bytes.fromhex(hex_string)

    # Create a list of all possible keys
    keys = [bytes([i]) for i in range(256)]

    # Create a list of all possible plaintexts
    plaintexts = [repeating_xor(bytes_string, key) for key in keys]

    # Create a list of all possible scores
    scores = [score(plaintext) for plaintext in plaintexts]

    # Return the plaintext with the highest score
    try:
        return plaintexts[scores.index(max(scores))].decode("utf-8")
    except UnicodeDecodeError:
        return ""
