Opérateurs sur les bits
#######################

En plus des opérateurs que nous avons vus jusqu'à présent qui travaillent sur
des nombres entiers dans leur ensemble, il existe des opérateurs spéciaux
capables d'opérer sur les bits individuels des nombres entiers.

Opérateurs sur les bits (Bitwise operators)
===========================================

Python met à dispostion les opérateurs suivants capables d'opérer sur les bits
individuels des nombres entiers :

``x << y``
----------

Décale les bits de ``x`` de ``y`` positions vers la gauche et remplit les bits
de poids faibles avec des 0. Cela revient au même que de multiplier ``x`` par
``2**y``.

Dans le code ci-dessous, on décale successivement, au sein de la boucle ``for``
les bits de la variable ``result``. L'instruction ``print(...)`` affiche
successivement les bits ainsi que la valeur décimale.

..  raw:: html

    <script src="//repl.it/embed/Hd9P/4.js"></script>

..  tip::

    *   On constate que le décalage des bits de ``y`` positions vers la gauche
        correspond à une multiplication par :math:`2^y`.

    *   La fonction ``int(digits, base)`` permet de convertir la chaine de
        chiffres ``digits`` exprimée en base ``base`` vers la notation décimale.

..  raw:: html

    <script src="//repl.it/embed/Hd9P/0.js"></script>

``x >> y``
----------

Décale les bits de ``x`` de ``y`` positions vers la droite et remplit les bits de poids fort avec des 0. Cela revient au même que de diviser (``//``) ``x`` par ``2**y``.

L'exemple suivant montre que, lorsque les bits "sortent" vers la droite, ils
sont simplement jetés à la poubelle :

..  raw:: html

    <script src="//repl.it/embed/Hd9P/5.js"></script>

``x & y``
----------

Effectue un ET logique bit-à-bit : dans le résultat final, un bit est à 1 si et
seulement si les bits de même poids de ``x`` et ``y`` sont tous deux à 1.

..  raw:: html

    <script src="//repl.it/embed/Hd9P/8.js"></script>

``x | y``
----------

Effectue un OU logique bit-à-bit : dans le résultat final, un bit est à 0 si et
seulement si les bits de même poids de ``x`` et ``y`` sont tous deux à 0.

..  raw:: html

    <script src="//repl.it/embed/Hd9P/7.js"></script>

``~ x``
-------

Effectue une inversion des bits. Cela revient au même que d'effectuer
l'opération ``-x - 1`` (complément à deux).

Dans cet exemple, pour afficher les bits de ``c = ~ a``, il a fallu utiliser une
autre fonction que précédemment car la fonction ``bin(...)`` n'affiche pas
vraiment les bits des nombres négatifs en complément à deux.


..  raw:: html

    <script src="//repl.it/embed/Hd9P/12.js"></script>


``x ^ y``
----------

Effectue un OU exclusif bit à bit : un bit du résultat final est à 1 si et
seulement si l'un des bits correspondant de ``x`` ou ``y`` est à 1 et l'autre à
0.

..  raw:: html

    <script src="//repl.it/embed/Hd9P/13.js"></script>


Exercices
=========

#.  Expliquer les comportements suivants en sachant que Python utilise la
    représentation en complément à deux pour les nombres entiers négatifs :

    ..  code-block:: python

        >>> -1 >> 1
        -1
        >>> ~ 255
        -256

#.  Epxliquer le fonctionnement de la fonction ``show_bin(n, fill=8)`` utilisée
    dans les premires exemples et expliquer pourquoi elle n'est pas utilisable
    avec les entiers négatifs

    ..  code-block:: python

        def show_bin(n, fill=8):
            format_string = "{00:>" + str(fill) + "}"
            return format_string.format(bin(n).split('b')[1].zfill(fill))


#.  Epxliquer le fonctionnement de la fonction ``show_bin(n, fill=8)`` utilisée
    dans les exemples ci-dessus pour afficher les bits des nombres entiers

    ..  code-block:: python

        def show_bin(n, fill=8):
            binary = []
            while binary != 0 and len(binary) < fill:
                binary.append(str(n & 1))
                n = n >> 1
            print(''.join(reversed(binary)))


#.  Nous avons vu dans le chapitre sur les réseaux qu'un masque de sous réseaux
    servait à définir les adresses appartenant à un réseau local. Ainsi, le
    masque réseau ``255.255.0.0`` permet de définir le sous-réseau
    ``192.168.0.0/16``.

    Définir une fonction ``subnet_ip(ip : str, netmask : str) => str`` qui
    retourne sous forme de chaîne de caractères l'adresse de sous-réseau
    ``subnet_ip`` correspondant à l'adresse IP ``ip`` :

    ..  raw:: html

        <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/student_embed/assignment/123318/4347b599fe8b52b15fceef730d5707af"></iframe>


#.  Compléter la fonction ``kill_nth_bit`` pour qu'elle retourne le nombre ``n``
    en ayant mis son ``k``-ième bit à 0.

    ..  code-block:: python

        def kill_nth_bit(n, k):
            pass

    ..  raw:: html
        
        <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/student_embed/assignment/123614/1305662c80e0bb6eb90ed08cf1dd0e5d"></iframe>
    
#.  La fonction ``array_packing(numbers)`` prend une liste d'au maximum 4
    nombres entiers codés sur 8 bits et doit retourner un nombre de 32 bits où
    les 8 bits de poids faible correspondent aux bits du premier élément de
    ``numbers`` et ainsi de suite jusqu'aux bits du dernier élément de
    ``numbers`` qui occuperont les 8 bits de poids fort du résultat.

    ..  raw:: html
        
        <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/student_embed/assignment/123780/92c18bd3050e0414452b056f45f90a7d"></iframe>

#.  On donne deux entiers ``a`` et ``b`` tels que :math:`0 \leq a \leq b`. 
    Développer une fonction ``range_bit_count(a, b)`` qui retourne le nombre de
    bits à 1 dans l'ensemble des nombres :math:`n` tels que :math:`a \leq n \leq b`.

    ..  admonition:: Exemple
        :class: tip

        ::
        
            >>> rangeBitCount(a=2, b=7)
            11

        En effet, pour ``a = 2`` et ``b = 7`` les nombres à considérer sont
        ``[2, 3, 4, 5, 6, 7]``, à savoir ``[10, 11, 100, 101, 110, 111]`` en
        binaire, ce qui donne un nombre de bits à 1 valant
        
        ::
        
            1 + 2 + 1 + 2 + 2 + 3 = 11.

    ..  raw:: html

        <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/student_embed/assignment/126761/ede3b40d4a5bf4cb1c08450823091e63"></iframe>

#.  Inverser l'ordre des bits dans l'entier ``n`` passé à la fonction
    ``mirror_bits(n)``.

    ..  admonition:: Exemple
        :class: tip
                
        ::
    
            >>> mirrorBits(97)
            67

        Car :math:`97_{10} = 1100001_2` en binaire, ce qui correspond à
        ``1000011`` après retournement des bits, ce qui correspond à 67 en base
        10.

    ..  raw:: html

        <iframe frameborder="0" width="100%" height="600px" src="https://repl.it/student_embed/assignment/126762/cdb2d2ecc6fdcd514924421bd14d7074"></iframe>