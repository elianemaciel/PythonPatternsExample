#!/usr/bin/env python3

from MenuOptions import MenuOptions


def main():

    menu_options = MenuOptions.instance()
    opcao = 0
    # import ipdb; ipdb.set_trace()
    while opcao < 5:
        menu_options.show_menu()
        opcao = int(input("Digite a opção:"))
        if opcao == 1:
            menu_options.option_um()
        elif opcao == 2:
            menu_options.option_dois()
        elif opcao == 3:
            menu_options.option_tres()
        elif opcao == 4:
            menu_options.option_quatro()
        elif opcao == 5:
            res = input("Deseja realmente sair?")
            if res.upper() == "S":
                break

main()