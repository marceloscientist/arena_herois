<div align="center">

🇧🇷 [Leia em Português](./README.pt-BR.md) | 🇺🇸 English

# ⚔️ Heroes Arena

### Capstone Project — Programming Logic Course

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-blue?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/Status-Ready-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## 📖 About

**Heroes Arena** is the capstone project for the **Programming Logic** course.

In a single system, you will see in practice everything studied throughout the course:

| Concept | Where it appears |
|---|---|
| 🧠 Programming Logic | `main.py` structure, conditionals, loops |
| 📦 Data Structures | In-memory hero list |
| 🏛️ Object-Oriented Programming | `Hero` class, attributes, methods |
| 📊 Big O Notation | `append O(1)`, search `O(n)`, ranking `O(n log n)` |
| 🗂️ Modularization | Project split across multiple files |

---

## 🖥️ Installation — Step by Step (Windows)

### ✅ Prerequisites

You will need to install **two tools** before running the project:

1. **Python 3.8+**
2. **Visual Studio Code**

---

### 🐍 STEP 1 — Install Python

**1.** Go to the official website:
👉 [https://www.python.org/downloads](https://www.python.org/downloads)

**2.** Click **"Download Python 3.x.x"**

**3.** Run the downloaded installer

> ⚠️ **IMPORTANT — Required step:**
> On the first screen of the installer, check:
> ```
> ✅ Add Python to PATH
> ```
> **Then click "Install Now"**

**4.** Verify the installation — open the **Command Prompt**:
> Press `Win + R`, type `cmd` and press Enter

```cmd
python --version
```

Expected output:
```
Python 3.12.0
```

---

### 💻 STEP 2 — Install VS Code

**1.** Go to the official website:
👉 [https://code.visualstudio.com](https://code.visualstudio.com)

**2.** Click **"Download for Windows"**

**3.** Run the installer and check:
```
✅ Add to PATH
✅ Register as default editor
✅ Add "Open with Code" to context menu
```

---

### 🧩 STEP 3 — Install the Python Extension

**1.** Open VS Code

**2.** Press `Ctrl + Shift + X`

**3.** Search for: `Python`

**4.** Install the official **Microsoft** extension

---

### 📥 STEP 4 — Download the Project

**Option A — With Git:**

```bash
git clone https://github.com/YOUR_USERNAME/arena-herois.git
cd arena-herois
```

**Option B — Direct download (no Git required):**

1. Click the green **`<> Code`** button on this page
2. Click **"Download ZIP"**
3. Extract the ZIP to a folder of your choice

---

### ▶️ STEP 5 — Run the Project

Open the VS Code integrated terminal with `` Ctrl + ` `` and run:

```bash
cd arena_herois

# Full system
python main.py

# Automated demo with pre-loaded heroes
python demo.py
```

---

## 🗂️ Project Structure

```
arena_herois/
│
├── main.py        # Entry point — orchestrates everything
├── heroi.py       # Hero class — OOP
├── menu.py        # Displays the menu — separation of concerns
├── sistema.py     # All logic — functions and algorithms
└── demo.py        # Automated demo for testing
```

---

## 📊 Core Concepts Applied

### 🏛️ Object-Oriented Programming

```python
class Heroi:
    def __init__(self, nome, nivel):
        self.nome   = nome
        self.nivel  = nivel
        self.vida   = nivel * 20
        self.ataque = nivel * 5

goku = Heroi("Goku", 10)   # instantiating an object
goku.apresentar()           # calling a method
```

### 📦 Data Structure — List

```python
herois = []                  # empty list
herois.append(Heroi(...))    # insert → O(1)
herois[0]                    # direct access → O(1)
```

### 🔍 Linear Search

```python
for heroi in herois:
    if heroi.nome == nome:   # search → O(n)
        return heroi
```

### 🏆 Sorting

```python
sorted(herois, key=lambda h: h.nivel, reverse=True)  # O(n log n)
```

---

## 📊 Big O Summary

| Operation | Code | Complexity |
|---|---|---|
| Register | `append()` | **O(1)** |
| Access by index | `herois[0]` | **O(1)** |
| List / Search | `for` + `if` | **O(n)** |
| Ranking | `sorted()` | **O(n log n)** |

---

## 🏆 Final Challenge

Create `ranking.py` and integrate it into `main.py`:

```python
def mostrar_top3(herois):
    classificados = sorted(herois, key=lambda h: h.nivel, reverse=True)
    top3 = classificados[:3]

    print("\n--- 🥇 Top 3 Heroes ---")
    for posicao, heroi in enumerate(top3, start=1):
        print(f"  {posicao}. {heroi.nome} — Level {heroi.nivel}")
```

**Concepts practiced:** `sorted()` with `lambda`, list slicing `[:3]`, `enumerate()`, module import.

---

## 🎓 What You Learned

- ✅ Variables and data types
- ✅ Conditionals and loops
- ✅ Functions
- ✅ Lists and data structures
- ✅ Object-Oriented Programming
- ✅ Search and sorting algorithms
- ✅ Algorithm complexity (Big O)
- ✅ Modularization and project architecture

---

## 🚀 What Comes Next

| Topic | Technologies |
|---|---|
| 🔷 Databases | SQLite, PostgreSQL |
| 🔷 REST APIs | Flask, FastAPI |
| 🔷 Frontend | HTML, CSS, JavaScript |
| 🔷 Advanced Git | Branches, Pull Requests |
| 🔷 Automated Tests | unittest, pytest |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

Made with ❤️ for the Programming Logic class

⭐ If this project helped you, give it a star!

</div>
