import unittest
from chess.pieces.king import King
from chess.boards.standard import StandardBoard


class TestKing(unittest.TestCase):
    """
    Test King with standard board
    """

    def setUp(self):
        self.board = StandardBoard()
        self.coordinates_validator = self.board.get_coordinates_validator()

    def test_valid_move_directions(self):
        king = King("D4")
        directions, is_indefinite = king.get_move_directions()

        expected_directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        self.assertFalse(is_indefinite)
        self.assertEqual(len(directions), len(expected_directions))
        for direction in expected_directions:
            self.assertIn(direction, directions)

    def test_valid_board_moves(self):
        """Test king moves from various positions

        Test cases when king is at:
        - center of the board (8 moves)
        - corner (3 moves)
        - edge (5 moves)

        """

        # Current position, expected moves
        test_cases = [
            ("D4", ["C3", "C4", "C5", "D3", "D5", "E3", "E4", "E5"]),  # center
            ("A1", ["A2", "B1", "B2"]),  # corner
            ("H5", ["G4", "G5", "G6", "H4", "H6"]),  # edge
        ]

        for position, expected_moves in test_cases:
            king = King(position)
            king.set_coordinates(self.board.notation_to_cell_coordinates(position))

            moves = king.get_possible_moves(self.coordinates_validator)
            moves_notations = [
                self.board.cell_coordinates_to_notation(move) for move in moves
            ]

            self.assertEqual(len(moves), len(expected_moves))
            for move in expected_moves:
                self.assertIn(move, moves_notations)


if __name__ == "__main__":
    unittest.main()
