#!/bin/bash

showMatix=false
time=false

while getopts "e:p" opt; do
    case $opt in
        e)
            fileName=$OPTARG
            ;;
        p)
            showMatrix=true
            ;;
        \?)
            echo "Option invalide: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "L'option -$OPTARG requiert un argument." >&2
            exit 1
            ;;
    esac
done

if [ -z "$fileName" ]; then
    echo "Erreur: l'argument -e est obligatoire." >&2
    exit 1
fi

fileName=${fileName#N}

if [ ! -f "$fileName" ]; then
    echo "Erreur: le fichier $fileName n'existe pas." >&2
    exit 1
fi

python3 ./main.py $fileName $showMatrix

exit 0