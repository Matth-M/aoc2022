import unittest

from main import letter_priority, part_one, part_two


class TestDay3(unittest.TestCase):
    def test_single_backpack(self):
        self.assertEqual(part_one("./test_input.txt"), 157)

    def test_letter_priority(self):
        self.assertEqual(letter_priority("p"), 16)
        self.assertEqual(letter_priority("L"), 38)
        self.assertEqual(letter_priority("P"), 42)
        self.assertEqual(letter_priority("v"), 22)
        self.assertEqual(letter_priority("t"), 20)
        self.assertEqual(letter_priority("s"), 19)

    def test_part_two(self):
        self.assertEqual(part_two("./test_input.txt"), 70)


if __name__ == "__main__":
    unittest.main()
