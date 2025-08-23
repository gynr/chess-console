from chess.interface.piece import Piece


class Pawn(Piece):
    """Pawn piece"""

    def get_move_directions(self) -> tuple[list[tuple[int, int]], bool]:
        """Get all possible moves for a pawn piece from a given notation.

        Possible behaviors:
        - Move 1 cell forward

        Returns:
            list[tuple[int, int]: List of possible directions.
            bool: True if the piece can move indefinitely.
        """
        # Pawn can move 1 cell forward
        directions = [
            (0, 1),
        ]

        return directions, False
