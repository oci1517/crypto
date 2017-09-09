###########################
Codage des entiers relatifs
###########################

Pour coder les nombres négatifs, on utilise la valeur du bit de poids fort (tout
à gauche) pour indiquer le signe. 

*   Bit de poids fort à 0 <==> nombre positif
*   Bit de poids fort à 1 <==> nombre négatif


Complément à deux
=================

En pratique, le codage utilisé est souvent le complément à deux dont voici une
présentation vidéo

..  only:: html

    ..  youtube:: mui5ZwF77B4


Représentation de la roue
-------------------------

On peut se représenter le codage en complément à deux avec la route suivante : 

..  figure:: figures/roue_complement_2.png
    :align: center
    :width: 85%

    Roue du codage en complément à deux