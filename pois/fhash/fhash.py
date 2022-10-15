import random

#  x1,x2 are decimal
# length of q should be same as length of key_len********
#  based on key length
# g = 3
# h = 5
# q = 7

# ley_len input???


def fixed_hash(x_1, x_2, q, g, h):
    # g= random.randint(1,q-1)
    # h= random.randint(1,q-1)
    hash = (pow(g, x_1, q) * pow(h, x_2, q)) % q
    return hash
