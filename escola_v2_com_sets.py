#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividade.

Imprimir a lista de criancas agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles =  ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

#listar alunas em cada atividade por sala

atividades = [
    ("Ingles",aula_ingles),
    ("Musica",aula_musica),
    ("Dança",aula_danca)
]

#listar alunas em cada atividade por sala

for nome_atividade,  atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40 )

    # Sala1 que tem intersecao com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print("sala1 ", atividade_sala1)
    print("sala2 ", atividade_sala2)
    print()
    print("#" * 40)
