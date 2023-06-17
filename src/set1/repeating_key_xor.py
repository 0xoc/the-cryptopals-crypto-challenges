from src.utils import repeating_xor


def encrypt(msg, key):
    """Encrypt a message with a key."""
    return repeating_xor(msg.encode("utf-8"), key.encode("utf-8")).hex()
