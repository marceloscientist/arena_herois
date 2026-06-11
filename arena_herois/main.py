# ============================================================
#  MAIN.PY — Ponto de entrada do programa
#  Conceito: Modularização, loop principal, controle de fluxo
# ============================================================

import menu as menu
import sistema as sistema

def main():
    herois = []   # Lista em memória — estrutura de dados central

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
