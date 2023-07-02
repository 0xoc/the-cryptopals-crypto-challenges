from src.set1.repeating_key_xor import decrypt
from src.set1.single_byte_xor_cipher import get_key
from src.utils import score


class RepeatingXorBreaker:
    def __init__(self, encrypted: bytes):
        self.encrypted = encrypted

    def break_xor(self):
        possible_key_lengths = self.get_possible_key_lengths()
        candidate_plaintexts = []

        for key_length in possible_key_lengths:
            pt = self.break_xor_for_key_length(key_length)
            candidate_plaintexts.append(pt)

        return max(candidate_plaintexts, key=score)

    def break_xor_for_key_length(self, key_length: int):
        # break the encrypted data into key_length chunks
        chunks = [
            self.encrypted[i : i + key_length]
            for i in range(0, len(self.encrypted), key_length)
        ]

        # take the first byte of each chunk and make a new chunk
        # take the second byte of each chunk and make a new chunk
        # repeat until you have key_length chunks

        key = bytes()

        for i in range(key_length):
            line = bytes()
            for j in range(len(chunks)):
                if i >= len(chunks[j]):
                    continue
                _b = chunks[j][i]
                line += bytes([_b])

            _key = get_key(line.hex())
            key += _key

        pt = decrypt(self.encrypted, key).encode("utf-8")

        print(f"{key_length}, {key}, {pt[:50]}")

        return pt

    def get_possible_key_lengths(self):
        return [i for i in range(1, 100)]
