from src.utils import hex2base64, xor


def test_hex2base64():
    _hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    _base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    assert hex2base64(_hex_str) == _base64


def test_xor():
    a = "1c0111001f010100061a024b53535009181c"
    b = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"

    assert xor(a, b) == expected
