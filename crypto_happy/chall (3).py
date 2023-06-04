import base64

FLAG = "flag{asdf}"

FLAGenc = FLAG[::-1].encode().hex()
print(FLAGenc, type(FLAGenc))
HAPPY_NUM = [ord(i) for i in FLAGenc]

for i, c in enumerate(FLAGenc):
    print(ord(c), ord(c)^(HAPPY_NUM[i]+i), HAPPY_NUM[i])

 
asd = [(ord(c) for c in FLAGenc)]
print(asd)
ciphertext = [(ord(c)^(HAPPY_NUM[i]+i)) for i,c in enumerate(FLAGenc)]

print(f"ciphertext = {ciphertext}")