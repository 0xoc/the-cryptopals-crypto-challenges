from src.set1.break_repeating_xor import RepeatingXorBreaker
import base64
from src.set1.detect_ecb import ECBDetector
from src.set1.aes_ecb import AECECBBreak

if __name__ == "__main__":
    with open("tests/fixtures/8.txt", "r") as f:
        data = f.read()

    ciphertexts = [base64.b64decode(ct) for ct in data.split("\n")]

    for ciphertext in ciphertexts:
        if ECBDetector(ciphertext).is_ecb():
            print(ciphertext)
            print(AECECBBreak(ciphertext).decrypt(b"YELLOW SUBMARINE"))
