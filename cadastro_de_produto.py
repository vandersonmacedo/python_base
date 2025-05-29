#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

from pprint import pprint


produto = {
    "nome": "Caneta",
    "Cores": ["azul", "Branco"],
    "preco": 3.23,
    "dimensao": {
        "Altura":12.1,
        "Largura":0.8,
    },
    "estoque": True,
    "codigo": 45678,
    "codebar": None,
}   

cliente = {
    "nome": "Bruno"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

pprint(compra)

total_compra = compra["quantidade"] * compra['produto']["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"    
)
