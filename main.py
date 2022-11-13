import prolog as pl
import tkinter
bg_color = '#FBF8EF'
bg_label = '#CCC0B4'

pl.generate_board()

def refresh_table(check_lose_and_win):
    if check_lose_and_win:
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
    else:
        tkinter.Label(window, text=str(check_lose_and_win)).grid(column=0, row=1000, columnspan=10)


def clicked():
    check_lose_and_win = pl.move_left()
    refresh_table(check_lose_and_win)


def clicked1():
    check_lose_and_win = pl.move_right()
    refresh_table(check_lose_and_win)


def clicked2():
    check_lose_and_win = pl.move_up()
    refresh_table(check_lose_and_win)


def clicked3():
    check_lose_and_win = pl.move_down()
    refresh_table(check_lose_and_win)


window = tkinter.Tk()
window.title("Добро пожаловать в игру 2048")
lbl = tkinter.Label(window, text="2048", bg=bg_color)
lbl.grid(column=0, row=0, columnspan=10)

window.geometry('430x600')
window.resizable(False, False)


lbl1 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl1.grid(column=1, row=1)
lbl2 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl2.grid(column=2, row=1)
lbl3 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl3.grid(column=3, row=1)
lbl4 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl4.grid(column=4, row=1)

lbl5 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl5.grid(column=1, row=2)
lbl6 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl6.grid(column=2, row=2)
lbl7 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl7.grid(column=3, row=2)
lbl8 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl8.grid(column=4, row=2)

lbl9 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl9.grid(column=1, row=3)
lbl10 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl10.grid(column=2, row=3)
lbl11 = tkinter.Label(window, text="", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl11.grid(column=3, row=3)
lbl12 = tkinter.Label(window, text="0", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl12.grid(column=4, row=3)

lbl13 = tkinter.Label(window, text="0", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl13.grid(column=1, row=4)
lbl14 = tkinter.Label(window, text="0", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl14.grid(column=2, row=4)
lbl15 = tkinter.Label(window, text="0", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl15.grid(column=3, row=4)
lbl16 = tkinter.Label(window, text="0", width=4, height=2, padx=15, pady=15, bg=bg_label, foreground='white', font='Arial 25')
lbl16.grid(column=4, row=4)

btn = tkinter.Button(window, text="влево", command=clicked)
btn.grid(column=1, row=8, columnspan=2)
btn = tkinter.Button(window, text="вправо ", command=clicked1)
btn.grid(column=3, row=8, columnspan=2)
btn = tkinter.Button(window, text="вверх ", command=clicked2)
btn.grid(column=2, row=7, columnspan=2)
btn = tkinter.Button(window, text="вниз", command=clicked3)
btn.grid(column=2, row=9, columnspan=2)

refresh_table(True)

window.mainloop()
