from src.set1.detect_single_byte_xor_cipher import detect
from src.set1.single_byte_xor_cipher import decode


def test_single_byte_xor_cipher():
    _hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    _plaintext = "Cooking MC's like a pound of bacon"

    assert decode(_hex_str) == _plaintext


def test_detect_single_byte_xor_cipher():
    ciphertexts = []
    with open("tests/fixtures/4.txt") as f:
        ciphertexts = f.read().splitlines()

    assert detect(ciphertexts) == "Now that the party is jumping\n"
