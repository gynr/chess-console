import unittest
from chess.pieces.queen import Queen
from chess.boards.standard import StandardBoard


class TestQueen(unittest.TestCase):
    """
    Test Queen with standard board
    """

    def setUp(self):
        self.board = StandardBoard()
        self.coordinates_validator = self.board.get_coordinates_validator()

    def test_valid_move_directions(self):
        queen = Queen("D4")
        directions, is_indefinite = queen.get_move_directions()

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

        self.assertTrue(is_indefinite)  # Queen can move indefinitely
        self.assertEqual(len(directions), len(expected_directions))
        for direction in expected_directions:
            self.assertIn(direction, directions)

    def test_valid_board_moves(self):
        """Test queen moves from various positions

        Test cases when queen is at:
        - enter of the board (27 moves)
        - corner (21 moves)
        - edge positions (21 moves)

        """

        # Current position, expected moves
        test_cases = [
            (
                "D4",  # center
                [
                    "A1",
                    "A4",
                    "A7",
                    "B2",
                    "B4",
                    "B6",
                    "C3",
                    "C4",
                    "C5",
                    "D1",
                    "D2",
                    "D3",
                    "D5",
                    "D6",
                    "D7",
                    "D8",
                    "E3",
                    "E4",
                    "E5",
                    "F2",
                    "F4",
                    "F6",
                    "G1",
                    "G4",
                    "G7",
                    "H4",
                    "H8",
                ],
            ),
            (
                "A1",  # corner
                [
                    "A2",
                    "A3",
                    "A4",
                    "A5",
                    "A6",
                    "A7",
                    "A8",
                    "B1",
                    "C1",
                    "D1",
                    "E1",
                    "F1",
                    "G1",
                    "H1",
                    "B2",
                    "C3",
                    "D4",
                    "E5",
                    "F6",
                    "G7",
                    "H8",
                ],
            ),
            (
                "A5",  # edge
                [
                    "A1",
                    "A2",
                    "A3",
                    "A4",
                    "A6",
                    "A7",
                    "A8",
                    "B4",
                    "B5",
                    "B6",
                    "C3",
                    "C5",
                    "C7",
                    "D2",
                    "D5",
                    "D8",
                    "E1",
                    "E5",
                    "F5",
                    "G5",
                    "H5",
                ],
            ),
        ]

        for test_case in test_cases:
            position, expected_moves = test_case
            queen = Queen(position)
            queen.set_coordinates(self.board.notation_to_cell_coordinates(position))

            moves = queen.get_possible_moves(self.coordinates_validator)
            moves_notations = [
                self.board.cell_coordinates_to_notation(move) for move in moves
            ]

            self.assertEqual(len(moves), len(expected_moves))
            for move in expected_moves:
                self.assertIn(move, moves_notations)


if __name__ == "__main__":
    unittest.main()
