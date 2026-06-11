# ============================================================
#  DEMO.PY — Popula o sistema automaticamente para demonstração
#  Execute ANTES da aula para não perder tempo digitando
# ============================================================

from heroi import Heroi
import main  # importa o ponto de entrada real

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


if __name__ == "__main__":
    herois = popular()
    main.main(herois)   # passa os heróis pré-carregados
