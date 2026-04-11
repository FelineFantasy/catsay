# catsay 🐱 [![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A cute ASCII cat library that says, warns, thinks, and asks questions. Perfect for making your CLI output more fun and expressive!

## 📋 Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Moods](#moods)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Author](#author)

## 📝 Description

**catsay** is a tiny Python library that renders an ASCII cat with messages. It provides several functions for different use cases:

- 🗣️ `cat_say` — The cat says text with a given mood
- ⚠️ `cat_warn` — The cat outputs a warning
- ❌ `cat_error` — The cat shows an error message
- 💭 `cat_think` — The cat thinks thoughtfully
- ❓ `cat_ask` — The cat asks a question and returns the user's answer

### Features:

- 🎭 **4 moods** — happy, sleepy,angry,love
- 📦 **Zero dependencies** — Pure Python, no extra packages
- 🔌 **Simple API** — 5 functions for all use cases
- 🎨 **ASCII art** — No external images or assets needed
- 💬 **Interactive** — `cat_ask()` reads user input

## ⚙️ Installation

### Option 1: Copy the file

Just copy `catsay.py` into your project:

```bash
# Place catsay.py in your project directory
```

### Option 2: Install from Git

```bash
git clone https://github.com/FelineFantasy/catsay.git
cd catsay
```

## 🚀 Usage

### Basic

```python
from catsay import cat_say, cat_warn, cat_error, cat_think, cat_ask

cat_say("Hello, World!")
cat_warn("Don't forget to feed the cat!")
cat_error("Something went wrong!")
cat_think("Hmm, interesting...")
answer = cat_ask("What's your name?")
print(f"User said: {answer}")
```

### Moods

```python
cat_say("I'm happy!", mood="happy")
cat_say("Zzz...", mood="sleepy")
cat_say("I'm angry!", mood="angry")
cat_say("I love you!", mood="love")
```

### Without text

```python
cat_say()  # Just a cute cat
cat_think()  # Thinking cat
cat_warn()  # Warning cat
cat_error()  # Error cat
```

## 📖 API Reference

### `cat_say(text: str = "", mood: str = "happy") -> None`

The cat says text with a given mood.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `""` | Text to display |
| `mood` | `str` | `"happy"` | Cat mood: `happy`, `sleepy`, `angry`, `love` |

**Raises:** `ValueError` if mood is not supported

**Example:**

```python
cat_say("Meow!")
#    /\_/\
#   ( o.o )  >  Meow!
#    > ^ <
```

---

### `cat_warn(text: str = "") -> None`

The cat outputs a warning.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `""` | Warning message |

**Example:**

```python
cat_warn("Low disk space!")
#    /\_/\
#   ( -.o )  ~  Low disk space! ~~~
#    > ^ <
```

---

### `cat_error(text: str = "Error") -> None`

The cat outputs an error message (uses angry mood).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `"Error"` | Error message |

**Example:**

```python
cat_error("File not found!")
#    /\_/\
#   ( ò.ó )  >  !!! File not found! !!!
#    > ^ <
```

---

### `cat_think(text: str = "", mood: str = "happy") -> None`

The cat says text thoughtfully (with `<` bubble).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `""` | Text to think about |
| `mood` | `str` | `"happy"` | Cat mood |

**Raises:** `ValueError` if mood is not supported

**Example:**

```python
cat_think("Hmm, interesting...")
#    /\_/\
#   ( o.o )  <  Hmm, interesting...
#    > ^ <
```

---

### `cat_ask(question: str = "") -> str`

The cat asks a question and returns the user's answer.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `question` | `str` | `""` | Question to ask |

**Returns:** `str` — User's input

**Example:**

```python
name = cat_ask("What's your name?")
print(f"Hello, {name}!")
```

## 🎭 Moods

| Mood | Face | Description |
|------|------|-------------|
| `happy` | `o.o` | Default, friendly cat |
| `sleepy` | `-.-` | Tired, drowsy cat |
| `angry` | `ò.ó` | Angry, frustrated cat |
| `love` | `^.^` | Loving, affectionate cat |

## 🧪 Full Example

```python
from catsay import cat_say, cat_warn, cat_error, cat_think, cat_ask

print("=== cat_say() ===\n")
cat_say()
cat_say("Meow!", mood="happy")
cat_say("Zzz", mood="sleepy")
cat_say("meow :(", mood="angry")
cat_say("I love you!", mood="love")

print("\n=== cat_warn() ===\n")
cat_warn()
cat_warn("Where's my food!")

print("\n=== cat_error() ===\n")
cat_error()
cat_error("The cat has fallen!")

print("\n=== cat_think() ===\n")
cat_think()
cat_think("Hmm", mood="happy")
cat_think("Hmm", mood="sleepy")
cat_think("Hmm", mood="angry")
cat_think("Hmm", mood="love")

print("\n=== cat_ask() ===\n")
cat_ask()
cat_ask("Where's my food?")
```

## 📁 Project Structure

```
catsay/
├── catsay.py      # Main library
└── README.md      # This file
```

## 🛠 Technologies

- **Python 3.6+** — Pure standard library, no external dependencies

## 📋 Requirements

- Python 3.6+
- No external dependencies

## 👤 Author

**FelineFantasy**

License: MIT

## 🔗 Links

- **GitHub**: https://github.com/FelineFantasy/catsay
- **Other Projects**:
  - [CatFactsAPI](https://github.com/FelineFantasy/CatFactsAPI) — REST API for cat facts
  - [Digital Cat](https://github.com/FelineFantasy/Digital_Cat) — Virtual pet game
  - [ask_input](https://github.com/FelineFantasy/ask_input) — Rust input library
  - [paw-calculator](https://github.com/FelineFantasy/paw-calculator) — Rust calculator with cat theme

---

Made with ❤️ for cat lovers
