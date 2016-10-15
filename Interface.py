from Graphics import *
from FileHandler import *


class App:

    def __init__(self, main, width, height):
        self._width = width
        self._height = height
        main.minsize(width=width, height=height)
        create_button(main, "Display all images", lambda: display_images(root, self._width), 500, 3, 2, 2)
        create_button(main, "Add file", lambda: add_file(), 510, 3, 2, 2)

    @property
    def width(self):
        return self._width


def perform(fun, args):
    fun(args)


def submit():
    print("submit")

root = tkinter.Tk()
app = App(root, 600, 600)
root.mainloop()







