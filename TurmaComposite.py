#!/usr/bin/env python3
from models.Turma import Turma


class TurmaComposite(Turma):

    def __init__(self):
        self._children = []

    def add(self, turma):
        self._children.append(turma)

    def show_all(self):
        if len(self._children) == 0:
            print("Não possui itens cadastradas.")
        for item in self._children:
            print(item)

    def get(self, string):
        for item in self._children:
            if string.lower() == item.codigo.lower():
                return item

    def show_all_detail(self):
        for item in self._children:
            aprovados = item.calc_aprovados()
            percent_aprovados = item.calc_percent_aprovados(aprovados)
            print(item)
            print("Número de aprovados: {}\n Percentual de Aprovados: {}\n".format(
                    aprovados,
                    percent_aprovados
                )
            )





