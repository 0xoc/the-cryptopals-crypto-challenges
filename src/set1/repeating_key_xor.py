from src.utils import repeating_xor


def encrypt(msg, key):
    """Encrypt a message with a key."""
    return repeating_xor(msg.encode("utf-8"), key.encode("utf-8")).hex()


def decrypt(ciphertext: bytes, key: bytes):
    """Decrypt a ciphertext with a key."""
    return repeating_xor(ciphertext, key).decode("utf-8")
