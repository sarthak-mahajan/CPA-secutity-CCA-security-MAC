import random
from prg.prg import largestprime, pad
from fhash import fixed_hash


def run():
    print("Enter original key length(of binary format) in decimal format= n:")
    key_len = int(input())
    print(
        "Enter two n bit numbers,such that their concatenation is what you want hashed to n bits"
    )
    print("Enter the 1st n-bit number in decimal format where n=key's length")
    x_1 = int(input())
    print("Enter the 2nd n-bit number in decimal format where n=key's length")
    x_2 = int(input())
    q = largestprime(pow(2, key_len))
    # chosen any random g: not used rand function so that it doesn't keep changing for same seed.
    g = int((q - 1) / 2 + 1)
    # g = random.randint(1, p - 1)
    h = int((q - 8) / 9 + 1)
    print("n bit hash is:", pad(key_len, format(fixed_hash(x_1, x_2, q, g, h), "b")))
    return 0


run()
