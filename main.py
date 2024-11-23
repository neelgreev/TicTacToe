from tkinter import *

# Initialize the root window
root = Tk()
root.iconbitmap("gameico.ico")
# Representation of the board
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
#This is to set the size of window
root.geometry("380x600")
#This is for the title of the window
root.title("TIC TAC TOE")
bg = PhotoImage(file="gameimgfin.png")

# Global variables
turn = "X"
game_mode = None  # "PvP" for Player vs Player, "PvC" for Player vs Computer

# welcome screen "which show which mode you want to choose"
def welcome_screen():
    global frame1, frame2
    frame1 = Frame(root)
    frame1.pack()
    titleLabel = Label(frame1, text="TIC TAC TOE", font=("Segoe", 30), bg="orange")
    titleLabel.pack(pady=20)




    frame2 = Frame(root)
    frame2.pack()

    btn_pvp = Button(frame2, text="Play with Friend", width=20, height=2, font=("Segoe", 15), bg="blue", fg="white",
                     command=lambda: start_game("PvP")) #command: Specifies the function that will be executed when the button is clicked.
    btn_pvp.pack(pady=20)

    btn_pvc = Button(frame2, text="Play with Computer", width=20, height=2, font=("Segoe", 15), bg="green", fg="white",
                     command=lambda: start_game("PvC")) #command: Specifies the function that will be executed when the button is clicked.
    btn_pvc.pack(pady=20)

# Create board buttons
def create_board():
    global buttons
    buttons = []
    for i in range(3):
        for j in range(3):
            button = Button(frame3, text=" ", width=4, height=2, font=("Segoe", 35), fg="white", bg="black")
            button.grid(row=i, column=j)
            button.bind("<Button-1>", play) #here i use Button-1 bcz it use for mouse right click
            buttons.append(button)

    restart_button = Button(frame3, text="RESTART", width=8, height=2, font=("Segoe", 20), bg="red",
                            command=restart_game)
    restart_button.grid(row=4, column=1)

# Start the game
def start_game(mode):
    global frame2, frame3, game_mode
    game_mode = mode

    frame1.destroy() #The destroy() method is typically used to Clear the screen: 
    frame2.destroy()  #The destroy() method is typically used to Clear the screen: 

    frame3 = Frame(root)
    background_label = Label(frame3, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame3.pack()

    # Create buttons for the board
    create_board()




#Play event coming from Mouse Click(Left click)
def play(event):
    global turn
    button = event.widget
    clicked = buttons.index(button) + 1

    if button["text"] == " ":
        button["text"] = turn
        board[clicked] = turn

        if checkWin(turn):
            winlabel = Label(frame3, text=f"{turn} WINS!", bg="green", font=("Arial", 30))
            winlabel.grid(row=3, column=0, columnspan=3)
        elif Tie():
            tielabel = Label(frame3, text="Tie Match!", bg="grey", font=("Arial", 30))
            tielabel.grid(row=3, column=0, columnspan=3)
        else:
            if game_mode == "PvP":
                turn = "O" if turn == "X" else "X"
            elif game_mode == "PvC" and turn == "X":
                turn = "O"
                ai_move()
                turn = "X"
# there is no need for else part bcz if this is PvC then it will show error.
# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if checkWin("O"):
        return 10 - depth
    elif checkWin("X"):
        return depth - 10
    elif Tie():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for key in board.keys():
            if board[key] == ' ':
                board[key] = "O"
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for key in board.keys():
            if board[key] == ' ':
                board[key] = "X"
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -float("inf")
    best_move = None
    for key in board.keys():
        if board[key] == ' ':
            board[key] = "O"
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    if best_move is not None:
        buttons[best_move - 1]["text"] = "O"
        board[best_move] = "O"
        if checkWin("O"):
            winlabel = Label(frame3, text="O WINS!", bg="green", font=("Arial", 30))
            winlabel.grid(row=3, column=0, columnspan=3)
        elif Tie():
            tielabel = Label(frame3, text="Tie Match!", bg="grey", font=("Arial", 30))
            tielabel.grid(row=3, column=0, columnspan=3)

# Check for win
def checkWin(player): #for check win i create a list of tuple.
    win_patterns = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
                    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
                    (1, 5, 9), (3, 5, 7)]  # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_patterns)

# Check for tie
def Tie():
    return all(board[key] != ' ' for key in board.keys())

# Restart game
def restart_game():
    # Clear the board
    for button in buttons:
        button["text"] = " "
    for key in board.keys():
        board[key] = " "

    # Remove any win or tie labels "this will try to clear 'X WIN OR OWIN" after restart "
    for widget in frame3.winfo_children():
        if isinstance(widget, Label) and widget["text"] in ["X WINS!", "O WINS!", "Tie Match!"]:
            widget.destroy()


#here we first time call the function above all are function defination. so program start from here.
# Start with the welcome screen
welcome_screen()

root.mainloop()
