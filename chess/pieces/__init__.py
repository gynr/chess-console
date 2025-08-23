from .pawn import Pawn
from .king import King
from .queen import Queen


PAWN = "pawn"
KING = "king"
QUEEN = "queen"

PIECE_CLASS = {
    PAWN: Pawn,
    KING: King, 
    QUEEN: Queen,
}