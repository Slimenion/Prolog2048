import prolog as pl
import tkinter
bg_color = '#FBF8EF'

pl.generate_board()
print(pl.board)
# pl.move_up()
# print(pl.board)
# pl.move_left()
# print(pl.board)
# pl.move_right()
# print(pl.board)
# pl.move_down()
# print(pl.board)


def clicked():
    check_lose_and_win = pl.move_left()
    if check_lose_and_win == "You win!":
        tkinter.Label(window, text="Вы выиграли").pack()

    if check_lose_and_win == "You lose":
        tkinter.Label(window, text="Вы проиграли").pack()

    lbl1.configure(text=pl.board[0])
    lbl2.configure(text=pl.board[1])
    lbl3.configure(text=pl.board[2])
    lbl4.configure(text=pl.board[3])
    lbl5.configure(text=pl.board[4])
    lbl6.configure(text=pl.board[5])
    lbl7.configure(text=pl.board[6])
    lbl8.configure(text=pl.board[7])
    lbl9.configure(text=pl.board[8])
    lbl10.configure(text=pl.board[9])
    lbl11.configure(text=pl.board[10])
    lbl12.configure(text=pl.board[11])
    lbl13.configure(text=pl.board[12])
    lbl14.configure(text=pl.board[13])
    lbl15.configure(text=pl.board[14])
    lbl16.configure(text=pl.board[15])
    print(pl.board)

def clicked1():
    check_lose_and_win = pl.move_right()
    if check_lose_and_win == "You win!":
        tkinter.Label(window, text="Вы выиграли").pack()

    if check_lose_and_win == "You lose":
        tkinter.Label(window, text="Вы проиграли").pack()

    lbl1.configure(text=pl.board[0])
    lbl2.configure(text=pl.board[1])
    lbl3.configure(text=pl.board[2])
    lbl4.configure(text=pl.board[3])
    lbl5.configure(text=pl.board[4])
    lbl6.configure(text=pl.board[5])
    lbl7.configure(text=pl.board[6])
    lbl8.configure(text=pl.board[7])
    lbl9.configure(text=pl.board[8])
    lbl10.configure(text=pl.board[9])
    lbl11.configure(text=pl.board[10])
    lbl12.configure(text=pl.board[11])
    lbl13.configure(text=pl.board[12])
    lbl14.configure(text=pl.board[13])
    lbl15.configure(text=pl.board[14])
    lbl16.configure(text=pl.board[15])
    print(pl.board)


def clicked2():
    check_lose_and_win = pl.move_up()
    if check_lose_and_win == "You win!":
        tkinter.Label(window, text="Вы выиграли").pack()

    if check_lose_and_win == "You lose":
        tkinter.Label(window, text="Вы проиграли").pack()

    lbl1.configure(text=pl.board[0])
    lbl2.configure(text=pl.board[1])
    lbl3.configure(text=pl.board[2])
    lbl4.configure(text=pl.board[3])
    lbl5.configure(text=pl.board[4])
    lbl6.configure(text=pl.board[5])
    lbl7.configure(text=pl.board[6])
    lbl8.configure(text=pl.board[7])
    lbl9.configure(text=pl.board[8])
    lbl10.configure(text=pl.board[9])
    lbl11.configure(text=pl.board[10])
    lbl12.configure(text=pl.board[11])
    lbl13.configure(text=pl.board[12])
    lbl14.configure(text=pl.board[13])
    lbl15.configure(text=pl.board[14])
    lbl16.configure(text=pl.board[15])
    print(pl.board)


def clicked3():
    check_lose_and_win = pl.move_down()
    if check_lose_and_win == "You win!":
        tkinter.Label(window, text="Вы выиграли").pack()

    if check_lose_and_win == "You lose":
        tkinter.Label(window, text="Вы проиграли").pack()

    lbl1.configure(text=pl.board[0])
    lbl2.configure(text=pl.board[1])
    lbl3.configure(text=pl.board[2])
    lbl4.configure(text=pl.board[3])
    lbl5.configure(text=pl.board[4])
    lbl6.configure(text=pl.board[5])
    lbl7.configure(text=pl.board[6])
    lbl8.configure(text=pl.board[7])
    lbl9.configure(text=pl.board[8])
    lbl10.configure(text=pl.board[9])
    lbl11.configure(text=pl.board[10])
    lbl12.configure(text=pl.board[11])
    lbl13.configure(text=pl.board[12])
    lbl14.configure(text=pl.board[13])
    lbl15.configure(text=pl.board[14])
    lbl16.configure(text=pl.board[15])
    print(pl.board)


window = tkinter.Tk()
window.title("Добро пожаловать в игру 2048")
lbl = tkinter.Label(window, text="2048")
lbl.grid(column=1, row=0)
window.geometry('400x400')

lbl1 = tkinter.Label(window, text="0")
lbl1.grid(column=1, row=1)
lbl2 = tkinter.Label(window, text="0")
lbl2.grid(column=2, row=1)
lbl3 = tkinter.Label(window, text="0")
lbl3.grid(column=3, row=1)
lbl4 = tkinter.Label(window, text="0")
lbl4.grid(column=4, row=1)

lbl5 = tkinter.Label(window, text="0")
lbl5.grid(column=1, row=2)
lbl6 = tkinter.Label(window, text="0")
lbl6.grid(column=2, row=2)
lbl7 = tkinter.Label(window, text="0")
lbl7.grid(column=3, row=2)
lbl8 = tkinter.Label(window, text="0")
lbl8.grid(column=4, row=2)

lbl9 = tkinter.Label(window, text="0")
lbl9.grid(column=1, row=3)
lbl10 = tkinter.Label(window, text="0")
lbl10.grid(column=2, row=3)
lbl11 = tkinter.Label(window, text="0")
lbl11.grid(column=3, row=3)
lbl12 = tkinter.Label(window, text="0")
lbl12.grid(column=4, row=3)

lbl13 = tkinter.Label(window, text="0")
lbl13.grid(column=1, row=4)
lbl14 = tkinter.Label(window, text="0")
lbl14.grid(column=2, row=4)
lbl15 = tkinter.Label(window, text="0")
lbl15.grid(column=3, row=4)
lbl16 = tkinter.Label(window, text="0")
lbl16.grid(column=4, row=4)

btn = tkinter.Button(window, text="влево", command=clicked)
btn.grid(column=0, row=6)
btn = tkinter.Button(window, text="вправо ", command=clicked1)
btn.grid(column=2, row=6)
btn = tkinter.Button(window, text="вверх ", command=clicked2)
btn.grid(column=1, row=5)
btn = tkinter.Button(window, text="   вниз   ", command=clicked3)
btn.grid(column=1, row=7)


window.mainloop()
