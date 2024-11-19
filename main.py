from tkinter import *

root = Tk()
root.iconbitmap("gameico.ico")
#Representation of the board
board={1:' ',2:' ',3:' ',
       4:' ',5:' ',6:' ',
       7:' ',8:' ',9:' '}

#This is to set the size of window
root.geometry("380x600")
#This is for the title of the window
root.title("TIC TAC TOE")
bg= PhotoImage(file= "gameimgfin.png")


frame1=Frame(root)
frame1.pack()
titleLabel=Label(frame1,text="TIC TAC TOE",font=("Seoge",30), bg="orange")
titleLabel.pack()







frame2=Frame(root)
background_label = Label(frame2, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame2.pack()



turn="X"
#Play event coming from Mouse Click(Left click)
def play(event):
    global turn
    button=event.widget
    clicked=(str(button))[-1]
    
    if(clicked=="n"):
        clicked=1
    else:
        clicked=int(clicked)
    
    if(button["text"]==" "):


        if(turn=="X"):
            button["text"]= "X"
            
            board[clicked]="X"
            if(checkWin(turn)):
                print(turn,' WON')
                winlabel=Label(frame2, text=f"{turn} WINS!" , bg="green",font=("Arial",30))
                winlabel.grid(row=3,column=0,columnspan=3)
            elif(Tie()):
                print('Tie')
                tielabel=Label(frame2, text="Tie Match!" , bg="grey",font=("Arial",30))
                tielabel.grid(row=3,column=0,columnspan=3)
            turn="O"

            
        else:
            button["text"]="O"
            
            board[clicked]="O"
            if(checkWin(turn)):
                print(turn,' WON')
                winlabel=Label(frame2, text=f"{turn} WINS!" , bg="green",font=("Arial",30))
                winlabel.grid(row=3,column=0,columnspan=3)
            elif(Tie()):
                print('Tie')
                tielabel=Label(frame2, text="Tie Match!" , bg="grey",font=("Arial",30))
                tielabel.grid(row=3,column=0,columnspan=3)
            
            

            turn="X"
    
            
    
  
#winning check
def checkWin(player):
    #ROWS CHECK
    if(board[1]==board[2] and board[2]==board[3] and board[3]==player):
        return True
    elif(board[4]==board[5] and board[5]==board[6] and board[6]==player):
        return True
    elif(board[7]==board[8] and board[8]==board[9] and board[9]==player):
        return True
    
    #COLUMNS CHECK
    elif(board[1]==board[4] and board[4]==board[7] and board[7]==player):
        return True
    elif(board[2]==board[5] and board[5]==board[8] and board[8]==player):
        return True
    elif(board[3]==board[6] and board[6]==board[9] and board[9]==player):
        return True
    

    #DIAGONALS CHECK
    elif(board[1]==board[5] and board[5]==board[9] and board[9]==player):
        return True
    elif(board[3]==board[5] and board[5]==board[7] and board[7]==player):
        return True
    else:
        return False
    
#TieCheck

def Tie():
    for i in board.keys():
        if(board[i]==' '):
            return False
    return True


#Restart

def restartGame():
    for i in buttons:
        i["text"]=" "
    for i in board.keys():
        board[i]=" "




#Below I have made the code for buttons
#FIRST ROW
button1=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button2=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button2.grid(row=0,column=1)
button2.bind("<Button-1>",play)

button3=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button3.grid(row=0,column=2)
button3.bind("<Button-1>",play)

#SECOND ROW

button4=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button4.grid(row=1,column=0)
button4.bind("<Button-1>",play)

button5=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button5.grid(row=1,column=1)
button5.bind("<Button-1>",play)

button6=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button6.grid(row=1,column=2)
button6.bind("<Button-1>",play)

#THIRD ROW

button7=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button7.grid(row=2,column=0)
button7.bind("<Button-1>",play)

button8=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button8.grid(row=2,column=1)
button8.bind("<Button-1>",play)

button9=Button(frame2,text=" ",width=4,height=2,font=("Seoge",35),fg="white",bg="black")
button9.grid(row=2,column=2)
button9.bind("<Button-1>",play)


buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]


restartButton=Button(frame2,text='RESTART',width=8,height=2,font=("Seoge",20),bg="red" ,command=restartGame)
restartButton.grid(row=4,column=1)

root.mainloop()

