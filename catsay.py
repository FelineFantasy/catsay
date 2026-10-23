#!/usr/bin/env python3

"""
Catsay - ASCII cat with customizable moods and messages
"""

# catsay.py
__all__ = ["say", "warn", "error", "think", "ask"]

FACES = {
    "happy": "o.o",
    "sleepy": "-.-",
    "angry": ">.<",
    "love": "^.^",
}


def _get_face(mood: str) -> str:
    """Return the face for a mood, raising ValueError if it is unknown."""
    if mood not in FACES:
        raise ValueError(f"Unsupported mood: {mood}. Available: {list(FACES.keys())}")
    return FACES[mood]


def _cat(face: str, message: str = "") -> str:
    """Return a three-line cat frame with an optional message beside the face."""
    middle = f"  ( {face} )"
    if message:
        middle += f"  {message}"
    return f"   /\\_/\\\n{middle}\n   > ^ <"


def say(text: str = "", mood: str = "happy") -> None:
    """The cat says text with a given mood (happy/sleepy/angry/love).

    Multi-line text is aligned under the first message line.
    """
    face = _get_face(mood)
    if not text:
        print(_cat(face))
        return
    indent = " " * len(f"  ( {face} )  >  ")
    message = ">  " + f"\n{indent}".join(text.splitlines() or [text])
    print(_cat(face, message))


def warn(text: str = "") -> None:
    """The cat outputs a warning."""
    print(_cat("-.o", f"~  {text} ~~~"))


def error(text: str = "Error") -> None:
    """The cat outputs an error message."""
    say(f"!!! {text} !!!", mood="angry")


def think(text: str = "", mood: str = "happy") -> None:
    """The cat says text thoughtfully."""
    face = _get_face(mood)
    print(_cat(face, f"<  {text}..." if text else "<"))


def ask(question: str = "") -> str:
    """The cat asks a question and returns the user's answer."""
    say(question, mood="love")
    return input("> ")


if __name__ == "__main__":
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
