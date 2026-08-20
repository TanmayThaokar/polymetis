import chess
import chess.pgn


# ==========================================
# 1. LOAD PGN
# ==========================================

PGN_FILE = "games/game.pgn"

with open(PGN_FILE, "r") as file:
    game = chess.pgn.read_game(file)


# Check if PGN was loaded
if game is None:
    print("Could not read the PGN file.")
    exit()


print("====================================")
print("       CHESS ANALYZER")
print("====================================")

print("\nGame loaded successfully!\n")


# ==========================================
# 2. GAME INFORMATION
# ==========================================

print("Game Information")
print("----------------")

print("White :", game.headers.get("White", "Unknown"))
print("Black :", game.headers.get("Black", "Unknown"))
print("Result:", game.headers.get("Result", "Unknown"))

print()


# ==========================================
# 3. CREATE STARTING BOARD
# ==========================================

board = game.board()


# ==========================================
# 4. STORE ALL POSITIONS
# ==========================================

positions = []

# Starting position
positions.append(board.copy())


# ==========================================
# 5. STORE ALL MOVES
# ==========================================

moves = []

for move in game.mainline_moves():

    # Convert move to normal chess notation
    san_move = board.san(move)

    # Store move information
    moves.append({
        "uci": move.uci(),
        "san": san_move
    })

    # Play the move
    board.push(move)

    # Save the resulting board position
    positions.append(board.copy())


# ==========================================
# 6. DISPLAY ALL MOVES
# ==========================================

print("Moves")
print("-----")

for i, move in enumerate(moves):

    print(
        f"Move {i + 1}: "
        f"{move['san']} "
        f"({move['uci']})"
    )


# ==========================================
# 7. DISPLAY TOTAL MOVES
# ==========================================

print("\nTotal moves:", len(moves))


# ==========================================
# 8. DISPLAY BOARD
# ==========================================

def show_board(position):

    print("\n")
    print(position)
    print("\n")


# ==========================================
# 9. CURRENT MOVE
# ==========================================

current_position = 0


# ==========================================
# 10. SHOW STARTING POSITION
# ==========================================

print("\nStarting Position:")

show_board(positions[current_position])


# ==========================================
# 11. REPLAY SYSTEM
# ==========================================

while True:

    print("====================================")
    print("Current position:", current_position)
    print("====================================")

    if current_position == 0:

        print("Starting position")

    else:

        move = moves[current_position - 1]

        print(
            "Move:",
            current_position,
            move["san"]
        )

    print("\nOptions:")
    print("n = Next move")
    print("p = Previous move")
    print("q = Quit")

    choice = input("\nEnter choice: ").lower()


    # ======================================
    # NEXT MOVE
    # ======================================

    if choice == "n":

        if current_position < len(moves):

            current_position += 1

            show_board(
                positions[current_position]
            )

        else:

            print("\nAlready at the final position.")


    # ======================================
    # PREVIOUS MOVE
    # ======================================

    elif choice == "p":

        if current_position > 0:

            current_position -= 1

            show_board(
                positions[current_position]
            )

        else:

            print("\nAlready at the starting position.")


    # ======================================
    # QUIT
    # ======================================

    elif choice == "q":

        print("\nExiting Chess Analyzer...")
        break


    else:

        print("\nInvalid choice.")