#!/usr/bin/env python3

from models.Aluno import Aluno


class AlunoComposite(Aluno):

    def __init__(self):
        self._children = []

    def add(self, aluno):
        self._children.append(aluno)

    def show_all(self):
        if len(self._children) == 0:
            print("Não possui itens cadastradas.")
        for item in self._children:
            print(item)

    def statistics(self):
        total = len(self._children)
        aprovados = 0
        for aluno in self._children:
            if aluno.is_aproved():
                aprovados += 1
        percert = aprovados / total * 100

        return total, aprovados, percert
