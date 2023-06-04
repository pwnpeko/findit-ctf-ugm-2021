from Crypto.Util.number import *
flag = "asdf"

def nextPrime(prime):
    if isPrime(prime):
        return prime
    else:
        return nextPrime(prime+1)

p = getPrime(128)
q = nextPrime(7*p)
r = nextPrime(p*q)
s = nextPrime(q*r)
n = p*q*r*s

phin = (p-1)*(q-1)*(r-1)*(s-1)
e = 65537
assert GCD(e,phin) == 1
m = bytes_to_long(flag.encode("ascii"))
c = pow(m,e,n)
c = long_to_bytes(c).hex()
print(c)
print(n)
