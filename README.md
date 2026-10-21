# catsay 🐱 [![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A cute ASCII cat library that says, warns, thinks, and asks questions. Perfect for making your CLI output more fun and expressive!

## 📝 Description

**catsay** is a tiny Python library that renders an ASCII cat with messages. It provides several functions for different use cases:

- 🗣️ `say` — The cat says text with a given mood
- ⚠️ `warn` — The cat outputs a warning
- ❌ `error` — The cat shows an error message
- 💭 `think` — The cat thinks thoughtfully
- ❓ `ask` — The cat asks a question and returns the user's answer

### Features:

- 🎭 **4 moods** — happy, sleepy, angry, love
- 📦 **Zero dependencies** — Pure Python, no extra packages
- 🔌 **Simple API** — 5 functions for all use cases
- 🎨 **ASCII art** — No external images or assets needed
- 💬 **Interactive** — `ask()` reads user input

## ⚙️ Installation

### Option 1: Install from PyPI

```bash
pip install catsay-py
```

### Option 2: Copy the file

Just copy `catsay.py` into your project:

```bash
# Place catsay.py in your project directory
```

### Option 3: Install from Git

```bash
git clone https://github.com/FelineFantasy/catsay
cd catsay
pip install .
```

## 🚀 Usage

### Basic

```python
from catsay import say, warn, error, think, ask

say("Hello, World!")
warn("Don't forget to feed the cat!")
error("Something went wrong!")
think("Hmm, interesting...")
answer = ask("What's your name?")
print(f"User said: {answer}")
```

### Moods

```python
say("I'm happy!", mood="happy")
say("Zzz...", mood="sleepy")
say("I'm angry!", mood="angry")
say("I love you!", mood="love")
```

### Without text

```python
say()  # Just a cute cat
think()  # Thinking cat
warn()  # Warning cat
error()  # Error cat
```

## 📖 API Reference

### `say(text: str = "", mood: str = "happy") -> None`

The cat says text with a given mood.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `""` | Text to display |
| `mood` | `str` | `"happy"` | Cat mood: `happy`, `sleepy`, `angry`, `love` |

**Raises:** `ValueError` if mood is not supported

**Example:**

```python
say("Meow!")
#    /\_/\
#   ( o.o )  >  Meow!
#    > ^ <
```

---

### `warn(text: str = "") -> None`

The cat outputs a warning.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `""` | Warning message |

**Example:**

```python
warn("Low disk space!")
#    /\_/\
#   ( -.o )  ~  Low disk space! ~~~
#    > ^ <
```

---

### `error(text: str = "Error") -> None`

The cat outputs an error message (uses angry mood).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `"Error"` | Error message |

**Example:**

```python
error("File not found!")
#    /\_/\
#   ( ò.ó )  >  !!! File not found! !!!
#    > ^ <
```

---

### `think(text: str = "", mood: str = "happy") -> None`

The cat says text thoughtfully (with `<` bubble).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `""` | Text to think about |
| `mood` | `str` | `"happy"` | Cat mood |

**Raises:** `ValueError` if mood is not supported

**Example:**

```python
think("Hmm, interesting...")
#    /\_/\
#   ( o.o )  <  Hmm, interesting...
#    > ^ <
```

---

### `ask(question: str = "") -> str`

The cat asks a question and returns the user's answer.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `question` | `str` | `""` | Question to ask |

**Returns:** `str` — User's input

**Example:**

```python
name = ask("What's your name?")
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
from catsay import say, warn, error, think, ask

print("=== say() ===\n")
say()
say("Meow!", mood="happy")
say("Zzz", mood="sleepy")
say("meow :(", mood="angry")
say("I love you!", mood="love")

print("\n=== warn() ===\n")
warn()
warn("Where's my food!")

print("\n=== error() ===\n")
error()
error("The cat has fallen!")

print("\n=== think() ===\n")
think()
think("Hmm", mood="happy")
think("Hmm", mood="sleepy")
think("Hmm", mood="angry")
think("Hmm", mood="love")

print("\n=== ask() ===\n")
ask()
ask("Where's my food?")
```

## 🧪 Testing

Run the test suite with the standard library `unittest`:

```bash
python -m unittest discover -s tests -v
```

Tests also run automatically on every push and pull request via GitHub Actions.

## 📁 Project Structure

```text
catsay/
├── .github/
│   ├── FUNDING.yml           # Support link for DonationAlerts
│   └── workflows/
│       └── tests.yml         # CI workflow for running tests
├── catsay.py                 # Main library
├── README.md                 # Documentation
├── LICENSE                   # MIT License
├── pyproject.toml            # Package configuration
├── tests/
│   └── test_catsay.py        # Unit tests
└── .gitignore                # Git ignore rules
```

## 🛠 Technologies

- **Python 3.8+** — Pure standard library, no external dependencies

## 📋 Requirements

- Python 3.8+
- No external dependencies

## 💖 Support the Project

If you enjoy **catsay** and want to help keep the project alive, you can support me here:

[![DonationAlerts](https://img.shields.io/badge/DonationAlerts-Support-blue.svg)](https://www.donationalerts.com/r/felinefantasy)

Your support helps me:
- 🐱 Keep developing cute tools
- 🛠️ Add more moods and features
- ☕ Stay awake while coding at 4 AM

Every little bit is appreciated! ❤️

## 👤 Author
- **FelineFantasy**
- **License**: MIT
