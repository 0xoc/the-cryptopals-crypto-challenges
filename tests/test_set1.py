from src.set1.break_repeating_xor import RepeatingXorBreaker
from src.set1.detect_single_byte_xor_cipher import detect
from src.set1.repeating_key_xor import encrypt
from src.set1.single_byte_xor_cipher import decode
import base64


def test_single_byte_xor_cipher():
    _hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    _plaintext = "Cooking MC's like a pound of bacon"

    assert decode(_hex_str) == _plaintext


def test_detect_single_byte_xor_cipher():
    ciphertexts = []
    with open("tests/fixtures/4.txt") as f:
        ciphertexts = f.read().splitlines()

    assert detect(ciphertexts) == "Now that the party is jumping\n"


def test_encrypt():
    plaintext = (
        "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    )

    key = "ICE"

    ciphertext = (
        "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623"
        "d63343c2a26226324272765272a282b2f20430a652e2c652"
        "a3124333a653e2b2027630c692b20283165286326302e272"
        "82f"
    )

    assert encrypt(plaintext, key) == ciphertext


def test_break_reaping_xor():
    # open file 6.txt
    ct = open("tests/fixtures/6.txt").read().replace("\n", "")

    ct = base64.b64decode(ct)

    breaker = RepeatingXorBreaker(ct)
    pt = breaker.break_xor()

    print(pt)
