from chess.interface.piece import Piece


class King(Piece):
    """King piece"""

    def get_move_directions(self) -> tuple[list[tuple[int, int]], bool]:
        """Get all possible moves for a king piece from a given notation.

        Possible behaviors:
        - Move 1 cell in any direction

        Returns:
            list[tuple[int, int]: List of possible directions.
            bool: True if the piece can move indefinitely.
        """

        # The king can move to 8 cells in any direction
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

        return directions, False
