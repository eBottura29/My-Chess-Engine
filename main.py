# --------------------------
# Initial Position Bitboards
# --------------------------

white_pawns = 0x000000000000FF00
white_knights = 0x0000000000000042
white_bishops = 0x0000000000000024
white_rooks = 0x0000000000000081
white_queens = 0x0000000000000008
white_king = 0x0000000000000010

black_pawns = 0x00FF000000000000
black_knights = 0x4200000000000000
black_bishops = 0x2400000000000000
black_rooks = 0x8100000000000000
black_queens = 0x0800000000000000
black_king = 0x1000000000000000

# -----------------
# Utility Functions
# -----------------


def print_bitboard(bb):
    """
    Prints a bitboard in readable chessboard format.
    """

    for rank in range(7, -1, -1):
        for file in range(8):

            square = rank * 8 + file

            if bb & (1 << square):
                print("1", end=" ")
            else:
                print(".", end=" ")

        print()

    print()


def print_board():
    """
    Prints the full chessboard using FEN-style piece letters.
    """

    piece_map = {
        "P": white_pawns,
        "N": white_knights,
        "B": white_bishops,
        "R": white_rooks,
        "Q": white_queens,
        "K": white_king,
        "p": black_pawns,
        "n": black_knights,
        "b": black_bishops,
        "r": black_rooks,
        "q": black_queens,
        "k": black_king,
    }

    for rank in range(7, -1, -1):

        for file in range(8):

            square = rank * 8 + file
            bit = 1 << square

            piece_found = False

            for piece, bitboard in piece_map.items():

                if bitboard & bit:
                    print(piece, end=" ")
                    piece_found = True
                    break

            if not piece_found:
                print(".", end=" ")

        print()

    print()


def square_to_bit(square: str):
    """
    Converts a square like 'e4' into:

    [square_index, bitboard]

    Example:
        e4 -> [28, 268435456]
    """

    square = square.strip().lower()

    if len(square) != 2:
        raise ValueError("Invalid square format")

    file_char = square[0]
    rank_char = square[1]

    if file_char not in "abcdefgh":
        raise ValueError("Invalid file")

    if rank_char not in "12345678":
        raise ValueError("Invalid rank")

    file = ord(file_char) - ord("a")
    rank = int(rank_char) - 1

    square_number = rank * 8 + file
    bitboard = 1 << square_number

    return [square_number, bitboard]


# ----------
# FEN Loader
# ----------


def clear_bitboards():
    """
    Resets all piece bitboards to empty.
    """

    global white_pawns, white_knights, white_bishops
    global white_rooks, white_queens, white_king
    global black_pawns, black_knights, black_bishops
    global black_rooks, black_queens, black_king

    white_pawns = 0
    white_knights = 0
    white_bishops = 0
    white_rooks = 0
    white_queens = 0
    white_king = 0

    black_pawns = 0
    black_knights = 0
    black_bishops = 0
    black_rooks = 0
    black_queens = 0
    black_king = 0


def initialize_game(
    start_file="start.fen",
    position_file="position.fen"
):
    """
    Copies the starting position into the current position file.
    """

    with open(start_file, "r") as f:
        start_fen = f.read().strip()

    with open(position_file, "w") as f:
        f.write(start_fen)


def load_fen(filename="position.fen"):
    """
    Loads a chess position from a FEN file.
    """

    global white_pawns, white_knights, white_bishops
    global white_rooks, white_queens, white_king
    global black_pawns, black_knights, black_bishops
    global black_rooks, black_queens, black_king

    clear_bitboards()

    # Read FEN

    with open(filename, "r") as f:
        fen = f.read().strip()

    parts = fen.split()

    if len(parts) < 4:
        raise ValueError("Invalid FEN")

    board_part = parts[0]
    side_to_move = parts[1]
    castling_part = parts[2]
    en_passant = parts[3]

    ranks = board_part.split("/")

    if len(ranks) != 8:
        raise ValueError("Invalid FEN board")

    # Parse Piece Placement

    for rank_index, rank_string in enumerate(ranks):

        rank = 7 - rank_index
        file = 0

        for char in rank_string:

            # Empty squares
            if char.isdigit():
                file += int(char)
                continue

            square = rank * 8 + file
            bit = 1 << square

            # White pieces
            if char == "P":
                white_pawns |= bit

            elif char == "N":
                white_knights |= bit

            elif char == "B":
                white_bishops |= bit

            elif char == "R":
                white_rooks |= bit

            elif char == "Q":
                white_queens |= bit

            elif char == "K":
                white_king |= bit

            # Black pieces
            elif char == "p":
                black_pawns |= bit

            elif char == "n":
                black_knights |= bit

            elif char == "b":
                black_bishops |= bit

            elif char == "r":
                black_rooks |= bit

            elif char == "q":
                black_queens |= bit

            elif char == "k":
                black_king |= bit

            else:
                raise ValueError(f"Invalid FEN piece: {char}")

            file += 1

    # Game State
    black_to_move = 1 if side_to_move == "b" else 0

    white_kingside = "K" in castling_part
    white_queenside = "Q" in castling_part

    black_kingside = "k" in castling_part
    black_queenside = "q" in castling_part

    return {
        "black_to_move": black_to_move,
        "white_kingside": white_kingside,
        "white_queenside": white_queenside,
        "black_kingside": black_kingside,
        "black_queenside": black_queenside,
        "en_passant": en_passant,
    }


def main():
    # Reset current game to starting position
    initialize_game()

    # Load current position
    state = load_fen("position.fen")

    print("==== Game State ====")
    print(state)

    print("\n==== Board ====")
    print_board()


if __name__ == "__main__":
    main()