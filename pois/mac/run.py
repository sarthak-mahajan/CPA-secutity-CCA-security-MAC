import random
from prg.prg import largestprime
from mac import CBC_MAC


def run():
    print("enter 1 for tag generation, 2 for authentication")
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
        print("CBC MAC tag :", CBC_MAC(m, k, key_len, p, g))

    elif choice == 2:
        print("Enter message in decimal format:")
        m = int(input())
        print("enter token in binary format:")
        t = input()
        print("Enter key in decimal format:")
        k = int(input())
        print("Enter original key length(of binary format) in decimal format:")
        key_len = int(input())

        p = largestprime(pow(2, key_len))
        # chosen any random g: not used rand function so that it doesn't keep changing for same seed.
        g = int((p - 1) / 2 + 1)
        # g = random.randint(1, p - 1)
        new_t = CBC_MAC(m, k, key_len, p, g)
        if new_t == t:
            print("Authentication succeeded")
        elif new_t != t:
            print("Authentication failed")
    return 0


run()
