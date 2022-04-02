import random
from .mapping import DICT_CYRILLIC
from .mapping import DICT_LATIN


class ShadyTextRandomizer:
    src_text = None
    chance = None

    def __init__(self, text, chance):
        self.src_text = list(text)
        self.chance = chance

    def random_cyrillic(self):
        return self.__randomize(DICT_CYRILLIC)

    def random_latin(self):
        return self.__randomize(DICT_LATIN)

    def __randomize(self, dictionary):
        text = self.src_text[:]
        i = 0
        for s in text:
            if s in dictionary:
                if random.randrange(1, 100) <= self.chance:
                    text[i] = random.choice(dictionary[s])
            i += 1
        return ''.join(text)
