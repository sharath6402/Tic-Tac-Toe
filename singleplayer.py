from tkinter import *

# Initialize main window
win = Tk()
win.title("TIC TAC TOE - 1 PLAYER")
win.geometry("350x400")
win.configure(background="blue")

board = [''] * 9
turn = 1  # 1 = Player (O), 2 = Computer (X)

# --- Utility Functions ---

def check_winner(bd):
    # Possible winning combinations
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for (a, b, c) in wins:
        if bd[a] != '' and bd[a] == bd[b] == bd[c]:
            return bd[a]
    if '' not in bd:
        return 'Draw'
    return None

# --- Minimax Algorithm ---
def minimax(bd, depth, is_maximizing):
    result = check_winner(bd)
    if result == 'X':  # Computer win
        return 1
    elif result == 'O':  # Player win
        return -1
    elif result == 'Draw':
        return 0

    if is_maximizing:
        best_score = -999
        for i in range(9):
            if bd[i] == '':
                bd[i] = 'X'
                score = minimax(bd, depth + 1, False)
                bd[i] = ''
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = 999
        for i in range(9):
            if bd[i] == '':
                bd[i] = 'O'
                score = minimax(bd, depth + 1, True)
                bd[i] = ''
                best_score = min(best_score, score)
        return best_score

def best_move():
    best_score = -999
    move = -1
    for i in range(9):
        if board[i] == '':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    return move

# --- UI and Game Logic ---

def make_move(i, player):
    global board
    if board[i] == '' and winner.cget("text") == "":
        board[i] = player
        buttons[i].config(text=player, state=DISABLED)
        result = check_winner(board)
        if result:
            if result == 'Draw':
                winner.config(text="It's a Draw!")
            else:
                winner.config(text=f"{result} Wins!")
            return True
        return False
    return True

def player_move(i):
    global turn
    if turn == 1:
        game_over = make_move(i, 'O')
        if not game_over:
            turn = 2
            player_label.config(text="Computer's Turn")
            win.after(500, computer_move)

def computer_move():
    global turn
    move = best_move()
    make_move(move, 'X')
    result = check_winner(board)
    if not result:
        turn = 1
        player_label.config(text="Your Turn (O)")

def reset_game():
    global board, turn
    board = [''] * 9
    turn = 1
    for b in buttons:
        b.config(text='', state=NORMAL)
    winner.config(text="")
    player_label.config(text="Your Turn (O)")

# --- UI Layout ---
Label(win, text="TIC TAC TOE - MINIMAX AI", fg="white", bg="blue",
      font=("Arial", 14, "bold")).pack(pady=10)

player_label = Label(win, text="Your Turn (O)", fg="white", bg="blue",
                     font=("Arial", 12, "bold"))
player_label.pack()

frame = Frame(win, bg="blue")
frame.pack(pady=20)

buttons = []
for i in range(9):
    b = Button(frame, text='', font=('Arial', 18, 'bold'), height=2, width=5,
               bg='lightgray', command=lambda i=i: player_move(i))
    b.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(b)

winner = Label(win, text="", fg="white", bg="blue", font=("Arial", 14, "bold"))
winner.pack(pady=10)

Button(win, text="Reset Game", font=("Arial", 12, "bold"),
       command=reset_game).pack(pady=10)

win.mainloop()
