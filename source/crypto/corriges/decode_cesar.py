'''

Correction des exercices sur le chiffre de César

'''

import string

###############################################################
## Fonction pour décrypter le crypto-texte avec la clé ``key``
###############################################################
def decode_cesar(text, key):
    alphabet = string.ascii_uppercase + " "
    
    dec = ""
    for ch in text:
        if ch != "\n":
            i = alphabet.index(ch)
            ch = alphabet[(i - key) % 27]
        dec += ch
    return dec


###############################################################
## Exercice 1 : test de toutes les clés = force brute
###############################################################
def brute_force(encrypted):
    for key in range(1, 27):
        print("key : ", key)
        msg = decode_cesar(encrypted, key)
        print("Message:\n", msg)
        print("------------")


###############################################################
## Exercice 2 : deviner la clé par analyse des fréquences
###############################################################
def guess_key(text):
    freqs = {}
    
    for c in text:
        try:
            freqs[c] += 1
        except:
            freqs[c] = 1
            
    items = freqs.items()
    sorted_items = sorted(items, key=lambda x: x[1])
    max_char = sorted_items[-1][0]

    return ord(max_char) - ord('E')


def clever_cesar_decrypt(encrypted):
    
    # on devine la clé sur la base de l'analyse des fréquences ... ne fonctionne
    # pas toujours
    key = guess_key(encrypted)
    print("Guessed Cesar key", key)

    original = decode_cesar(encrypted, key)

    print("Original message : ", original)
    


###############################################################
## Programme principal
###############################################################
if __name__ == '__main__':
    with open("cesar_01_secret.txt", 'r') as fd:
        encrypted = fd.read()

        # Brute force (exo 1)
        print("Décryptage en utilisant la force brute ... essai de toutes les clés :")
        brute_force(encrypted)

        # Analyse des fréquences (exo 2)
        print("Décryptage en utilisant l'analyse des fréquences pour deviner la clé :")
        clever_cesar_decrypt(encrypted)


