import tkinter
from tkinter.filedialog import askopenfilename

files = []


class App:

    def __init__(self, main):
        global files
        main.minsize(width=666, height=666)
        create_button("Submit", submit, 2, 3, 2, 2)
        create_button("Add file", add_file, 30, 3, 2, 2)


def submit():
    print("submit")


def add_file():
    filename = askopenfilename()
    files.append(filename)
    print(files)


def create_button(text, button_action, row, col, rowspan, colspan):
    B = tkinter.Button(root, text=text, command=button_action)
    B.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan)

root = tkinter.Tk()
app = App(root)

root.mainloop()