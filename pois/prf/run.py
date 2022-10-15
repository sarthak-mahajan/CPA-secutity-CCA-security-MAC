import random
from prg.prg import largestprime
from prf import PRF


def run():
    print("Enter seed of PRF in decima format:")
    r = int(input())
    print("Enter key in decimal format:")
    k = int(input())
    print("Enter original key length(of binary format) in decimal format:")
    key_len = int(input())
    p = largestprime(pow(2, key_len))
    # chosen any random g: not used rand function so that it doesn't keep changing for same seed.
    g = int((p - 1) / 2 + 1)
    # g = random.randint(1, p - 1)
    print("PRF output:", PRF(r, k, key_len, p, g))
    return 0


run()
