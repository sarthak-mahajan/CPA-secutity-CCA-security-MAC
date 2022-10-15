import random

from prg.prg import pad, PRG


# r,k decimal input
def PRF(r, k, key_len, p, g):
    new_l = 2 * key_len
    r_bin = pad(key_len, format(r, "b"))
    s = pad(key_len, format(k, "b"))
    for i in r_bin:
        prg = PRG(int(s, 2), new_l, key_len, p, g)
        if i == "0":
            s = prg[0 : int(new_l / 2)]
        elif i == "1":
            s = prg[int(new_l / 2) : new_l]
    return s
