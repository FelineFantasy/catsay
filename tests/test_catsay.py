import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import catsay


def capture(func, *args, **kwargs):
    output = io.StringIO()
    with redirect_stdout(output):
        func(*args, **kwargs)
    return output.getvalue()


class CatSayTests(unittest.TestCase):
    def test_default_cat(self):
        self.assertEqual(capture(catsay.say), "   /\\_/\\\n  ( o.o )\n   > ^ <\n")

    def test_text_and_mood(self):
        self.assertEqual(
            capture(catsay.say, "Meow!", mood="sleepy"),
            "   /\\_/\\\n  ( -.- )  >  Meow!\n   > ^ <\n",
        )

    def test_all_moods_render_their_face(self):
        for mood, face in catsay.FACES.items():
            self.assertIn(f"( {face} )", capture(catsay.say, "hi", mood=mood))

    def test_unknown_mood_raises(self):
        with self.assertRaises(ValueError):
            capture(catsay.say, "hi", mood="grumpy")

    def test_multi_line_text_is_aligned(self):
        self.assertEqual(
            capture(catsay.say, "first\nsecond"),
            "   /\\_/\\\n"
            "  ( o.o )  >  first\n"
            "              second\n"
            "   > ^ <\n",
        )

    def test_trailing_newline_does_not_add_blank_line(self):
        self.assertEqual(
            capture(catsay.say, "only\n"),
            "   /\\_/\\\n  ( o.o )  >  only\n   > ^ <\n",
        )


class CatWarnTests(unittest.TestCase):
    def test_empty_warning(self):
        self.assertEqual(capture(catsay.warn), "   /\\_/\\\n  ( -.o )  ~   ~~~\n   > ^ <\n")

    def test_warning_with_text(self):
        self.assertEqual(
            capture(catsay.warn, "Low disk space!"),
            "   /\\_/\\\n  ( -.o )  ~  Low disk space! ~~~\n   > ^ <\n",
        )


class CatErrorTests(unittest.TestCase):
    def test_default_error(self):
        self.assertEqual(
            capture(catsay.error),
            "   /\\_/\\\n  ( >.< )  >  !!! Error !!!\n   > ^ <\n",
        )

    def test_custom_error(self):
        self.assertIn("!!! File not found! !!!", capture(catsay.error, "File not found!"))


class CatThinkTests(unittest.TestCase):
    def test_empty_thought_has_no_ellipsis(self):
        self.assertEqual(capture(catsay.think), "   /\\_/\\\n  ( o.o )  <\n   > ^ <\n")

    def test_thought_with_text(self):
        self.assertEqual(
            capture(catsay.think, "Hmm", mood="love"),
            "   /\\_/\\\n  ( ^.^ )  <  Hmm...\n   > ^ <\n",
        )

    def test_unknown_mood_raises(self):
        with self.assertRaises(ValueError):
            capture(catsay.think, "Hmm", mood="grumpy")

    def test_multi_line_thought_is_aligned(self):
        self.assertEqual(
            capture(catsay.think, "line one\nline two", mood="love"),
            "   /\\_/\\\n"
            "  ( ^.^ )  <  line one\n"
            "              line two...\n"
            "   > ^ <\n",
        )


class CatAskTests(unittest.TestCase):
    def test_returns_user_answer(self):
        output = io.StringIO()
        with patch("builtins.input", return_value="fish") as mock_input:
            with redirect_stdout(output):
                answer = catsay.ask("What's for dinner?")
        self.assertEqual(answer, "fish")
        self.assertIn("What's for dinner?", output.getvalue())
        mock_input.assert_called_once_with("> ")


if __name__ == "__main__":
    unittest.main()
