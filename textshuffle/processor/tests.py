from django.test import SimpleTestCase
import re

from . import utils


class UtilsTests(SimpleTestCase):
    def test_shuffle_word_short_words_unchanged(self):
        for w in ("a", "ab", "cat", "hi", "abc"):
            self.assertEqual(utils.shuffle_word(w), w)

    def test_shuffle_word_preserves_first_last_and_middle_permutation(self):
        w = "example"
        res = utils.shuffle_word(w)
        self.assertEqual(res[0], w[0])
        self.assertEqual(res[-1], w[-1])
        self.assertEqual(len(res), len(w))
        # middle letters are a permutation
        self.assertCountEqual(res[1:-1], w[1:-1])

    def test_shuffle_text_properties_and_punctuation_preserved(self):
        text = "Hello, world! This is a test: Python3."
        res = utils.shuffle_text(text)

        words_orig = re.findall(r"\b\w+\b", text)
        words_res = re.findall(r"\b\w+\b", res)
        self.assertEqual(len(words_orig), len(words_res))

        for o, r in zip(words_orig, words_res):
            if len(o) <= 3:
                self.assertEqual(o, r)
            else:
                self.assertEqual(o[0], r[0])
                self.assertEqual(o[-1], r[-1])
                self.assertCountEqual(o[1:-1], r[1:-1])

        # separators (punctuation/whitespace) in same places
        non_words_orig = re.split(r"\w+", text)
        non_words_res = re.split(r"\w+", res)
        self.assertEqual(non_words_orig, non_words_res)
