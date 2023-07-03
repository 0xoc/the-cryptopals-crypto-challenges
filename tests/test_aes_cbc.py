from src.set2.aes_cbc import encrypt, decrypt


def test_aes_cbc():
    key = b"YELLOW SUBMARINE"
    iv = b"fake 0th ciphertext block"
    plaintext = b"YELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINE"

    ciphertext = encrypt(plaintext, key, iv)
    decrypted = decrypt(ciphertext, key, iv)

    assert decrypted == plaintext
