#!/bin/bash
python3 inst_gen.py -S4 -t1 -n2

passCounter=0

if [[ "$1" = "-a" ]]; then
    if [[ "$2" = "conv" ]] || [[ "$2" = "strassen" ]] || [[ "$2" = "strassenSeuil" ]]; then
        algo=$2;
        ((passCounter=passCounter+1))
    fi
fi

if [ "$3" = "-e1" ]; then
    matrix1=$4
    ((passCounter=passCounter+1))
fi

if [ "$5" = "-e2" ]; then
    matrix2=$6
    ((passCounter=passCounter+1))
fi

if [ "$7" = "-p" ] || [ "$8" = "-p" ]; then
    show="show"
fi

if [ "$7" = "-t" ] || [ "$8" = "-t" ]; then
    time="time"
fi

if [[ passCounter < 3 ]]; then
    error
fi

# Ajouter les flags et initialiser un parametre pour chaque flags.
python3 ./main.py $algo $matrix1 $matrix2 $show $time

#Fonction a appler dans le cas d'un erreur.
error() {
    echo "Une erreur est survenu lors de l'appel, svp s'assurer d'avoir bien ecrit les arguments."
    exit 1
}

exit 0