from tkinter import *
import random
n=input("X participate name:")
m=input("O participate name:")
flag=True    
def next_turn(row, column):

    global player,X_wins,O_wins
    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(m+" Turn"))
            elif check_winner() is True:
                O_wins+=1
                X_score.config(text=(O_wins))
                if O_wins==5:
                    O_wins=0
                    X_score.config(text=(O_wins))

                    label.config(text=(n+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(n+" Turn"))

            elif check_winner() is True:
                X_wins+=1
                Y_score.config(text=(X_wins))
                if X_wins==5:
                    X_wins=0
                    Y_score.config(text=(X_wins))
                    label.config(text=(m+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
def quit():
    X_wins=0
    Y_score.config(text=(X_wins))
    O_wins=0
    X_score.config(text=(O_wins))
    global player

    player = random.choice(players)

    label.config(text=player+" Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
window = Tk()
O_wins=0
X_wins=0

window.title("Tic-Tac-Toe")
window.configure(bg="grey")
window.geometry("1300x1600")
window.resizable(True, True)
players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],
        [0,0,0],
        [0,0,0]]

top_frame = Frame(
    window,
    bg='#5D6D7E',
    width=1400,
    height=250
)
top_frame.place(x=0, y=0)
game_title = Label(
    top_frame,
    bg='#5D6D7E',
    fg='white',
    text='Tic Tac Toe',
    font=('', 58)
)
game_title.place(x=450, y=0)
X_title = Label(
    top_frame,
    bg='#5D6D7E',
    fg='blue',
    text=n+":",
    font=('', 40)
)
X_title.place(x=0, y=180)
Y_title = Label(
    top_frame,
    bg='#5D6D7E',
    fg='red',
    text=m+":",
    font=('', 40)
)
Y_title.place(x=1000, y=180)
Y_score = Label(
    top_frame,
    bg='#5D6D7E',
    fg='white',
    text=O_wins,
    font=('', 40)
)
Y_score.place(x=1250, y=180)

X_score = Label(
    top_frame,
    bg='#5D6D7E',
    fg='white',
    text=(X_wins),
    font=('', 40)
)
X_score.place(x=250, y=180)


label = Label(top_frame, text=player + " Turn", font=('arial',30), bg = "#5D6D7E", fg ="white")
label.place(x=590,y= 200)
start_button = Button(top_frame, text="Start Game", font=('arial',30),bg = "#5D6D7E", fg ="white", command=quit)
start_button.place(x=540, y=90)
reset_button = Button(top_frame, text="Restart Game", font=('arial',15),bg = "#5D6D7E", fg ="white", command=new_game)
reset_button.place(x=575, y=160)

bottom_frame = Frame(
    window,
    bg='#FFFFFF',
    width=1000,
    height=1000
)
bottom_frame.place(x=265, y=300)
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame, text="",font=('consolas',40), width=8, height=2,
                                    command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
        
if flag:
    window.mainloop()
