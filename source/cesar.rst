################
Chiffre de César
################

D’après la tradition, Jules César (100 av. J.-C. - 44 av. J.-C.) utilisait déjà
la méthode suivante dans ses communications militaires : chaque caractère du
texte en clair était décalé dans l’alphabet d’un certain nombre de lettres en
reprenant au début de l’alphabet une fois arrivé au bout.

..  only:: html

    ..  sidebar:: Clé de chiffrement de César

        ..  figure:: figures/crypto-2.png
            :align: center
            :width: 95%

            Clé de chiffrement de César

..  only:: latex

    ..  figure:: figures/crypto-2.png
            :align: center
            :width: 30%

            Clé de chiffrement de César

Cette méthode utilisait deux anneaux imbriqués portant les lettres de
l’alphabet. L’anneau intérieur était décalé d’un certain nombre de positions, ce
qui constitue la clé de cryptage. Par exemple, si la clé vaut 3, le A sera codé
par un D, le B par un E, le C par un F, le D par un G etc ...

Le programme ci-dessous lit le message à crypter depuis un fichier texte pour
permettre de le modifier et de le partager facilement. Il faut écrire le texte
en clair à l’aide d’un éditeur de code standard dans le fichier ``original.txt``
qu’il faut sauvegarder dans le même dossier que le programme Python. Il faut
restreindre le message original aux lettres capitales, aux espaces et aux
retours à la ligne. On aura par exemple

::

    ON SE RETROUVE AUJOURD HUI A HUIT HEURES
    BISOUS
    TANIA

La fonction ``encode(msg)`` encode la chaine de caractères ``msg`` du message
issu du fichier texte. Elle procède en remplaçant chaque caractère original par
le caractère crypté correspondant, excepté le caractère de retour à la ligne
``\n``.

..  code-block:: python
    :linenos:

    import string
    key = 4
    alphabet = string.ascii_uppercase + " "

    def encode(text):
        enc = ""
        for ch in text:
            if ch != "\n":
                i = alphabet.index(ch)
                ch = alphabet[(i + key) % 27]
            enc += ch
        return enc
        
    fInp = open("original.txt")
    text = fInp.read()
    fInp.close() 

    print "Original:\n", text
    krypto = encode(text)
    print "Krypto:\n", krypto

    fOut = open("secret.txt", "w")
    for ch in krypto:
        fOut.write(ch)
    fOut.close()

Voici le texte crypté :

::

    SRDWIDVIXVSYZIDEYNSYVHDLYMDEDLYMXDLIYVIW
    FMWSYW
    XERME

Le décodage est implémenté de façon analogue à part le fait que les caractères
sont décalés dans l’autre sens.


..  code-block:: python
    :linenos:

    import string
    key = 4
    alphabet = string.ascii_uppercase + " "

    def decode(text):
        dec = ""
        for ch in text:
            if ch != "\n":
                i = alphabet.index(ch)
                ch = alphabet[(i - key) % 27]
            dec += ch
        return dec

    fInp = open("secret.txt")
    krypto = fInp.read()
    fInp.close() 

    print "Krypto:\n", krypto
    msg = decode(krypto)
    print "Message:\n", msg

    fOut = open("message.txt", "w")
    for ch in msg:
        fOut.write(ch)
    fOut.close()


..  admonition:: Memento
    :class: warning

    Notez qu’il faut conserver tous les caractères d’espacement du cryptotexte,
    même s’ils se trouvent au début ou à la fin de la ligne. Il est clair que
    cette méthode de cryptage peut être compromise très facilement. La manière
    la plus simple consiste simplement à tester toutes les 26 clés possibles
    jusqu’à l’obtention d’un texte en clair en français.


Exercices
=========

Exercie 1 : force brute
-----------------------

Écrivez un programme qui casse qui déchiffre le cryptotexte suivant codé à
l'aide du chiffre de César en testant successivement toutes les 27 clés
possibles.

::

    OAL SHDXTKMJXSASTVVXHLSL XSAFNALTLAGF
    UMLSASVTFSGFDQSUXSL XJXSTLSXAZ L
    ZJXXLAFZK
    XNXDAFX


Exercie 2 : analyse de fréquences
---------------------------------

Sachant que le message original a été écrit en anglais, déterminer la clé de
chiffrement utilisée pour le cryptotexte ci-dessous. Décoder le message à l'aide
de la clé trouvée.

..  tip::

    Utilisez une table de fréquence d'apparition des caractères dans la langue
    anglaise. Vous pouvez également construire une telle table en analysant un
    ouvrage en anglais contemporain.

    https://en.wikipedia.org/wiki/Letter_frequency

::


..  comment::

    Exercice 3
    ----------

    a)  Expliquer pourquoi le fait de ne pas crypter les espaces et les sauts de ligne
        affaiblit le chiffrement du message.

    b)  Modifier le chiffre ce César présenté pour qu'il encode également les caractères de séparation