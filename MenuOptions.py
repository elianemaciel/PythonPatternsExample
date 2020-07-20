#!/usr/bin/env python3

from Register import Register
from TurmaComposite import TurmaComposite
from AlunoComposite import AlunoComposite


class MenuOptions:
    """
    Padrão de Criação Singleton
    O método classmethod instance() verifica se já existe uma instância da classe e caso não exista, ele cria essa instância e retorna para o usuário.
    """

    _instance = None

    def __init__(self):
        self.composite = TurmaComposite()
        self.composite_aluno = AlunoComposite()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def show_menu(self):
        print("------------------------------------------------------------\n")
        print("                   Instituição TI                           \n")
        print("------------------------------------------------------------\n")
        print("Escolha uma das opções a seguir:\n")
        print(" 1) Listar todas as Turma\n")
        print(" 2) Informar dados de uma turma\n")
        print(" 3) Consultar os dados de uma turma\n")
        print(" 4) Consultar estatísticas gerais\n")
        print(" 5) Sair do sistema\n")
        print("------------------------------------------------------------\n")

    def option_um(self):
        self.composite.show_all()

    def option_dois(self):
        register = Register()
        turma = register.cadastrar_turma(self.composite)

        option = 'S'

        while option.upper() == "S":
            aluno = register.cadastrar_aluno(self.composite_aluno)
            turma.add_aluno(aluno)
            option = input('Deseja cadastrar novo aluno? ')

    def option_tres(self):
        codigo = input("Digite o código da turma: ")
        turma = self.composite.get(codigo)
        print(turma)
        turma.show_alunos()

    def option_quatro(self):
        self.composite.show_all_detail()
        total, aprovados, percent = self.composite_aluno.statistics()
        print(
            """
            Total de alunos na instituição: {}
            Total de aprovados: {}
            Percentual de Aprovados: {}""".format(
                total,
                aprovados,
                percent
            )
        )
