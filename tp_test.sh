#!/bin/bash

# Pour glouton et approx
for n in {"1000","5000","10000","50000","100000"}; do
    ./inst_gen.py -s $n -n 5
    python3 ./main_test.py $n
    ((i=i+1))
done

# Pour tous les algorithmes
i = 0
for n in {"5","10","15","20","25"}; do
    ./inst_gen.py -s $n -n 5 -x DP
    python3 ./main_test.py $n
    i=i+1
done

