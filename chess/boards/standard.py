from chess.interface.board import Board


class StandardBoard(Board):
    """This is implementation of standard chess board."""

    def __init__(self):
        self.rows = 8
        self.columns = 8
        self.column_notation = "ABCDEFGH"
        self.row_notation = "12345678"

    def is_valid_notation(self, notation: str) -> bool:
        """Check if given notation is valid notation on the board.

        Example:
        - A1 -> True
        - H8 -> True
        - I1 -> False
        - A9 -> False

        Returns:
            bool: True if the notation is valid, False otherwise.
        """

        if not isinstance(notation, str) or len(notation) != 2:
            return False

        return notation[0] in self.column_notation and notation[1] in self.row_notation

    def is_valid_cell_coordinates(self, cell_coordinates: tuple[int, int]) -> bool:
        """Check if given cell coordinates are valid on the board.

        Example:
        - (0, 0) -> True
        - (7, 7) -> True
        - (0, 8) -> False
        - (8, 0) -> False

        Returns:
            bool: True if the cell coordinates are valid, False otherwise.
        """
        return (
            0 <= cell_coordinates[0] < self.rows
            and 0 <= cell_coordinates[1] < self.columns
        )

    def notation_to_cell_coordinates(self, notation: str) -> tuple[int, int]:
        """Convert chess notation to cell coordinates.

        Example:
        - A1 -> (0, 0)
        - H8 -> (7, 7)
        """

        if not self.is_valid_notation(notation):
            raise ValueError(f"Invalid notation: {notation}")

        return self.column_notation.index(notation[0]), self.row_notation.index(
            notation[1]
        )

    def cell_coordinates_to_notation(self, cell_coordinates: tuple[int, int]) -> str:
        """Convert cell coordinates to chess notation.

        Example:
        - (0, 0) -> A1
        - (7, 7) -> H8
        """

        if not self.is_valid_cell_coordinates(cell_coordinates):
            raise ValueError(f"Invalid cell coordinates: {cell_coordinates}")

        return (
            self.column_notation[cell_coordinates[0]]
            + self.row_notation[cell_coordinates[1]]
        )
