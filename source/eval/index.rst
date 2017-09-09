#######################
Examen pratique
#######################

Consignes générales
===================

L'examen se réalise directement sur REPL.it avec le lien d'inscription
https://repl.it/classroom/invite/F0OHtI3.


Question 1 : code de Hamming
============================

..  warning::

    Dans cet exercice, les fonctions suivantes de Python ne sont pas permises.
    Vous pouvez les utiliser pour tester votre code et expérimenter mais leur
    usage est impossible au sein de la fonction ``hamming_encode`` car les tests
    ne seront pas validés.

    *   ``bin(n)``
    *   ``int(n, 2)``
    *   ``show_bin(n, fill)``

À l’aide des fonctions déjà présentes dans le code, développez une fonction

..  code-block:: python

    hamming_encode(N : int, size : nb_ctrl) => int

qui prend les bits du nombre ``N`` et forme un mot de code comportant
``nb_ctrl`` bits de contrôle. Cette fonction doit lever l'exception
``ValueError`` si le nombre de bits de contrôle est insuffisant pour coder tous
les bits présents dans le mot à coder (nombre entier ``N``).

Conseils
--------

Étudier le fonctionnement des fonctions suivantes (dont certaines ont été
demandée dans l'examen théorique ...). Dans toutes les fonctions, la position
des bits est comptée à partir de zéro de puis la droite.


    *   ``sum_bits(n)`` : effectue la somme des bits formant l'entier ``n``.

    *   ``set_kth_bit(n, k)`` : retourne l'entier ``n`` en mettant à 1 le bit à la position ``k``

    *   ``bits_len(n)`` : renvoie le nombre de bits nécessaires pour coder le nombre ``n``

    *   ``insert_bit(n, bit, k)`` : retourne l'entier ``n`` en insérant un bit
        de valeur ``bit`` à la position ``k``.

    *   ``controlled_bits(n, k)`` : renvoie un entier dont les bits à 1
        indiquent les positions contrôlées par le bit de contrôle ``k`` dans un mot
        de code contenant ``n`` bits de contrôle



Exemples
--------

..  code-block:: pycon

    >>> encoded = hamming_encode(0b1010, nb_ctrl=3)
    >>> encoded
    82
    >>> bin(encoded)
    0b1010010
    >>> hamming_encode(0b100111001001110, 3)
    Traceback (most recent call last):
    File "python", line 1, in <module>
    File "python", line 171, in hamming_encode
    ValueError: Not enough control bits


Espace de travail
-----------------

..  raw:: html

    <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/student_embed/assignment/136334/52aeadd8a41f95a4927832ff2c4dbffa"></iframe>


Question 2 : vérification avec la formule de Luhn
=================================================

Résolvez le problème ci-dessous (consignes dans REPL.it)

..  raw:: html

    <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/student_embed/assignment/136574/4c8556aa50006b34a8a3dca76775cfb7"></iframe>
