from abc import ABC, abstractmethod
from typing import Callable


class Piece(ABC):

    def __init__(self, notation: str):
        """Intitalize chess piece with notation. Eg. A1

        Args:
            notation (str): Chess notation of the piece.
        """
        self.notation = notation.upper()
        self._coordinates = None

    def set_coordinates(self, coordinates: tuple[int, int]):
        """Set the coordinates of the piece."""
        self._coordinates = coordinates

    def get_coordinates(self) -> tuple[int, int]:
        """Get the coordinates of the piece."""
        if self._coordinates is None:
            raise ValueError("Coordinates are not set")
        return self._coordinates

    @abstractmethod
    def get_move_directions(self) -> tuple[list[tuple[int, int]], bool]:
        """Get the move directions of the piece.

        Returns:
            list[tuple[int, int]]: List of move directions.
            bool: True if the piece can move indefinitely, False otherwise.
        """
        pass

    def get_possible_moves(
        self, coordinates_validator: Callable[[tuple[int, int]], bool]
    ) -> list[tuple[int, int]]:
        """
        Get all possible moves for a piece from a given position.

        Args:
            coordinates_validator (Callable[[tuple[int, int]], bool]): Function to validate coordinates.

        Returns:
            list[tuple[int, int]]: List of possible moves.
        """
        moves = []
        col, row = self.get_coordinates()

        # Except the current cell (0, 0), the king can move to 8 cells in any direction
        directions, is_indefinite = self.get_move_directions()

        for direction in directions:
            new_col = col + direction[0]
            new_row = row + direction[1]
            if is_indefinite:
                while coordinates_validator((new_col, new_row)):
                    moves.append((new_col, new_row))
                    new_col += direction[0]
                    new_row += direction[1]
            else:
                if coordinates_validator((new_col, new_row)):
                    moves.append((new_col, new_row))

        return moves
