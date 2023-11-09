from tkinter import *
win = Tk()
win.title("TIC TAC TOE 2 PLAYERS")
win.geometry("350x350")
win.configure(background = "blue")
turn = 1
sign = 'O'
board=['','','','','','','','','']
def windecide():
    global board
    global turn
    if board[0]==board[1]==board[2]=='O' or board[0]==board[1]==board[2]=='X':
        winner.configure(text=f"Winner player {turn}")
        turn = 3
    if board[3]==board[5]==board[4]=='O' or board[4]==board[5]==board[3]=='X':
        winner.configure(text=f"Winner player {turn}")
        turn = 3
    if board[7]==board[8]==board[6]=='O' or board[6]==board[7]==board[8]=='X':
        winner.configure(text=f"Winner player {turn}")
        turn = 3
    if board[0]==board[4]==board[8]=='O' or board[0]==board[4]==board[8]=='X':
        winner.configure(text=f"Winner player {turn}")
        turn = 3
    if board[0]==board[3]==board[6]=='O' or board[0]==board[3]==board[6]=='X':
        winner.configure(text=f"Winner player {turn}")
        turn = 3
    if board[1]==board[4]==board[7]=='O' or board[4]==board[1]==board[7]=='X':
        winner.configure(text=f"Winner player {turn}")
        turn = 3
    if board[2]==board[5]==board[8]=='O' or board[2]==board[5]==board[8]=='X':
        winner.configure(text=f"Winner player {turn}")
        turn = 3
    if board[6]==board[4]==board[2]=='O' or board[6]==board[4]==board[2]=='X':
        winner.configure(text=f"Winner player {turn}")
        turn = 3
def buttonclicked(id):
    global turn
    global board
    
    if board[id]== "":
        if turn==1:
            win.update_idletasks()
            if id == 0:
                b0.configure(text='O')
                b0.configure(state=DISABLED)
            elif id == 1:
                b1.configure(text='O')
                b1.configure(state=DISABLED)
            elif id == 2:
                b2.configure(text='O')
                b2.configure(state=DISABLED)
            elif id == 3:
                b3.configure(text='O')
                b3.configure(state=DISABLED)
            elif id == 4:
                b4.configure(text='O')
                b4.configure(state=DISABLED)
            elif id == 5:
                b5.configure(text='O')
                b5.configure(state=DISABLED)
            elif id == 6:
                b6.configure(text='O')
                b6.configure(state=DISABLED)
            elif id == 7:
                b7.configure(text='O')
                b7.configure(state=DISABLED)
            elif id == 8:
                b8.configure(text='O')
                b8.configure(state=DISABLED)
            board[id] = 'O'
            windecide()
            player.config(text="PLAYER 2")
            turn=2
            
        elif turn==2:
            win.update_idletasks()
            if id == 0:
                b0.configure(text='X')
                b0.configure(state=DISABLED)
            elif id == 1:
                b1.configure(text='X')
                b1.configure(state=DISABLED)
            elif id == 2:
                b2.configure(text='X')
                b2.configure(state=DISABLED)
            elif id == 3:
                b3.configure(text='X')
                b3.configure(state=DISABLED)
            elif id == 4:
                b4.configure(text='X')
                b4.configure(state=DISABLED)
            elif id == 5:
                b5.configure(text='X')
                b5.configure(state=DISABLED)
            elif id == 6:
                b6.configure(text='X')
                b6.configure(state=DISABLED)
            elif id == 7:
                b7.configure(text='X')
                b7.configure(state=DISABLED)
            elif id == 8:
                b8.configure(text='X')
                b8.configure(state=DISABLED)
            board[id] = 'X'
            windecide()
            turn=1
            player.config(text="PLAYER 1")

    

heading = Label(win,text="TWO PLAYER TIC-TAC-TOE",fg="white",bg="blue",height=2,width=20,font=("TimesRoman",12,'bold'))
player = Label(win,text="PLAYER 1",fg="white",bg="blue",height=2,width=20,font=("TimesRoman",12,'bold'))
pl = Label(win,text="PLAYER 1 - O",fg="white",bg="blue",height=2,width=10,font=("TimesRoman",12,'bold'))
p2 = Label(win,text="PLAYER 2 - X",fg="white",bg="blue",height=2,width=10,font=("TimesRoman",12,'bold'))
b0=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(0))
b1=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(1))
b2=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(2))
b3=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(3))
b4=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(4))
b5=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(5))
b6=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(6))
b7=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(7))
b8=Button(win,text='',fg="black",bg="grey",height=2,width=8,font=("TimesRoman",12,'bold'),command=lambda:buttonclicked(8))
winner = Label(win,text="",fg="white",bg="blue",height=2,width=20,font=("TimesRoman",12,'bold'))

player.place(x=150,y=300)
heading.place(x=80,y=10)
pl.place(x=40,y=50)
p2.place(x=200,y=50)
b0.place(x=40,y=100)
b1.place(x=130,y=100)
b4.place(x=130,y=150)
b7.place(x=130,y=200)
b3.place(x=40,y=150)
b2.place(x=220,y=100)
b5.place(x=220,y=150)
b8.place(x=220,y=200)
b6.place(x=40,y=200)
winner.place(x=40,y=250)
win.mainloop()
