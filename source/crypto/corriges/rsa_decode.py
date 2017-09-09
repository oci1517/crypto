privateKey = [11023, 5891]

def decode(encoded):
    ''' prend une liste de nombres et retourne la chaine de caractère du texte en clair '''
    
    m, d = privateKey

    decoded = ""
    for s in encoded:
        r = s**d % m
        decoded += chr(r)
    return decoded


secret = []
with open('secret.txt', 'r') as inFile:
    for line in inFile:
        secret.append(int(line))

message = decode(secret)

with open("message.txt", "w") as outFile:
    outFile.write(message)

