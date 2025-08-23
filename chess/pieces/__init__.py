from .king import King
from .pawn import Pawn
from .queen import Queen

PAWN = "pawn"
KING = "king"
QUEEN = "queen"

PIECE_CLASS = {
    PAWN: Pawn,
    KING: King,
    QUEEN: Queen,
}
