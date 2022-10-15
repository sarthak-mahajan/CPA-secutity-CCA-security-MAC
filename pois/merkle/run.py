import random
from prg.prg import largestprime
from merkle import merkle


def run():
    print("Enter original key length(of binary format) in decimal format:")
    key_len = int(input())
    print("Enter the message to be hashed")
    m = int(input())

    q = largestprime(pow(2, key_len))
    # chosen any random g: not used rand function so that it doesn't keep changing for same seed.
    g = int((q - 1) / 2 + 1)
    # g = random.randint(1, p - 1)
    h = int((q - 8) / 9 + 1)
    print("n bit hash is:", merkle(m, key_len, q, g, h))
    return 0


run()
