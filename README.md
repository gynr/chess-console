# chess-console

A console-based chess simulation application.

## Features

List of application features

1. **Chessboard Setup**

   * Empty chess board.
   * 8×8 grid (64 cells).
   * Rows labeled `1–8`, columns labeled `A–H`.
   * Each cell uniquely identified (e.g., `A1`, `H8`).

2. **Supported Chess Pieces**

   * **Pawn**: It can only move 1 step at a time, in the vertical forward direction.
   * **King**: It can only move 1 step at a time, in all 8 directions (vertical, horizontal and diagonal)
   * **Queen**: It can move across the board in all 8 directions.


3. **Console application only (no GUI, no web).**
    
    * **Input Format**: String `"<Piece>, <Position>"` Example: `King, D5`.
    * **Output Format**: Comma-separated list of all **valid destination cells** for that piece from given position. Example: `C4, C5, C6, D4, D6, E4, E5, E6`


## Setup Instructions

1. Clone the repository:
   ```bash
   git clone git@github.com:gynr/chess-console.git
   cd chess-console
   ```

2. Create and activate virtual env
    ```bash
    python3 -m venv venvChessConsole
    source venvChessConsole/bin/activate
    ```

3. Install depenendcies
    ```bash
    pip install -r requirements.txt
    ```

4. Pre-commit hook setup
    ```bash
    pre-commit install
    ```

## How to Run the Program

1. Make sure you have completed `Setup Instructions`
2. Run following command:
    ```bash
    python main.py "Pawn, A1"
    ```
    * Here we pass two args: `<Chess Piece Name>, <Chess notation of the piece>`
    * Piece supported: `Pawn`, `Queen`, `King`
    * Standard chess notion: `<A-H><1-9>`

3. Output moves: `["A2"]` 
4. To exit the app, enter `exit`.
5. To get thye help, enter `guide`.


## How to run tests

1. Make sure you have completed `Setup Instructions`

2. Run following command:
    ```bash
    pytest tests -v
    ```





