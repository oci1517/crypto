privateKey=[97213511, 79907015]

def decode(li):
    m = privateKey[0]
    d = privateKey[1]
    enc = ""
    for c in li:
        print(c)
        s = int(c)
        r = pow(s, d, m)
        enc += chr(r)
    return enc

fInp = open("secret.txt")
krypto = []
while True:
   line = fInp.readline().rstrip("\n")
   if line == "":
       break
   krypto.append(line)
fInp.close() 

print "Krypto:\n", krypto
msg = decode(krypto)
print "Message:\n", msg

fOut = open("message.txt", "w")    
for ch in msg:
    fOut.write(ch)
fOut.close() 
