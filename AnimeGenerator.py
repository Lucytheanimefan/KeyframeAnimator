import imageio
import matplotlib
import matplotlib.image as mgimg
from matplotlib import animation
from PIL import Image
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from FileHandler import get_files


myimages=[]

def create_array_of_images(filenames):
    for fname in filenames:
        img = mgimg.imread(fname)
        imgplot = plt.imshow(img)

        # append AxesImage object to the list
        myimages.append([imgplot])
    return myimages
    #return [plt.imshow(mgimg.imread(f)) for f in filenames]


class AnimeGenerator:

    def __init__(self, frames_per_sec,  savename):
        self._frames_per_sec = frames_per_sec
        self._filenames = get_files()
        self.images=[]
        self._savename = savename

    def create_gif(self):
        for filename in self._filenames:
            self.images.append(imageio.imread(filename))
        imageio.mimsave(self._savename+'.gif', self.images)

    def create_anime(self):
        print("Creating anime")
        images = create_array_of_images(get_files())
        print(images)
        fig = plt.figure()
        my_anim = animation.ArtistAnimation(fig, images, interval=1000, blit=True, repeat_delay=1000)
        plt.show()

    def save(self, anime):
        anime.save()


