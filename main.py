from pyswip import Prolog
import tkinter as tk
from contextlib import redirect_stdout


class TextWrapper:
    text_field: tk.Text

    def __init__(self, text_field: tk.Text):
        self.text_field = text_field

    def write(self, text: str):
        self.text_field.insert(tk.END, text)

    def flush(self):
        self.text_field.update()


root = tk.Tk()

text = tk.Text(root)
text.pack()

prolog = Prolog()
prolog.consult("2048.pl")

with redirect_stdout(TextWrapper(text)):  # подменяем объект sys.stdout на свой объект
    print("Slime")
    print(list(prolog.query("play.")))
    # print(list(prolog.query("showBoard(Board).")))# print внутри вызывает метод write объекта sys.stdout
    print("Hello again")  # Вывод в консоль

root.mainloop()

