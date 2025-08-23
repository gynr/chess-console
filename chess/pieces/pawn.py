from chess.interface.piece import Piece
from chess.interface.board import Board

class Pawn(Piece):
    """Pawn piece 
    """

    def get_possible_moves(self, board: Board) -> list[tuple[int, int]]:
        """Get all possible moves for a pawn piece from a given notation.
        
        Possible behaviors:
        - Move 1 cell forward

        Args:
            board (Board): Chess board instance.

        Returns:
            list[tuple[int, int]]: List of possible moves.
        """
        moves = []
        col, row = self.get_notation_coordinates(board)

        # Pawn can move 1 cell forward
        new_row = row + 1

        if board.is_valid_cell_coordinates((col, new_row)):
            moves.append((col, new_row))

        return moves
