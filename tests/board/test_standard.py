import unittest
from chess.boards.standard import StandardBoard


class TestStandardBoard(unittest.TestCase):

    def setUp(self):
        self.board = StandardBoard()

    def test_valid_notation(self):
        valid_notations = ["A1", "H8", "D4", "E5"]
        for notation in valid_notations:
            self.assertTrue(self.board.is_valid_notation(notation))

    def test_invalid_notation(self):
        invalid_notations = ["Z1", "A9", "AA", "11", "A", "1", ""]
        for notation in invalid_notations:
            self.assertFalse(self.board.is_valid_notation(notation))

    def test_valid_cell_coordinates(self):
        valid_coords = [(0, 0), (7, 7), (3, 4), (6, 1)]
        for coords in valid_coords:
            self.assertTrue(self.board.is_valid_cell_coordinates(coords))

    def test_invalid_cell_coordinates(self):
        invalid_coords = [(-1, 0), (8, 0), (0, -1), (0, 8), (8, 8), (-1, -1)]
        for coords in invalid_coords:
            self.assertFalse(self.board.is_valid_cell_coordinates(coords))

    def test_valid_notation_to_cell_coordinates(self):
        test_cases = [("A1", (0, 0)), ("H8", (7, 7)), ("D4", (3, 3)), ("E5", (4, 4))]
        for notation, expected_coords in test_cases:
            result = self.board.notation_to_cell_coordinates(notation)
            self.assertEqual(result, expected_coords)

    def test_invalid_notation_to_cell_coordinates(self):
        invalid_notations = ["Z1", "A9", "I1", "H9", "AA", "11"]
        for notation in invalid_notations:
            self.assertRaises(
                ValueError, self.board.notation_to_cell_coordinates, notation
            )

    def test_valid_cell_coordinates_to_notation(self):
        test_cases = [((0, 0), "A1"), ((7, 7), "H8"), ((3, 3), "D4"), ((4, 4), "E5")]
        for coords, expected_notation in test_cases:
            result = self.board.cell_coordinates_to_notation(coords)
            self.assertEqual(result, expected_notation)

    def test_invalid_cell_coordinates_to_notation(self):
        invalid_coords = [(-1, 0), (8, 0), (0, -1), (0, 8), (8, 8)]
        for coords in invalid_coords:
            self.assertRaises(
                ValueError, self.board.cell_coordinates_to_notation, coords
            )


if __name__ == "__main__":
    unittest.main()
