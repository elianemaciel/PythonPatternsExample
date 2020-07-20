#!/usr/bin/env python3

from models.Disciplina import Disciplina
from models.Professor import Professor
from models.Aluno import Aluno
from models.Turma import Turma


class Register(object):
    """
    Padrões Façade
    """

    def cadastrar_disciplina(self, disciplina):
        return Disciplina.get_or_create(disciplina)

    def cadastrar_professor(self, professor):
        return Professor.get_or_create(professor)

    def cadastrar_turma(self, composite):
        print("Dados para a turma: ")
        codigo = input("Digite o código da turma: ")
        nome = input("Digite o nome do professor: ")
        disciplina_str = input("Digite o disciplina: ")
        disciplina = self.cadastrar_disciplina(disciplina_str)
        professor = self.cadastrar_professor(nome)

        turma = Turma(
            codigo=codigo,
            disciplina=disciplina,
            professor=professor
        )
        composite.add(turma)

        return turma

    def cadastrar_aluno(self, composite):

        print("Dados do aluno: ")
        codigo = input("Digite o código: ")
        nome = input("Digite o nome do aluno: ")
        email = input("Digite o e-mail: ")
        notas = input("Digite as 3 notas separadas por vírgola: ")
        list_notas = [int(x) for x in notas.split(",")]

        aluno = Aluno(
            codigo=codigo,
            nome=nome,
            email=email,
            notas=list_notas
        )
        composite.add(aluno)
        return aluno
