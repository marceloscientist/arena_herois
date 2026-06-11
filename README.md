<div align="center">

# ⚔️ Arena dos Heróis

### Projeto de conclusão — UC Lógica de Programação

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-blue?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/Status-Pronto-green?style=for-the-badge)

</div>

---

## 📖 Sobre o Projeto

O **Arena dos Heróis** é o projeto de encerramento da UC de **Lógica de Programação**.

Em um único sistema, você vai ver na prática tudo que estudou durante o curso:

| Conceito | Onde aparece |
|---|---|
| 🧠 Lógica de Programação | Estrutura do `main.py`, condicionais, loops |
| 📦 Estrutura de Dados | Lista de heróis em memória |
| 🏛️ Orientação a Objetos | Classe `Heroi`, atributos, métodos |
| 📊 Big O Notation | `append O(1)`, busca `O(n)`, ranking `O(n log n)` |
| 🗂️ Modularização | Projeto dividido em múltiplos arquivos |

---

## 🖥️ Instalação — Passo a Passo (Windows)

### ✅ Pré-requisitos

Você vai precisar instalar **duas ferramentas** antes de rodar o projeto:

1. **Python 3.8+**
2. **Visual Studio Code**

---

### 🐍 PASSO 1 — Instalar o Python

**1.** Acesse o site oficial:
👉 [https://www.python.org/downloads](https://www.python.org/downloads)

**2.** Clique no botão **"Download Python 3.x.x"**

**3.** Execute o instalador baixado

> ⚠️ **ATENÇÃO — Passo obrigatório:**
> Na primeira tela do instalador, marque a opção:
> ```
> ✅ Add Python to PATH
> ```
> **Só depois clique em "Install Now"**

**4.** Verifique se funcionou — abra o **Prompt de Comando**:
> Pressione `Win + R`, digite `cmd` e pressione Enter

```cmd
python --version
```

Você deve ver algo como:
```
Python 3.12.0
```

---

### 💻 PASSO 2 — Instalar o VS Code

**1.** Acesse o site oficial:
👉 [https://code.visualstudio.com](https://code.visualstudio.com)

**2.** Clique em **"Download for Windows"**

**3.** Execute o instalador e marque estas opções:
```
✅ Adicionar ao PATH
✅ Registrar como editor padrão
✅ Adicionar "Abrir com Code" ao menu de contexto
```

---

### 🧩 PASSO 3 — Instalar a Extensão Python no VS Code

**1.** Abra o VS Code

**2.** Pressione `Ctrl + Shift + X`

**3.** Na barra de busca, digite: `Python`

**4.** Instale a extensão oficial da **Microsoft**

---

### 📥 PASSO 4 — Baixar o Projeto

**Opção A — Com Git instalado:**

Abra o terminal e execute:
```bash
git clone https://github.com/SEU_USUARIO/arena-herois.git
cd arena-herois
```

**Opção B — Download direto (sem Git):**

1. Clique no botão verde **`<> Code`** nesta página
2. Clique em **"Download ZIP"**
3. Extraia o arquivo ZIP em uma pasta de sua preferência

---

### ▶️ PASSO 5 — Abrir no VS Code

**1.** Abra o VS Code

**2.** Vá em `File → Open Folder`

**3.** Selecione a pasta `arena-herois`

---

### ⚙️ PASSO 6 — Selecionar o Interpretador Python

**1.** Pressione `Ctrl + Shift + P`

**2.** Digite: `Python: Select Interpreter`

**3.** Selecione a versão do Python instalada

---

### 🎮 PASSO 7 — Rodar o Projeto

Abra o terminal integrado do VS Code com `` Ctrl + ` `` e execute:

```bash
# Entrar na pasta do projeto
cd arena_herois

# Rodar o sistema completo
python main.py
```

Ou para rodar a **demo com heróis pré-carregados**:

```bash
python demo.py
```

---

## 🗂️ Estrutura do Projeto

```
arena_herois/
│
├── main.py        # Ponto de entrada — coordena tudo
├── heroi.py       # Classe Herói — OOP
├── menu.py        # Exibe o menu — separação de responsabilidades
├── sistema.py     # Toda a lógica — funções e algoritmos
└── demo.py        # Demo automática para testes
```

> 💡 **Por que separar em arquivos?**
> Projetos reais nunca ficam em um único arquivo.
> Cada arquivo tem **uma responsabilidade clara** — isso é arquitetura de software.

---

## 📊 Conceitos aplicados no projeto

### 🏛️ Orientação a Objetos

```python
class Heroi:
    def __init__(self, nome, nivel):
        self.nome   = nome
        self.nivel  = nivel
        self.vida   = nivel * 20
        self.ataque = nivel * 5

goku = Heroi("Goku", 10)   # instanciando um objeto
goku.apresentar()           # chamando um método
```

---

### 📦 Estrutura de Dados — Lista

```python
herois = []                  # lista vazia
herois.append(Heroi(...))    # inserção → O(1)
herois[0]                    # acesso direto → O(1)
```

---

### 🔍 Busca Linear

```python
for heroi in herois:
    if heroi.nome == nome:   # busca → O(n)
        return heroi
```

---

### 🏆 Ordenação

```python
sorted(herois, key=lambda h: h.nivel, reverse=True)  # O(n log n)
```

---

### 📊 Tabela Big O

| Operação | Código | Complexidade |
|---|---|---|
| Cadastrar | `append()` | **O(1)** |
| Acessar por índice | `herois[0]` | **O(1)** |
| Listar / Buscar | `for` + `if` | **O(n)** |
| Ranking | `sorted()` | **O(n log n)** |

---

## 🎮 Como usar o sistema

```
====================================
       ⚔  ARENA DOS HERÓIS  ⚔
====================================
  1 - Cadastrar Herói
  2 - Listar Heróis
  3 - Buscar Herói
  4 - Ranking
  5 - Batalhar
  6 - Sair
====================================
```

---

## 🏆 Desafio Final

Crie o arquivo `ranking.py` com a função abaixo e integre ao `main.py`:

```python
# ranking.py

def mostrar_top3(herois):
    """
    Exibe os 3 heróis mais poderosos.
    Pratique: sorted(), slicing, enumerate(), import
    """
    classificados = sorted(herois, key=lambda h: h.nivel, reverse=True)
    top3 = classificados[:3]

    print("\n--- 🥇 Top 3 Heróis ---")
    for posicao, heroi in enumerate(top3, start=1):
        print(f"  {posicao}º {heroi.nome} — Nível {heroi.nivel}")
```

**Conceitos praticados:**
- `sorted()` com `lambda`
- Slicing `[:3]`
- `enumerate()`
- Criação e importação de módulo

---

## 🎓 UC Lógica de Programação

Este projeto é o encerramento de uma jornada que passou por:

- ✅ Variáveis e tipos de dados
- ✅ Condicionais e loops
- ✅ Funções
- ✅ Listas e estruturas de dados
- ✅ Orientação a Objetos
- ✅ Busca e Ordenação
- ✅ Complexidade de algoritmos (Big O)
- ✅ Modularização e arquitetura de projetos

> *"Há algumas semanas você estava aprendendo o que era uma variável.*
> *Hoje você é capaz de organizar um projeto em múltiplos arquivos,*
> *criar classes, instanciar objetos, manipular listas, buscar, ordenar*
> *e analisar a complexidade dos seus algoritmos."*

---

## ▶️ Próximos Passos

Agora que você domina os fundamentos, os próximos desafios são:

- 🔷 **Banco de Dados** — persistir seus heróis com SQLite ou PostgreSQL
- 🔷 **APIs REST** — expor seu sistema via HTTP com Flask ou FastAPI
- 🔷 **Frontend** — criar uma interface visual com HTML, CSS e JavaScript
- 🔷 **Git avançado** — branches, pull requests e colaboração em equipe
- 🔷 **Testes automatizados** — garantir que seu código nunca quebre

---

<div align="center">

Feito com ❤️ para a turma de Lógica de Programação

⭐ Se este projeto te ajudou, deixa uma estrela no repositório!

</div>
