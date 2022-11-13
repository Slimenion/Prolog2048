import prolog as pl
import tkinter
bg_color = '#CCC0B4'
font_color = '#FFFFFF'
button_color = '#BCAEA1'

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
lbl = tkinter.Label(window, text="2048", background=bg_color, font=('Arial', 28, 'bold'), width=4, fg=font_color)
lbl.grid(row=0, column=2, columnspan=2)
window.geometry('380x530+770+300')
photo = tkinter.PhotoImage(file='2048_icon.png')
window.iconphoto(False, photo)
window.config(background=bg_color)



for i in range(4):
    for j in range(4):
        tkinter.Label(window, text=f"-", background=button_color, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid").grid(row=i+1, column=j+1)




lbl1 = tkinter.Label(window, text="-", background=button_color, padx=15, pady=15, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid",)
lbl1.grid(row=1, column=1)
lbl2 = tkinter.Label(window, text="-", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl2.grid(row=1, column=2)
lbl3 = tkinter.Label(window, text="-", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl3.grid(row=1, column=3)
lbl4 = tkinter.Label(window, text="-", width=3,  height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl4.grid(row=1, column=4)

lbl5 = tkinter.Label(window, text="-", background=button_color, padx=15, pady=15, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid")
lbl5.grid(row=2, column=1)
lbl6 = tkinter.Label(window, text="-", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl6.grid(row=2, column=2)
lbl7 = tkinter.Label(window, text="-", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl7.grid(row=2, column=3)
lbl8 = tkinter.Label(window, text="-", width=3,  height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid" )
lbl8.grid(row=2, column=4)

lbl9 = tkinter.Label(window, text="-", background=button_color, padx=15, pady=15, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid")
lbl9.grid(row=3, column=1)
lbl10 = tkinter.Label(window, text="-", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl10.grid(row=3, column=2)
lbl11 = tkinter.Label(window, text="-", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl11.grid(row=3, column=3)
lbl12 = tkinter.Label(window, text="-", width=3,  height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl12.grid(row=3, column=4)

lbl13 = tkinter.Label(window, text="-", background=button_color, padx=15, pady=15, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid")
lbl13.grid(row=4, column=1)
lbl14 = tkinter.Label(window, text="-", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl14.grid(row=4, column=2)
lbl15 = tkinter.Label(window, text="-", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl15.grid(row=4, column=3)
lbl16 = tkinter.Label(window, text="-", width=3,  height=1, padx=15, pady=15, background='#BCAEA1', font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl16.grid(row=4, column=4)

btn = tkinter.Button(window, text="вверх ", command=clicked2, bg='#40CB9A', width=6,  height=1, font=('Arial', 16, 'bold'), pady=5, fg=font_color)
btn.grid(row=5, column=2, columnspan=2)
btn = tkinter.Button(window, text="влево", command=clicked, bg='#40CB9A', width=6,  height=1, font=('Arial', 16, 'bold'), pady=5, fg=font_color)
btn.grid(row=6, column=1)
btn = tkinter.Button(window, text="вправо ", command=clicked1, bg='#40CB9A', width=6,  height=1, font=('Arial', 16, 'bold'), pady=5, fg=font_color)
btn.grid(row=6, column=4, columnspan=3)
btn = tkinter.Button(window, text="   вниз   ", command=clicked3, bg='#40CB9A', width=6,  height=1, font=('Arial', 16, 'bold'), pady=5, fg=font_color)
btn.grid(row=7, column=2, columnspan=2)


window.mainloop()
