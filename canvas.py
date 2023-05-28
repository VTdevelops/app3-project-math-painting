import numpy as np
from PIL import Image


class Canvas:
    """ Object where all shapes are going to be drawn """
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create 3d numpy array of zeros
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        # Change [0, 0, 0] with user
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
