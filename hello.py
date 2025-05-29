#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem      .
correspondente.

usage:

Tenha a variavel LANG devidamente configurada ex:


    export LANG=pt_BR

ou informe atraves do CLI argument `--lang`

Execucao:

    python3 hello.py
    ou
    ./hello.py
    
"""
__version__ = "0.1.3"
__author__ = "Vanderson Macedo"
__license__ = "Unlicense"

# Dunder = __

# Este programa imprime Hello World
import os
import sys

arguments = {"lang": None, "count": 1}
    
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value


current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repeticao
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose the language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Ola, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# O(1) constante
print(msg[current_language] * int(arguments["count"]))
