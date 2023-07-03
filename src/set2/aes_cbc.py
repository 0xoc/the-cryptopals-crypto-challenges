import pyaes

from src.set2.PKC7 import pad, remove_pad


def encrypt(plain_text: bytes, key: bytes, iv: bytes = b"fake 0th ciphertext block"):
    aes = pyaes.AES(key)

    # split plaintext into 16-byte blocks
    padded_plaintext = pad(plain_text, 16)

    # split plaintext into 16-byte blocks
    blocks = [padded_plaintext[i : i + 16] for i in range(0, len(padded_plaintext), 16)]

    # encrypt each block
    for i in range(len(blocks)):
        # XOR the current block with the previous block
        if i > 0:
            previous_block = blocks[i - 1]
        else:
            previous_block = iv

        blocks[i] = bytes([a ^ b for a, b in zip(blocks[i], previous_block)])
        blocks[i] = bytes(aes.encrypt(blocks[i]))

    return b"".join(blocks)


def decrypt(cipher_text: bytes, key: bytes, iv: bytes = b"fake 0th ciphertext block"):
    aes = pyaes.AES(key)

    # split ciphertext into 16-byte blocks
    blocks = [cipher_text[i : i + 16] for i in range(0, len(cipher_text), 16)]

    plain_text = b""

    # decrypt each block
    for i in range(len(blocks)):
        # XOR the current block with the previous block
        if i > 0:
            previous_block = blocks[i - 1]
        else:
            previous_block = iv

        decrypted = bytes(aes.decrypt(blocks[i]))
        decrypted = bytes([a ^ b for a, b in zip(decrypted, previous_block)])

        plain_text += decrypted

    # remove padding
    plain_text = remove_pad(plain_text)

    return plain_text
