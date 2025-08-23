from chess.interface.piece import Piece
from chess.interface.board import Board

class King(Piece):
    """King piece 
    """

    def get_possible_moves(self, board: Board) -> list[tuple[int, int]]:
        """Get all possible moves for a king piece from a given notation.
        
        Possible behaviors:
        - Move 1 cell in any direction

        Args:
            board (Board): Chess board instance.

        Returns:
            list[tuple[int, int]]: List of possible moves.
        """
        moves = []
        col, row = self.get_notation_coordinates(board)

        # Except the current cell (0, 0), the king can move to 8 cells in any direction
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
            if board.is_valid_cell_coordinates((new_col, new_row)):
                moves.append((new_col, new_row))

        return moves
