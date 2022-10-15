import random
from fhash.fhash import fixed_hash
from merkle.merkle import merkle
from prg.prg import pad


def HMAC(m, k, key_len, q, g, h):
    opad = format(0x36, "b")
    ipad = format(0x5C, "b")
    op = ""
    for i in range(0, key_len, len(opad)):
        op = op + opad
    op = op[:key_len]
    ip = ""
    for i in range(0, key_len, len(ipad)):
        ip = ip + ipad
    ip = ip[:key_len]
    x1 = k ^ int(ip, 2)
    iv = 2 ** (key_len) - 1
    h_ip = fixed_hash(x1, iv, q, g, h)
    h_merk = int(merkle(m, key_len, q, g, h, h_ip), 2)
    x2 = k ^ int(op, 2)
    h_op = fixed_hash(x2, iv, q, g, h)
    hmac = fixed_hash(h_merk, h_op, q, g, h)
    return pad(key_len, format(hmac, "b"))
