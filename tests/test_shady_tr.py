import unittest
import data
from shady_tr import ShadyTextRandomizer


class ShadyTextRandomizerTest(unittest.TestCase):
    """Test ``shady_tr.shady_text_randomizer``."""

    def setUp(self):
        """Set up."""
        self.latin_text = data.latin_text
        self.cyrillic_text = data.cyrillic_text

    def test_01_randomize_cyrillic_chance_100(self):
        """Test randomize cyrillic text."""
        text_rnd = ShadyTextRandomizer(self.cyrillic_text, 100)
        result = text_rnd.random_cyrillic()
        self.assertNotEqual(result, self.cyrillic_text)
        return result

    def test_02_randomize_cyrillic_chance_0(self):
        """Test randomize cyrillic text."""
        text_rnd = ShadyTextRandomizer(self.cyrillic_text, 0)
        result = text_rnd.random_cyrillic()
        self.assertEqual(result, self.cyrillic_text)
        return result

    def test_03_randomize_latin_chance_100(self):
        """Test randomize cyrillic text."""
        text_rnd = ShadyTextRandomizer(self.latin_text, 100)
        result = text_rnd.random_latin()
        self.assertNotEqual(result, self.latin_text)
        return result

    def test_04_randomize_latin_chance_0(self):
        """Test randomize cyrillic text."""
        text_rnd = ShadyTextRandomizer(self.latin_text, 0)
        result = text_rnd.random_latin()
        self.assertEqual(result, self.latin_text)
        return result
