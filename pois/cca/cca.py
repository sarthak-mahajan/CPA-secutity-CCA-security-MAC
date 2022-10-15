import random


from cpa.cpa import OFB_CPA_enc, OFB_CPA_dec
from mac.mac import CBC_MAC

# m,k are decimal
def CCA_enc(m, k, key_len, p, g):
    ciph = OFB_CPA_enc(m, k, key_len, p, g)
    tag = CBC_MAC(int(ciph, 2), k, key_len, p, g)
    fin = ciph + tag
    return fin


# c is binary, k is decimal
def CCA_dec(c, k, key_len, p, g):
    ciph = c[0 : len(c) - key_len]
    tag = c[len(c) - key_len :]
    if CBC_MAC(int(ciph, 2), k, key_len, p, g) == tag:
        message = OFB_CPA_dec(ciph, k, key_len, p, g)
        return message
    else:
        return "invalid"
