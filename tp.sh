#!/bin/bash

path=false
time=false

while getopts "a:e:pt" opt; do
    case $opt in
        a)
            algorithm=$OPTARG
            ;;
        e)
            coords=$OPTARG
            ;;
        p)
            path=true
            ;;
        t)
            time=true
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

if [ -z "$algorithm" ] || [ -z "$coords" ]; then
    echo "Erreur: les arguments -a et -e sont obligatoires." >&2
    exit 1
fi

if [ "$algorithm" != "glouton" ] && [ "$algorithm" != "progdyn" ] && [ "$algorithm" != "approx" ]; then
    echo "Erreur: algorithme invalide. Utilisez -a avec les valeurs suivantes : glouton, progdyn, approx." >&2
    exit 1
fi

nCities=${coords#N}
nCities=${nCities%%_*} 

python3 ./inst_gen.py -s $nCities

if [ ! -f "$coords" ]; then
    echo "Erreur: le fichier $coords n'existe pas." >&2
    exit 1
fi

python3 ./main.py $algorithm $coords $time $path

exit 0