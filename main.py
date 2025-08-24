import sys

from chess.boards import BOARD_CLASS, STANDARD_BOARD
from chess.interface.board import Board
from chess.interface.piece import Piece
from chess.pieces import PIECE_CLASS

# Arguments supported by the app
EXIT = "EXIT"
GUIDE = "GUIDE"


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
    """Get the class of the board."""
    if board_type.lower() not in BOARD_CLASS:
        raise ValueError(f"Invalid board type: {board_type}")
    return BOARD_CLASS[board_type.lower()]


def get_guide() -> str:
    """
    Get the guide for the user.
    """
    guide = """
    ------------------------------------------------------------
    CHESS GUIDE:
    ------------------------------------------------------------
    Chess simulation of 8x8 chess board. With chess notations as:
    * Rows: A-H
    * Columns: 1-8

    Supported Chess Pieces:
    * Pawn: It can only move 1 step at a time, in the vertical forward direction.
    * King: It can only move 1 step at a time, in all 8 directions (vertical, horizontal and diagonal)
    * Queen: It can move across the board in all 8 directions.

    Example: 'Pawn, A1'

    To exit, type 'exit'. To get this guide, type 'guide'.
    ------------------------------------------------------------
    """
    return guide


def main():
    print("Welcome to Chess! Let's play!")
    print(get_guide())

    while True:
        try:
            # If input given as command line arguments
            if len(sys.argv) > 1:
                user_input = sys.argv[1]
                print(f"Processing: {user_input}")
                process_move(user_input)
                break
            else:
                # If input given as user input
                user_input = input("\nEnter the move (e.g. 'Pawn, A1'): ")

                user_input = clean_input(user_input)

                if not user_input:
                    print("No input provided. Please try again.")
                    continue

                if user_input == EXIT:
                    print("Exiting...Goodbye!")
                    break

                if user_input == GUIDE:
                    print(get_guide())
                    continue

                process_move(user_input)
                continue
        except KeyboardInterrupt:
            print("Stopped by user. Goodbye!")
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again! For help, type 'guide'. To exit, type 'exit'.")
            break
        except Exception as e:
            print(f"Error: {e}")
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
    board = get_board_class(STANDARD_BOARD)()

    if not board.is_valid_notation(position):
        raise ValueError(f"Invalid notation: {position}")

    piece = piece_class(position)
    piece.set_coordinates(board.notation_to_cell_coordinates(position))

    coordinates_validator = board.get_coordinates_validator()
    moves_coordinates = piece.get_possible_moves(coordinates_validator)
    moves = [board.cell_coordinates_to_notation(move) for move in moves_coordinates]

    print(f"Possible moves for {piece_type} at {position}: {moves}")


if __name__ == "__main__":
    main()
