import random
import re


def shuffle_word(word):
    if len(word) <= 3:
        return word
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + "".join(middle) + word[-1]


def shuffle_text(text):
    def repl(match):
        return shuffle_word(match.group(0))

    return re.sub(r"\b\w+\b", repl, text)
