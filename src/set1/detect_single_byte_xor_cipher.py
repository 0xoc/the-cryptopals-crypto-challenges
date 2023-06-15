from src.set1.single_byte_xor_cipher import decode, score


def detect(ciphertexts):
    candidates = []
    for ciphertext in ciphertexts:
        candidates.append(decode(ciphertext).encode("utf-8"))

    return max(candidates, key=score).decode("utf-8")
