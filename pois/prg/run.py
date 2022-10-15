import random
from prg import PRG, largestprime


def run():
    print("Enter key in decimal format:")
    k = int(input())
    print("Enter expanded length(of binary format) that you want in decimal format:")
    new_l = int(input())
    print("Enter original key length(of binary format) in decimal format:")
    key_len = int(input())
    p = largestprime(pow(2, key_len))
    # chosen any random g: not used rand function so that it doesn't keep changing for same seed.
    g = int((p - 1) / 2 + 1)
    # g = random.randint(1, p - 1)
    print("Pseudo random number:", PRG(k, new_l, key_len, p, g))
    return 0


run()
