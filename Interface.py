from Graphics import *
from FileHandler import *
from AnimeGenerator import *


class App:

    def __init__(self, main, width, height):
        self._width = width
        self._height = height
        self._main = main
        self.anime = AnimeGenerator(5, "yo")
        main.minsize(width=width, height=height)
        self.create_buttons();

        '''
        create_button(main, "Display all images", lambda: display_images(root, self._width), 500, 3, 2, 2)
        create_button(main, "Add file", lambda: add_file(), 510, 3, 2, 2)
        create_button(main, "Create anime", lambda: add_file(), 520, 3, 2, 2)
        '''

    def create_buttons(self):
        create_button(self._main, "Display all images", lambda: display_images(root, self._width), 500, 3, 2, 2)
        create_button(self._main, "Add file", lambda: add_file(), 510, 3, 2, 2)
        create_button(self._main, "Create anime", lambda: self.anime.create_anime(), 520, 3, 2, 2)

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







