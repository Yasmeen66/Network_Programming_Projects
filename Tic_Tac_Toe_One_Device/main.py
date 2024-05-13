from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe Game")
window.geometry("500x300")

lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)

turn = 1

def clickbtn1():
    global turn
    if btn1["text"] == " ":
        if turn == 1:
            turn = 2
            btn1["text"] = "X"
        elif turn == 2:
            turn = 1
            btn1["text"] = "O"
        check()
def clickbtn2():
    global turn
    if btn2["text"] == " ":
        if turn == 1:
            turn = 2
            btn2["text"] = "X"
        elif turn == 2:
            turn = 1
            btn2["text"] = "O"
        check()

def clickbtn3():
    global turn
    if btn3["text"] == " ":
        if turn == 1:
            turn = 2
            btn3["text"] = "X"
        elif turn == 2:
            turn = 1
            btn3["text"] = "O"
        check()

def clickbtn4():
    global turn
    if btn4["text"] == " ":
        if turn == 1:
            turn = 2
            btn4["text"] = "X"
        elif turn == 2:
            turn = 1
            btn4["text"] = "O"
        check()

def clickbtn5():
    global turn
    if btn5["text"] == " ":
        if turn == 1:
            turn = 2
            btn5["text"] = "X"
        elif turn == 2:
            turn = 1
            btn5["text"] = "O"
        check()

def clickbtn6():
    global turn
    if btn6["text"] == " ":
        if turn == 1:
            turn = 2
            btn6["text"] = "X"
        elif turn == 2:
            turn = 1
            btn6["text"] = "O"
        check()

def clickbtn7():
    global turn
    if btn7["text"] == " ":
        if turn == 1:
            turn = 2
            btn7["text"] = "X"
        elif turn == 2:
            turn = 1
            btn7["text"] = "O"
        check()

def clickbtn8():
    global turn
    if btn8["text"] == " ":
        if turn == 1:
            turn = 2
            btn8["text"] = "X"
        elif turn == 2:
            turn = 1
            btn8["text"] = "O"
        check()

def clickbtn9():
    global turn
    if btn9["text"] == " ":
        if turn == 1:
            turn = 2
            btn9["text"] = "X"
        elif turn == 2:
            turn = 1
            btn9["text"] = "O"
        check()

flag = 1
def check():
    global flag
    b1 = btn1["text"];
    b2 = btn2["text"];
    b3 = btn3["text"];
    b4 = btn4["text"];
    b5 = btn5["text"];
    b6 = btn6["text"];
    b7 = btn7["text"];
    b8 = btn8["text"];
    b9 = btn9["text"];
    flag = flag+1
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        winplayer(btn1["text"])
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        winplayer(btn4["text"]);
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        winplayer(btn7["text"]);
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        winplayer(btn1["text"]);
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        winplayer(btn2["text"]);
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        winplayer(btn3["text"]);
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        winplayer(btn1["text"]);
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        winplayer(btn7["text"]);
    if flag == 10:
        messagebox.showinfo("Failed:( ","Try Again!!")
        reset_game()

def winplayer(winner):
    result = "Game complete " + winner + " wins "
    messagebox.showinfo("Congrats:)",result)
    window.destroy()


def reset_game():
    global flag
    flag = 1
    # Reset the text of all buttons to empty
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "

btn1 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn1)
btn1.grid(row = 1, column = 1)
btn2 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn2)
btn2.grid(row = 1, column = 2)
btn3 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn3)
btn3.grid(row = 1, column = 3)
btn4 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn4)
btn4.grid(row = 2, column = 1)
btn5 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn5)
btn5.grid(row = 2, column = 2)
btn6 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn6)
btn6.grid(row = 2, column = 3)
btn7 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn7)
btn7.grid(row = 3, column = 1)
btn8 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn8)
btn8.grid(row = 3, column = 2)
btn9 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn9)
btn9.grid(row = 3, column = 3)
reset_button = Button(window, text="Reset",bg="white",fg="black",width=8,height=1,font=('Helvetica','10'), command=reset_game)
reset_button.grid(row=4, column=0)

window.mainloop()
