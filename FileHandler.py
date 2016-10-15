import tkinter
from tkinter.filedialog import askopenfilename
import imghdr
import PIL.Image
import PIL.ImageTk
from PIL import Image

files = []
basewidth = 300


def add_file(root):
    filename = askopenfilename()
    files.append(filename)
    print(files)
    if check_if_image_file(filename):
        show_image(filename, root)


def show_image(filename, root):
    im = Image.open(filename)
    wpercent = (basewidth / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    my_image = PIL.ImageTk.PhotoImage(im)
    panel = tkinter.Label(root, image=my_image)
    panel.image = my_image
    panel.grid(row=0, column=0, columnspan=30, rowspan=30)


def check_if_image_file(filename):
    image_type = imghdr.what(filename)
    print(image_type)
    return image_type is not None