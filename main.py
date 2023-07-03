from base64 import b64decode
from src.set2.aes_cbc import decrypt

if __name__ == "__main__":
    with open("tests/fixtures/cbc.txt", "r") as f:
        data = f.read().replace("\n", "")

    key = b"YELLOW SUBMARINE"
    iv = 0x00.to_bytes(16, "big")

    ciphertext = b64decode(data)

    decrypted = decrypt(ciphertext, key, iv)

    print(decrypted.decode("utf-8"))
