from requests import get
from PIL import Image
import random


class Generator:
    def __init__(self):
        self.__QRNGSeed()

    # Make an API call to quantum rng the seed
    def __QRNGSeed(self):
        URL = "https://qrng.anu.edu.au/API/jsonI.php?length=8&type=uint8"
        nums = get(URL).json()["data"]

        seed = ""
        for num in nums:
            seed += str(num)

        self.__SetSeed(seed)

    # Seed the random library with given seed
    def __SetSeed(self, seed):
        random.seed(seed)

    # Create a random image of specified dimensions, type and save to path
    def GenerateImage(self, width, height, type, path=""):
        i = Image.new("RGB", (width, height))
        for y in range(height):
            for x in range(width):
                color = self.__GetRandomColor()
                if (type == "RGB"):
                    i.putpixel((x, y), color)
                elif (type == "BW"):
                    i.putpixel((x, y), (color[0], color[0], color[0]))

        new_seed = random.randint(100000, 100000000)
        self.__SetSeed(new_seed)

        # If there is no path specified, save in source dir
        if (path != ""):
            i.save(path + "/" + str(new_seed) + ".png")
        else:
            i.save(str(new_seed) + ".png")
        return i

    # Returns tuple with RGB values
    def __GetRandomColor(self):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        return (r, g, b)
