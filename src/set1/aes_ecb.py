import pyaes


class AECECBBreak:
    def __init__(self, ciphertext: bytes):
        self.ciphertext = ciphertext

    def decrypt(self, key: bytes):
        """Decrypt the ciphertext using aes_ecb. 128-bit key."""

        aes = pyaes.AES(key)
        print(self.ciphertext)

        decrypted = "".join([chr(c) for c in aes.decrypt(self.ciphertext[0:16])])
        return decrypted
