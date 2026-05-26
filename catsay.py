# catsay.py
__all__ = ["cat_say", "cat_warn", "cat_error", "cat_think", "cat_ask"]

FACES = {
    "happy": "o.o",
    "sleepy": "-.-",
    "angry": "ò.ó",
    "love": "^.^",
}


def cat_say(text: str = "", mood: str = "happy") -> None:
    """The cat says text with a given mood (happy/sleepy/angry/love)."""
    if mood not in FACES:
        raise ValueError(f"Unsupported mood: {mood}. Available: {list(FACES.keys())}")

    face = FACES[mood]

    cat = rf"""   /\_/\
  ( {face} )  >  {text}
   > ^ <""" if text else rf"""   /\_/\
  ( {face} )
   > ^ <"""
    print(cat)


def cat_warn(text: str = "") -> None:
    """The cat outputs a warning."""
    cat = rf"""   /\_/\
  ( -.o )  ~  {text} ~~~
   > ^ <"""
    print(cat)


def cat_error(text: str = "Error") -> None:
    """The cat outputs an error message."""
    cat_say(f"!!! {text} !!!", mood="angry")


def cat_think(text: str = "", mood: str = "happy") -> None:
    """The cat says text thoughtfully."""
    if mood not in FACES:
        raise ValueError(f"Unsupported mood: {mood}. Available: {list(FACES.keys())}")

    face = FACES[mood]
    cat = rf"""   /\_/\
  ( {face} )  <  {text}...
   > ^ <"""
    print(cat)


def cat_ask(question: str = "") -> str:
    """The cat asks a question and returns the user's answer."""
    cat_say(question, mood="love")
    return input("> ")


if __name__ == "__main__":
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
