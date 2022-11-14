import prolog as pl
import tkinter
bg_color = '#CCC0B4'
font_color = '#FFFFFF'
button_color = '#BCAEA1'
two_color = '#BDAD9E'
four_color = '#ECE0CA'
eigth_color = '#F2B179'
sixteen_color = '#EC8D53'
color_32 = '#EC8D53'
color_64 = '#E95937'
color_128 = '#F3D96B'
color_256 = '#ECC400'
color_512 = '#BEEC8A'
color_default = '#CCC0B4'

pl.generate_board()
# pl.move_up()
# print(pl.board)
# pl.move_left()
# print(pl.board)
# pl.move_right()
# print(pl.board)
# pl.move_down()
# print(pl.board)

# def refresh_table(check_lose_and_win):
#     if check_lose_and_win:
#         lbl1.configure(text=pl.board[0] if pl.board[0] > 0 else "")
#         if not lbl1['text'] == "":
#             lbl1['bg'] = button_color
#         else:
#             lbl1['bg'] = bg_color
#         lbl2.configure(text=pl.board[1] if pl.board[1] > 0 else "")
#         if not lbl2['text'] == "":
#             lbl2['bg'] = button_color
#         else:
#             lbl2['bg'] = bg_color
#         lbl3.configure(text=pl.board[2] if pl.board[2] > 0 else "")
#         if not lbl3['text'] == "":
#             lbl3['bg'] = button_color
#         else:
#             lbl3['bg'] = bg_color
#         lbl4.configure(text=pl.board[3] if pl.board[3] > 0 else "")
#         if not lbl4['text'] == "":
#             lbl4['bg'] = button_color
#         else:
#             lbl4['bg'] = bg_color
#         lbl5.configure(text=pl.board[4] if pl.board[4] > 0 else "")
#         if not lbl5['text'] == "":
#             lbl5['bg'] = button_color
#         else:
#             lbl5['bg'] = bg_color
#         lbl6.configure(text=pl.board[5] if pl.board[5] > 0 else "")
#         if not lbl6['text'] == "":
#             lbl6['bg'] = button_color
#         else:
#             lbl6['bg'] = bg_color
#         lbl7.configure(text=pl.board[6] if pl.board[6] > 0 else "")
#         if not lbl7['text'] == "":
#             lbl7['bg'] = button_color
#         else:
#             lbl7['bg'] = bg_color
#         lbl8.configure(text=pl.board[7] if pl.board[7] > 0 else "")
#         if not lbl8['text'] == "":
#             lbl8['bg'] = button_color
#         else:
#             lbl8['bg'] = bg_color
#         lbl9.configure(text=pl.board[8] if pl.board[8] > 0 else "")
#         if not lbl9['text'] == "":
#             lbl9['bg'] = button_color
#         else:
#             lbl9['bg'] = bg_color
#         lbl10.configure(text=pl.board[9] if pl.board[9] > 0 else "")
#         if not lbl10['text'] == "":
#             lbl10['bg'] = button_color
#         else:
#             lbl10['bg'] = bg_color
#         lbl11.configure(text=pl.board[10] if pl.board[10] > 0 else "")
#         if not lbl11['text'] == "":
#             lbl11['bg'] = button_color
#         else:
#             lbl11['bg'] = bg_color
#         lbl12.configure(text=pl.board[11] if pl.board[11] > 0 else "")
#         if not lbl12['text'] == "":
#             lbl12['bg'] = button_color
#         else:
#             lbl12['bg'] = bg_color
#         lbl13.configure(text=pl.board[12] if pl.board[12] > 0 else "")
#         if not lbl13['text'] == "":
#             lbl13['bg'] = button_color
#         else:
#             lbl13['bg'] = bg_color
#         lbl14.configure(text=pl.board[13] if pl.board[13] > 0 else "")
#         if not lbl14['text'] == "":
#             lbl14['bg'] = button_color
#         else:
#             lbl14['bg'] = bg_color
#         lbl15.configure(text=pl.board[14] if pl.board[14] > 0 else "")
#         if not lbl15['text'] == "":
#             lbl15['bg'] = button_color
#         else:
#             lbl15['bg'] = bg_color
#         lbl16.configure(text=pl.board[15] if pl.board[15] > 0 else "")
#         if not lbl16['text'] == "":
#             lbl16['bg'] = button_color
#         else:
#             lbl16['bg'] = bg_color
#     else:
#         tkinter.Label(window, text=str(check_lose_and_win)).grid(column=0, row=1000, columnspan=10)

def refresh_table(check_lose_and_win):
    if check_lose_and_win:
        lbl1.configure(text=pl.board[0] if pl.board[0] > 0 else "")
        if not lbl1['text'] == "":
            color_b = color_default
            match lbl1['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl1['bg'] = color_b
        else:
            lbl1['bg'] = bg_color
        lbl2.configure(text=pl.board[1] if pl.board[1] > 0 else "")
        if not lbl2['text'] == "":
            color_b = color_default
            match lbl2['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl2['bg'] = color_b
        else:
            lbl2['bg'] = bg_color
        lbl3.configure(text=pl.board[2] if pl.board[2] > 0 else "")
        if not lbl3['text'] == "":
            color_b = color_default
            match lbl3['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl3['bg'] = color_b
        else:
            lbl3['bg'] = bg_color
        lbl4.configure(text=pl.board[3] if pl.board[3] > 0 else "")
        if not lbl4['text'] == "":
            color_b = color_default
            match lbl4['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl4['bg'] = color_b
        else:
            lbl4['bg'] = bg_color
        lbl5.configure(text=pl.board[4] if pl.board[4] > 0 else "")
        if not lbl5['text'] == "":
            color_b = color_default
            match lbl5['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl5['bg'] = color_b
        else:
            lbl5['bg'] = bg_color
        lbl6.configure(text=pl.board[5] if pl.board[5] > 0 else "")
        if not lbl6['text'] == "":
            color_b = color_default
            match lbl6['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl6['bg'] = color_b
        else:
            lbl6['bg'] = bg_color
        lbl7.configure(text=pl.board[6] if pl.board[6] > 0 else "")
        if not lbl7['text'] == "":
            color_b = color_default
            match lbl7['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl7['bg'] = color_b
        else:
            lbl7['bg'] = bg_color
        lbl8.configure(text=pl.board[7] if pl.board[7] > 0 else "")
        if not lbl8['text'] == "":
            color_b = color_default
            match lbl8['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl8['bg'] = color_b
        else:
            lbl8['bg'] = bg_color
        lbl9.configure(text=pl.board[8] if pl.board[8] > 0 else "")
        if not lbl9['text'] == "":
            color_b = color_default
            match lbl9['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl9['bg'] = color_b
        else:
            lbl9['bg'] = bg_color
        lbl10.configure(text=pl.board[9] if pl.board[9] > 0 else "")
        if not lbl10['text'] == "":
            color_b = color_default
            match lbl10['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl10['bg'] = color_b
        else:
            lbl10['bg'] = bg_color
        lbl11.configure(text=pl.board[10] if pl.board[10] > 0 else "")
        if not lbl11['text'] == "":
            color_b = color_default
            match lbl11['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl11['bg'] = color_b
        else:
            lbl11['bg'] = bg_color
        lbl12.configure(text=pl.board[11] if pl.board[11] > 0 else "")
        if not lbl12['text'] == "":
            color_b = color_default
            match lbl12['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl12['bg'] = color_b
        else:
            lbl12['bg'] = bg_color
        lbl13.configure(text=pl.board[12] if pl.board[12] > 0 else "")
        if not lbl13['text'] == "":
            color_b = color_default
            match lbl13['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl13['bg'] = color_b
        else:
            lbl13['bg'] = bg_color
        lbl14.configure(text=pl.board[13] if pl.board[13] > 0 else "")
        if not lbl14['text'] == "":
            color_b = color_default
            match lbl14['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl14['bg'] = color_b
        else:
            lbl14['bg'] = bg_color
        lbl15.configure(text=pl.board[14] if pl.board[14] > 0 else "")
        if not lbl15['text'] == "":
            color_b = color_default
            match lbl15['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl15['bg'] = color_b
        else:
            lbl15['bg'] = bg_color
        lbl16.configure(text=pl.board[15] if pl.board[15] > 0 else "")
        if not lbl16['text'] == "":
            color_b = color_default
            match lbl16['text']:
                case 2:
                    color_b = two_color
                case 4:
                    color_b = four_color
                case 8:
                    color_b = eigth_color
                case 16:
                    color_b = sixteen_color
                case 32:
                    color_b = color_32
                case 64:
                    color_b = color_64
                case 128:
                    color_b = color_128
                case 256:
                    color_b = color_256
                case 512:
                    color_b = color_512
                case _:
                    color_b = color_default
            lbl16['bg'] = color_b
        else:
            lbl16['bg'] = bg_color
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


def clicked4():
    pl.generate_board()
    refresh_table(True)


window = tkinter.Tk()
window.title("Добро пожаловать в игру 2048")
lbl = tkinter.Label(window, text="2048", background=bg_color, font=('Arial', 28, 'bold'), width=4, fg=font_color)
lbl.grid(row=0, column=2, columnspan=2)
window.geometry('380x610+770+300')
photo = tkinter.PhotoImage(file='2048_icon.png')
window.iconphoto(False, photo)
window.config(background=bg_color)



# for i in range(4):
#     for j in range(4):
#         tkinter.Label(window, text=f"-", background=button_color, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid").grid(row=i+1, column=j+1)




lbl1 = tkinter.Label(window, text=" ", background=button_color, padx=15, pady=15, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid",)
lbl1.grid(row=1, column=1)
lbl2 = tkinter.Label(window, text=" ", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl2.grid(row=1, column=2)
lbl3 = tkinter.Label(window, text=" ", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl3.grid(row=1, column=3)
lbl4 = tkinter.Label(window, text=" ", width=3,  height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl4.grid(row=1, column=4)

lbl5 = tkinter.Label(window, text=" ", background=button_color, padx=15, pady=15, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid")
lbl5.grid(row=2, column=1)
lbl6 = tkinter.Label(window, text=" ", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl6.grid(row=2, column=2)
lbl7 = tkinter.Label(window, text=" ", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl7.grid(row=2, column=3)
lbl8 = tkinter.Label(window, text=" ", width=3,  height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid" )
lbl8.grid(row=2, column=4)

lbl9 = tkinter.Label(window, text=" ", background=button_color, padx=15, pady=15, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid")
lbl9.grid(row=3, column=1)
lbl10 = tkinter.Label(window, text=" ", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl10.grid(row=3, column=2)
lbl11 = tkinter.Label(window, text=" ", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl11.grid(row=3, column=3)
lbl12 = tkinter.Label(window, text=" ", width=3,  height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl12.grid(row=3, column=4)

lbl13 = tkinter.Label(window, text=" ", background=button_color, padx=15, pady=15, font=('Arial', 24, 'bold'), width=3, height=1, fg=font_color, borderwidth=4, relief="solid")
lbl13.grid(row=4, column=1)
lbl14 = tkinter.Label(window, text=" ", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl14.grid(row=4, column=2)
lbl15 = tkinter.Label(window, text=" ", width=3, height=1, padx=15, pady=15, background=button_color, font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl15.grid(row=4, column=3)
lbl16 = tkinter.Label(window, text=" ", width=3,  height=1, padx=15, pady=15, background='#BCAEA1', font=('Arial', 24, 'bold'), fg=font_color, borderwidth=4, relief="solid")
lbl16.grid(row=4, column=4)

btn = tkinter.Button(window, text="вверх ", command=clicked2, bg='#40CB9A', width=6,  height=1, font=('Arial', 16, 'bold'), pady=5, fg=font_color)
btn.grid(row=5, column=2, columnspan=2)
btn = tkinter.Button(window, text="влево", command=clicked, bg='#40CB9A', width=6,  height=1, font=('Arial', 16, 'bold'), pady=5, fg=font_color)
btn.grid(row=6, column=1)
btn = tkinter.Button(window, text="вправо ", command=clicked1, bg='#40CB9A', width=6,  height=1, font=('Arial', 16, 'bold'), pady=5, fg=font_color)
btn.grid(row=6, column=4, columnspan=3)
btn = tkinter.Button(window, text="   вниз   ", command=clicked3, bg='#40CB9A', width=6,  height=1, font=('Arial', 16, 'bold'), pady=5, fg=font_color)
btn.grid(row=7, column=2, columnspan=2)
lbl17 = tkinter.Label(window, text=" ", width=3,  height=1, padx=15, pady=15, background=bg_color,)
lbl17.grid(row=8, column=4, columnspan=4,)
btn = tkinter.Button(window, text="начать с начала", command=clicked4, bg='#40CB9A', width=13,  height=1, font=('Arial', 16, 'bold'), pady=4, fg=font_color)
btn.grid(row=9, column=2, columnspan=2)

refresh_table(True)

window.mainloop()
