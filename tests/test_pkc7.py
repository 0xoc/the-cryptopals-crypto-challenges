from src.set2.PKC7 import pad


def test_pkc7():
    raw_data = b"YELLOW SUBMARINE"

    assert pad(raw_data, 20) == b"YELLOW SUBMARINE\x04\x04\x04\x04"
