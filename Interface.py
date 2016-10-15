from Graphics import *
from FileHandler import *


class App:

    def __init__(self, main):
        main.minsize(width=666, height=666)
        create_button(main, "Display all images", lambda: display_images(root), 500, 3, 2, 2)
        create_button(main, "Add file", lambda: add_file(main), 510, 3, 2, 2)


def perform(fun, args):
    fun(args)


def submit():
    print("submit")

root = tkinter.Tk()
app = App(root)
root.mainloop()







