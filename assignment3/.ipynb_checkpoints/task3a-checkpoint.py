import utils
import skimage
import skimage.morphology
import numpy as np


def remove_noise(im: np.ndarray) -> np.ndarray:
    """
        A function that removes noise in the input image.
        args:
            im: np.ndarray of shape (H, W) with boolean values (dtype=np.bool)
        return:
            (np.ndarray) of shape (H, W). dtype=np.bool
    """
    # START YOUR CODE HERE ### (You can change anything inside this block)
    # You can also define other helper functions
    
    #Using the skimage.morphology library: https://scikit-image.org/docs/dev/api/skimage.morphology.html
    #Need to create a footprint
    #footprint = skimage.morphology.disk(5)
    footprint = skimage.morphology.disk(7)
    #footprint = skimage.morphology.disk(10)
    #footprint = skimage.morphology.diamond(8)
    processed_image = skimage.morphology.binary_opening(im, footprint)
    processed_image = skimage.morphology.binary_closing(processed_image, footprint)
    
    return processed_image
    ### END YOUR CODE HERE ###


if __name__ == "__main__":
    # DO NOT CHANGE
    im = utils.read_image("noisy.png")
    binary_image = (im != 0)
    noise_free_image = remove_noise(binary_image)

    assert im.shape == noise_free_image.shape, "Expected image shape ({}) to be same as resulting image shape ({})".format(
        im.shape, noise_free_image.shape)
    assert noise_free_image.dtype == np.bool, "Expected resulting image dtype to be np.bool. Was: {}".format(
        noise_free_image.dtype)

    noise_free_image = utils.to_uint8(noise_free_image)
    utils.save_im("noisy-filtered.png", noise_free_image)
