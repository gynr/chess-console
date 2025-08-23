from chess.interface.piece import Piece
from chess.interface.board import Board

class Queen(Piece):
    """Queen piece 
    """

    def get_possible_moves(self, board: Board) -> list[tuple[int, int]]:
        """Get all possible moves for a queen piece from a given notation.
        
        Possible behaviors:
        - Move in any direction
        - Move in any number of cells

        Args:
            board (Board): Chess board instance.

        Returns:
            list[tuple[int, int]]: List of possible moves.
        """

        moves = []
        col, row = self.get_notation_coordinates(board)

        # Queen can move in any direction
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for direction in directions:
            new_col = col + direction[0]
            new_row = row + direction[1]

            # Check for all cells in the direction until the edge of the board is reached
            while board.is_valid_cell_coordinates((new_col, new_row)):
                moves.append((new_col, new_row))
                new_col += direction[0]
                new_row += direction[1]

        return moves