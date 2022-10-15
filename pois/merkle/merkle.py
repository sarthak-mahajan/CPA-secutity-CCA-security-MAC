import random
from fhash.fhash import fixed_hash
from prg.prg import pad


#  m is decimal
def merkle(m, key_len, q, g, h, iv=-1):
    m_bin = pad(key_len, format(m, "b"))
    m_l = len(m_bin)
    m_chunks = [m_bin[i : i + key_len] for i in range(0, m_l, key_len)]
    if len(m_chunks[-1]) < key_len:
        for i in range(0, key_len - len(m_chunks[-1])):
            m_chunks[-1] = m_chunks[-1] + "0"
    if iv == -1:
        iv = 2 ** (key_len) - 1
    z = iv
    for i in m_chunks:
        z = fixed_hash(int(i, 2), z, q, g, h)
    fin_hash = fixed_hash(m_l, z, q, g, h)
    return pad(key_len, format(fin_hash, "b"))
