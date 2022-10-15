import random
from prg.prg import largestprime
from cpa import OFB_CPA_enc, OFB_CPA_dec


def run():
    print("enter 1 for encryption, 2 for decryption")
    choice = int(input())
    if choice == 1:
        print("Enter message in decimal format:")
        m = int(input())
        print("Enter key in decimal format:")
        k = int(input())
        print("Enter original key length(of binary format) in decimal format:")
        key_len = int(input())
        p = largestprime(pow(2, key_len))
        # chosen any random g: not used rand function so that it doesn't keep changing for same seed.
        g = int((p - 1) / 2 + 1)
        # g = random.randint(1, p - 1)
        print("CPA encryption:", OFB_CPA_enc(m, k, key_len, p, g))

    elif choice == 2:
        print("Enter cipher in binary format:")
        c = input()
        print("Enter key in decimal format:")
        k = int(input())
        print("Enter original key length(of binary format) in decimal format:")
        key_len = int(input())
        p = largestprime(pow(2, key_len))
        # chosen any random g: not used rand function so that it doesn't keep changing for same seed.
        g = int((p - 1) / 2 + 1)
        # g = random.randint(1, p - 1)
        print("CPA decryption:", int(OFB_CPA_dec(c, k, key_len, p, g), 2))

    return 0


run()
