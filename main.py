from src.set1.break_repeating_xor import RepeatingXorBreaker
import base64


if __name__ == "__main__":
    # open file 6.txt
    ct = open("tests/fixtures/6.txt").read().replace("\n", "")

    ct = base64.b64decode(ct)

    breaker = RepeatingXorBreaker(ct)
    pt = breaker.break_xor()

    print("final result:")
    print(pt)
