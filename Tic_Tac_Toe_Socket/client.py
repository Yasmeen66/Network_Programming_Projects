from tkinter import *
from tkinter import messagebox
from threading import Thread
from socket import *

window = Tk()
window.title("Client")
window.geometry("500x300")

lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Server: X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Client: O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)

player = 2

def clickbtn1():
    global player
    if player == 2:
        player = 1
        btn1["text"] = "O"
        sendplay(1)
        check()
def clickbtn2():
    global player
    if btn2["text"] == " ":
        if player == 2:
            player = 1
            btn2["text"] = "O"
            sendplay(2)
        check()

def clickbtn3():
    global player
    if btn3["text"] == " ":
        if player == 2:
            player = 1
            btn3["text"] = "O"
            sendplay(3)
        check()

def clickbtn4():
    global player
    if btn4["text"] == " ":
        if player == 2:
            player = 1
            btn4["text"] = "O"
            sendplay(4)
        check()

def clickbtn5():
    global player
    if btn5["text"] == " ":
        if player == 2:
            player = 1
            btn5["text"] = "O"
            sendplay(5)
        check()

def clickbtn6():
    global player
    if btn6["text"] == " ":
        if player == 2:
            player = 1
            btn6["text"] = "O"
            sendplay(6)
        check()

def clickbtn7():
    global player
    if btn7["text"] == " ":
        if player == 2:
            player = 1
            btn7["text"] = "O"
            sendplay(7)
        check()

def clickbtn8():
    global player
    if btn8["text"] == " ":
        if player == 2:
            player = 1
            btn8["text"] = "O"
            sendplay(8)
        check()

def clickbtn9():
    global player
    if btn9["text"] == " ":
        if player == 2:
            player = 1
            btn9["text"] = "O"
            sendplay(9)
        check()

buttonlist=list()
client = socket(AF_INET, SOCK_STREAM)
host='127.0.0.1'
port=7228
# Connect to the server
client.connect((host,port ))

def sendplay(buttonNum):
    buttonNum=str(buttonNum)
    buttonNum = buttonNum.encode()
    client.send(buttonNum)
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
def recievemessage():
    while True:
        btn=client.recv(10)
        decodemessage(btn)
def decodemessage(btn):
    btn=btn.decode()
    btn=int(btn)
    handlemessage(btn)
def handlemessage(btn):
    global player
    buttonlist[btn-1]["text"]="X"
    player=2




thread=Thread(target=recievemessage)
thread.start()

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
buttonlist.append(btn1)
btn2 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn2)
btn2.grid(row = 1, column = 2)
buttonlist.append(btn2)
btn3 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn3)
btn3.grid(row = 1, column = 3)
buttonlist.append(btn3)
btn4 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn4)
btn4.grid(row = 2, column = 1)
buttonlist.append(btn4)
btn5 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn5)
btn5.grid(row = 2, column = 2)
buttonlist.append(btn5)
btn6 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn6)
btn6.grid(row = 2, column = 3)
buttonlist.append(btn6)
btn7 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn7)
btn7.grid(row = 3, column = 1)
buttonlist.append(btn7)
btn8 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn8)
btn8.grid(row = 3, column = 2)
buttonlist.append(btn8)
btn9 = Button(window,text=" ",bg="white",fg="black",width=3,height=1,font=('Helvetica','20'),command=clickbtn9)
btn9.grid(row = 3, column = 3)
buttonlist.append(btn9)
reset_button = Button(window, text="Reset",bg="white",fg="black",width=8,height=1,font=('Helvetica','10'), command=reset_game)
reset_button.grid(row=5, column=1, columnspan=5,pady=7)

window.mainloop()
