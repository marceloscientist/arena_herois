# ============================================================
#  SISTEMA.PY — Toda a lógica do sistema
#  Conceito: Funções, Listas, Busca, Ordenação, Big O
# ============================================================

from arena_herois.heroi import Heroi


# ----------------------------------------------------------
#  CADASTRAR
#  Complexidade: O(1) — append no final da lista
# ----------------------------------------------------------
def cadastrar(herois):
    print("\n--- Cadastrar Herói ---")
    nome  = input("  Nome   : ").strip()
    nivel = int(input("  Nível  : ").strip())

    herois.append(Heroi(nome, nivel))

    print(f"\n  ✅ {nome} cadastrado com sucesso!")


# ----------------------------------------------------------
#  LISTAR
#  Complexidade: O(n) — percorre toda a lista
# ----------------------------------------------------------
def listar(herois):
    print("\n--- Lista de Heróis ---")

    if not herois:
        print("  Nenhum herói cadastrado.")
        return

    for heroi in herois:
        heroi.apresentar()


# ----------------------------------------------------------
#  BUSCAR
#  Complexidade: O(n) — busca linear
# ----------------------------------------------------------
def buscar(herois):
    print("\n--- Buscar Herói ---")
    nome = input("  Nome: ").strip()

    for heroi in herois:
        if heroi.nome.lower() == nome.lower():
            print("\n  ✅ Herói encontrado:")
            heroi.apresentar()
            return

    print(f"\n  ❌ Herói '{nome}' não encontrado.")


# ----------------------------------------------------------
#  RANKING
#  Complexidade: O(n log n) — algoritmo Timsort do Python
# ----------------------------------------------------------
def ranking(herois):
    print("\n--- 🏆 Ranking por Nível ---")

    if not herois:
        print("  Nenhum herói cadastrado.")
        return

    classificados = sorted(herois, key=lambda h: h.nivel, reverse=True)

    for posicao, heroi in enumerate(classificados, start=1):
        print(f"  {posicao}º  {heroi.nome:<12} | Nível: {heroi.nivel}")


# ----------------------------------------------------------
#  BATALHAR
#  Conceito: Objetos interagindo entre si
# ----------------------------------------------------------
def batalhar(herois):
    print("\n--- ⚔ Batalha ---")

    if len(herois) < 2:
        print("  Você precisa de pelo menos 2 heróis cadastrados.")
        return

    print("\n  Heróis disponíveis:")
    for i, heroi in enumerate(herois):
        print(f"  {i} - {heroi.nome}")

    try:
        idx_a = int(input("\n  Escolha o atacante (número): "))
        idx_b = int(input("  Escolha o alvo     (número): "))

        atacante = herois[idx_a]
        alvo     = herois[idx_b]

        atacante.atacar(alvo)

        if not alvo.esta_vivo():
            print(f"\n  💀 {alvo.nome} foi derrotado!")

    except (IndexError, ValueError):
        print("\n  ❌ Seleção inválida.")
