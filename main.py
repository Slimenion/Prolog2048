import prolog as pl
import tkinter as tk

bg_color = '#FBF8EF'

pl.generate_board()
print(pl.board)
pl.move_up()
print(pl.board)
pl.move_left()
print(pl.board)
pl.move_right()
print(pl.board)
pl.move_down()
print(pl.board)

# icon_2048 = tk.PhotoImage(file='2048_icon.png')

#  Описываем появление окна
win = tk.Tk()

label_1 = tk.Label(
    win,
    text="Hello world!",
    bg=bg_color
)
label_1.pack()
# win.iconphoto(False, icon_2048)
win.title('2048')
win.geometry('500x600')
win.resizable(False, False)

win.config(bg=bg_color)

win.mainloop()
