from abc import ABC, abstractmethod
from chess.interface.board import Board

class Piece(ABC):

    def __init__(self, notation: str):
        """Intitalize chess piece with notation. Eg. A1

        Args:
            notation (str): Chess notation of the piece.
        """
        self.notation = notation.upper()


    @abstractmethod
    def get_possible_moves(self, board: Board) -> list[tuple[int, int]]:
        """
        Get all possible moves for a piece from a given position.

        Args:
            board (Board): Chess board instance.

        Returns:
            list[tuple[int, int]]: List of possible moves.
        """
        pass
    
    def get_notation_coordinates(self, board: Board) -> tuple[int, int]:
        """
        Get the coordinates of the piece on the board.

        Args:
            board (Board): Chess board instance.

        Returns:
            tuple[int, int]: Coordinates of the piece on the board.
        """
        return board.notation_to_cell_coordinates(self.notation)