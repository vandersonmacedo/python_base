#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10

Tabuada do 1
1
2
3
...

_________________________
Tabuada do 2
2
4

...
________________________

"""
__version__ = "0.1.1"
__author__ = "Vanderson Macedo"


#Iterable (percorriveis)

numeros = list(range(1, 11))

# Para cada numero em numeros:

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} X {n2} = {resultado}"))

    print("#" * 18)
        
