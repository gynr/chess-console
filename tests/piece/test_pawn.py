import unittest
from chess.pieces.pawn import Pawn
from chess.boards.standard import StandardBoard


class TestPawn(unittest.TestCase):
    """
    Test Pawn with standard board
    """

    def setUp(self):
        self.board = StandardBoard()
        self.coordinates_validator = self.board.get_coordinates_validator()

    def test_valid_move_directions(self):
        pawn = Pawn("D4")
        directions, is_indefinite = pawn.get_move_directions()

        expected_directions = [(0, 1)]

        self.assertFalse(is_indefinite)
        self.assertEqual(directions, expected_directions)

    def test_valid_board_moves(self):
        """Test pawn moves from various positions

        Test cases when pawn is at:
        - top-left corner
        - top-right corner
        - middle of the board
        - bottom-left corner
        - bottom-right corner

        """

        # Current position, expected moves
        test_cases = [
            ("A1", ["A2"]),  # top-left
            ("H1", ["H2"]),  # top-right
            ("A8", []),  # bottom-left
            ("H8", []),  # bottom-right
            ("D4", ["D5"]),  # middle
        ]

        for position, expected_moves in test_cases:
            pawn = Pawn(position)
            pawn.set_coordinates(self.board.notation_to_cell_coordinates(position))

            moves = pawn.get_possible_moves(self.coordinates_validator)
            moves_notations = [
                self.board.cell_coordinates_to_notation(move) for move in moves
            ]

            self.assertEqual(len(moves), len(expected_moves))
            for move in expected_moves:
                self.assertIn(move, moves_notations)


if __name__ == "__main__":
    unittest.main()
