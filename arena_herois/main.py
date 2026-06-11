# ============================================================
#  MAIN.PY — Ponto de entrada do programa
#  Conceito: Modularização, loop principal, controle de fluxo
# ============================================================

import menu as menu # importa o menu para mostrar as opções para o usuário
import sistema as sistema # importa as funções do sistema para usar aqui no main

def main(herois=None):       # ← recebe do demo, ou cria vazia
    if herois is None:
        herois = []

    while True:
        menu.mostrar()
        opcao = input("\n  Escolha uma opção: ").strip()

        if opcao == "1":
            sistema.cadastrar(herois)

        elif opcao == "2":
            sistema.listar(herois)

        elif opcao == "3":
            sistema.buscar(herois)

        elif opcao == "4":
            sistema.ranking(herois)

        elif opcao == "5":
            sistema.batalhar(herois)

        elif opcao == "6":
            print("\n  👋 Até a próxima, professor!\n")
            break

        else:
            print("\n  ⚠  Opção inválida. Tente novamente.")

        input("\n  [ Enter para continuar ]")


if __name__ == "__main__":
    main()
