from abc import ABC, abstractmethod

class Board(ABC):

    @abstractmethod
    def notation_to_cell_coordinates(self, notation: str) -> tuple[int, int]:
        """
        Convert a chess notation to cell coordinates.
        Example for 8x8 board:
        - A1 -> (0, 0)
        - H8 -> (7, 7)
        """
        pass

    @abstractmethod
    def cell_coordinates_to_notation(self, cell_coordinates: tuple[int, int]) -> str:
        """
        Convert a cell coordinates to chess notation.
        Example for 8x8 board:
        - (0, 0) -> A1
        - (7, 7) -> H8
        """
        pass

    @abstractmethod
    def is_valid_notation(self, notation: str) -> bool:
        """
        Check if a notation is valid on the board.
        """
        pass

    @abstractmethod
    def is_valid_cell_coordinates(self, cell_coordinates: tuple[int, int]) -> bool:
        """
        Check if a cell coordinates are valid on the board.
        """
        pass

    
