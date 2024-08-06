"""
Working material for the notebook

PIL library: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class



"""
from PIL import Image
import numpy as np
import os
import json


def pixel_values(image_path, reshape_size):
    """
    Given an image return a string with the pixel  values
    Arguments:
        - image: string
        - reshape_size: tuple of integers, size to reshape images to
    Returns:
        - pixels: string
    """

    image = Image.open(image_path).convert('L')
    image = image.resize(reshape_size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image.getdata())
    single_array = image_array.reshape(250000,)
    single_string = " ".join(str(x) for x in single_array)
    return single_string

def class_json(path, image_class):
    """
    Given a path iterate over the images in the directory and create a json
    Arguments:
        - path to image directory
    Return: 
        - None
    """
    images = os.listdir(path)
    image_number = 1
    json_images = {}

    for image in images:
        if image_number % 200 == 0:
            print(f"{image_number} processed")
        path = path
        try:
            image_path = os.path.join(path, image)
            pixels = pixel_values(image_path, (500, 500))
            json_images[image_number] = pixels
            image_number += 1
        except:
            continue
        if image_number == 501:
            print("Complete")
            with open(f"val_{image_class}_images.json", "w") as f:
                json.dump(json_images, f)
            return True
       


if __name__ == "__main__":
    class_json("./data/val/6", "6")
