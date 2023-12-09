import unittest

from main import part_one, part_two


class TestDay3(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one("./test_input.txt"), 2)
        self.assertEqual(part_one("./input.txt"), 562)

    def test_part_two(self):
        self.assertEqual(part_two("./test_input.txt"), 4)


if __name__ == "__main__":
    unittest.main()
