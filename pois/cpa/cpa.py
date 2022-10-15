import random

from prg.prg import pad
from prf.prf import PRF

#  assume m_l >=l always
#  assuming last bock is padded on right side
# m, k are decimal
def OFB_CPA_enc(m, k, key_len, p, g):
    m_bin = pad(key_len, format(m, "b"))
    m_l = len(m_bin)
    m_chunks = [m_bin[i : i + key_len] for i in range(0, m_l, key_len)]
    l = len(m_chunks[-1])
    if l < key_len:
        for i in range(0, key_len - l):
            m_chunks[-1] = m_chunks[-1] + "0"
    # iv_bin=''.join([str(random.randint(0,1)) for _ in range(key_len)])
    # iv=int(iv_bin,2)
    iv = key_len - l
    iv_bin = pad(key_len, format(iv, "b"))
    cipher = []
    cipher.append(iv_bin)
    r = iv
    for i in m_chunks:
        r = int(PRF(r, k, key_len, p, g), 2)
        c = r ^ int(i, 2)
        cipher.append(pad(key_len, format(c, "b")))
    cipher = "".join(cipher)
    return cipher


#  c is binary, k is decimal
def OFB_CPA_dec(c, k, key_len, p, g):
    c_l = len(c)
    c_chunks = [c[i : i + key_len] for i in range(0, c_l, key_len)]
    iv_bin = c_chunks[0]
    iv = int(iv_bin, 2)
    message = []
    r = iv
    for i in c_chunks[1:]:
        r = int(PRF(r, k, key_len, p, g), 2)
        m = r ^ int(i, 2)
        message.append(pad(key_len, format(m, "b")))
    message = "".join(message)
    message = message[0 : len(message) - iv]
    return message
