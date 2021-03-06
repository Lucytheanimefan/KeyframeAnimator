import tkinter
from tkinter.filedialog import askopenfilename
import imghdr
import PIL.Image
import PIL.ImageTk
from PIL import Image


files = []

def get_files():
    return files


def add_file():
    filename = askopenfilename()
    if check_if_image_file(filename):
        files.append(filename)
        print(files)
    else:
        print("Sorry, not a valid image file")


def display_images(root, max_width):
    show_images(root, max_width)


def show_images(root, max_width):
    x = 0
    y = 0
    for image in files:
        show_image(image, root, 300, x, y, 20, 20)
        x += 300
        if x >= max_width:
            x = 0
            y += 300


def show_image(filename, root, img_width,x, y, colspan, rspan):
    im = Image.open(filename)
    im = resize_image(img_width, im)
    my_image = PIL.ImageTk.PhotoImage(im)
    panel = tkinter.Label(root, image=my_image)
    panel.image = my_image
    panel.grid(row=y, column=x, columnspan=colspan, rowspan=rspan)


def resize_image(basewidth, im):
    wpercent = (basewidth / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    return im


def check_if_image_file(filename):
    image_type = imghdr.what(filename)
    print(image_type)
    return image_type is not None