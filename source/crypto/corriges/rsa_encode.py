# publicKey = [97213511, 6551]
publicKey = [11023, 11]

def encode(text):
    ''' prend un texte comportant des caractères ASCII et génère une liste de
    nombres représentant le texte crypté '''
    m, e = publicKey
    encoded = []

    for ch in text:
        r = ord(ch)
        s = int(r**e % m)
        encoded.append(s)

    return encoded

with open('original.txt', 'r') as inFile:
    text = inFile.read()

print( "Original message : ", text)
crypto = encode(text)
print( "Encrypted message :", crypto)

with open("secret.txt", "w") as outFile:
    outFile.write('\n'.join(map(str, crypto)))

