import random
import math

# defined for dlp: can be random but fixed for a program, p needs to be near 2^n , n=key_len
# p = 23
# g = random.randint(1, p - 1)


def primecheck(N):
    for i in range(2,1+int(math.sqrt(N))  , 1):
        if N % i == 0:
            return False
    return True


# 2^(n)=p, if n is key_len
def largestprime(p):
    for i in range(1, p):
        val = p - i
        if primecheck(val) == 1:
            return val
    return -1


# takes in binary input
def pad(key_len, num):
    # num=format(num,"b")
    if len(num) < key_len:
        for i in range(0, key_len - len(num)):
            num = "0" + num
    return num


# assign p a very large prime value by default: 20 bit prime rn
#  s is decimal


def dlp(s, p, g):
    ans = pow(g, s, p)
    # print(ans)
    return ans


#  calculates MSB of "n" bit string, leading 0's inclused
#  num decimal
def hc_dlp(num, key_len):
    # print(num,key_len,type(num))
    num = format(num, "b")
    num = pad(key_len, num)
    ans = num[0]
    return ans


#  seed decimal
# try to take last "l" bits of dlp
def single_PRG(seed, key_len, p, g, func="dlp"):
    if func == "dlp":
        b = hc_dlp(seed, key_len)
        a = dlp(seed, p, g)
        ans = (a, b)
        return ans


#  seed decimal
def PRG(seed, new_l, key_len, p, g):
    expan = new_l - key_len
    s = seed
    out = ""
    for i in range(0, expan):
        sin_prg = single_PRG(s, key_len, p, g)
        s = sin_prg[0]
        out += sin_prg[1]
    ans = pad(new_l, format(s, "b") + out)
    return ans
