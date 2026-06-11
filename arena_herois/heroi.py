# ============================================================
#  HEROI.PY — Define a estrutura de um Herói
#  Conceito: Classe, Objeto, Atributos, Métodos
# ============================================================

class Heroi:

    def __init__(self, nome, nivel):
        self.nome   = nome
        self.nivel  = nivel
        self.vida   = nivel * 20       # Vida proporcional ao nível
        self.ataque = nivel * 5        # Ataque proporcional ao nível

    def apresentar(self):
        print(f"  ⚔  {self.nome:<12} | Nível: {self.nivel:>2} | Vida: {self.vida:>4} | Ataque: {self.ataque:>3}")

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def atacar(self, alvo):
        print(f"\n  💥 {self.nome} atacou {alvo.nome}!")
        alvo.receber_dano(self.ataque)
        print(f"     {alvo.nome} recebeu {self.ataque} de dano. Vida restante: {alvo.vida}")
