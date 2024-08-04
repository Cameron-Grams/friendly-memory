"""
Working material for the notebook

PIL library: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#using-the-image-class



"""
from PIL import Image
import numpy as np
import os



def obtain_average_size(directory):
    """
    Given a path to a directory return the average size of the images
    in the directory
    Arguments:
        - directory: string, location of the images
    Returns:
        - average_size: tuple of integers, the width and height of the 
          average size
    """
    widths = []
    heights = []
    image_names = os.listdir(directory)
    for image in image_names:
        try:
            current_image = directory + "/" + image
            image_size = Image.open(current_image).size
            widths.append(image_size[0])
            heights.append(image_size[1])
        except:
            continue

    average_widths = np.average(widths)
    average_heights = np.average(heights)
    return (int(average_widths),int(average_heights))





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
    image_array = np.array(image)
    single_array = image_array.reshape(250000,)
    return single_array, str(single_array)[1:-1]
    
