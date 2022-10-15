import random
from prg.prg import pad
from prf.prf import PRF

# m,k are decimal
def CBC_MAC(m, k, key_len, p, g):
    m_bin = pad(key_len, format(m, "b"))
    m_l = len(m_bin)
    m_chunks = [m_bin[i : i + key_len] for i in range(0, m_l, key_len)]
    l = len(m_chunks[-1])
    if l < key_len:
        for i in range(0, key_len - l):
            m_chunks[-1] = m_chunks[-1] + "0"

    r = int(PRF(m_l, k, key_len, p, g), 2)
    for i in m_chunks:
        r = r ^ int(i, 2)
        r = int(PRF(r, k, key_len, p, g), 2)
    return pad(key_len, format(r, "b"))
