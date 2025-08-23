from chess.interface.piece import Piece
from chess.interface.board import Board
from chess.pieces import PIECE_CLASS
from chess.boards import BOARD_CLASS, STANDARD_BOARD
import sys

def get_piece_class(piece_type: str) -> type[Piece]:
    """Get the class of the piece.

    Args:
        piece_type (str): The type of the piece.

    Returns:
        class: The class of the piece.
    """
    if piece_type.lower() not in PIECE_CLASS:
        raise ValueError(f"Invalid piece type: {piece_type}")
    return PIECE_CLASS[piece_type.lower()]

def get_board_class(board_type: str) -> type[Board]:
    """Get the class of the board.
    """
    if board_type.lower() not in BOARD_CLASS:
        raise ValueError(f"Invalid board type: {board_type}")
    return BOARD_CLASS[board_type.lower()]

def get_guide() -> str:
    """
    Get the guide for the user.
    """ 
    guide = """
    Enter the type of piece and position to get all possible moves.
    Example: 'Pawn, A1'
    """
    return guide

def main():
    print("Welcome to Chess! Let's play!")
    print(get_guide())
    
    while True:
        try:
            if len(sys.argv) > 1:
                user_input = sys.argv[1]
                print(f"Processing: {user_input}")
                process_move(user_input)
                break
        except KeyboardInterrupt:
            print("Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please try again with format: 'PieceType, Position'")
            print(get_guide())
            break

def clean_input(user_input: str) -> str:
    """
    Clean the user input.
    """
    return user_input.strip().upper()

def process_move(user_input: str):
    """
    Process the move from the user input.
    """
    piece_type, position = user_input.split(",")
    piece_type = clean_input(piece_type)    
    position = clean_input(position)

    piece_class = get_piece_class(piece_type)
    board_class = get_board_class(STANDARD_BOARD)()

    if not board_class.is_valid_notation(position):
        raise ValueError(f"Invalid notation: {position}")

    piece = piece_class(position)
    moves = piece.get_possible_moves(board_class)
    print(moves)

if __name__ == "__main__":
    main()

