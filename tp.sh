#!/bin/bash
python3 inst_gen.py -S3 -t3 -n2
gcc -c main.cpp -o main

# Ajouter les flags et initialiser un parametre pour chaque flags.
./main 2 


exit 0