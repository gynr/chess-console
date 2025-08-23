from chess.interface.piece import Piece

class Queen(Piece):
    """Queen piece 
    """

    def get_move_directions(self) -> tuple[list[tuple[int, int]], bool]:
        """Get all possible moves for a queen piece from a given notation.
        
        Possible behaviors:
        - Move in any direction
        - Move indefinitely

        Returns:
            list[tuple[int, int]: List of possible directions.
            bool: True if the piece can move indefinitely.
        """
        # Queen can move in any direction, indefinitely
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

        return directions, True