# ============================================================
#  DEMO.PY — Popula o sistema automaticamente para demonstração
#  Execute ANTES da aula para não perder tempo digitando
# ============================================================

from heroi import Heroi
import sistema
import menu

def popular():
    """Cria 5 heróis automaticamente"""
    herois = [
        Heroi("Goku",   10),
        Heroi("Vegeta",  8),
        Heroi("Gohan",   6),
        Heroi("Piccolo", 7),
        Heroi("Trunk",   5),
    ]
    print("\n  ✅ 5 heróis carregados automaticamente!\n")
    return herois


def main():
    herois = popular()

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
            print("\n  👋 Até a próxima!\n")
            break
        else:
            print("\n  ⚠  Opção inválida.")

        input("\n  [ Enter para continuar ]")


if __name__ == "__main__":
    main()
