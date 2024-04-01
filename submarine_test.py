import unittest

from submarine import Submarine


class SubmarineTest(unittest.TestCase):
    def test_submarine_creates_initial_state(self):
        submarine = Submarine()
        self.assertEqual(0, submarine.distance)
        self.assertEqual(0, submarine.depth)

    def test_submarine_handles_forward_navigation(self):
        submarine = Submarine()
        submarine.navigate("forward 5")
        self.assertEqual(5, submarine.distance)

    def test_submarine_handles_rotation(self):
        submarine = Submarine()
        submarine.navigate("down 3")
        submarine.navigate("forward 5")
        self.assertEqual(5, submarine.distance)
        self.assertEqual(15, submarine.depth)


if __name__ == '__main__':
    unittest.main()
