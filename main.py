from tkinter import *
import random 

def next_turn(row, column):
    
    global player
    
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        if player == players[0]:
            
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
                
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
                
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
                
        else:
            
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
                
            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))
                
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
                
                  
def check_winner():
    for row in range(5):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == buttons[row][3]['text'] == buttons[row][4]['text'] != "":
            for column in range(5):
                buttons[row][column].config(bg="green")
            return True

    for column in range(5):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == buttons[3][column]['text'] == buttons[4][column]['text'] != "":
            for row in range(5):
                buttons[row][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == buttons[3][3]['text'] == buttons[4][4]['text'] != "":
        for i in range(5):
            buttons[i][i].config(bg="green")
        return True

    elif buttons[0][4]['text'] == buttons[1][3]['text'] == buttons[2][2]['text'] == buttons[3][1]['text'] == buttons[4][0]['text'] != "":
        for i in range(5):
            buttons[i][4 - i].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(5):
            for column in range(5):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    
    spaces = 25
    
    for row in range(5):
        for column in range(5):
            if buttons[row][column]['text'] != "":
                spaces -=1
                
    
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    
    global player
    
    player = random.choice(players)
    
    label.config(text=player+" turn")
    
    for row in range(5):
        for column in range(5):
            buttons[row][column].config(text="")


window = Tk()
window.title("Tic-Tac-Toe")
players= ["x", "o"]
player= random.choice(players)
buttons = [[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]

label = Label(text= player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(5):
    for column in range(5):
        buttons[row][column] = Button(frame, text="", font=('consolas',40), width= 5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()