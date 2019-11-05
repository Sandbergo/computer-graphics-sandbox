import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
import skimage
import utils




def convolve_im(im: np.array,
                kernel: np.array,
                verbose=True):
    """ Convolves the image (im) with the spatial kernel (kernel),
        and returns the resulting image.

        "verbose" can be used for visualizing different parts of the 
        convolution.
        
        Note: kernel can be of different shape than im.

    Args:
        im: np.array of shape [H, W]
        kernel: np.array of shape [K, K] 
        verbose: bool
    Returns:
        im: np.array of shape [H, W]
    """
    ### START YOUR CODE HERE ### (You can change anything inside this block)

    conv_result = im
    fft_im = np.fft.fft2(im)
    fft_kernel = fftpack.fft2(kernel, shape=im.shape[:2], axes=(0, 1))
    fft_conv = fft_im * fft_kernel
    conv_result = np.real(np.fft.ifft2(fft_conv))

    if verbose:
        # Use plt.subplot to place two or more images beside eachother
        plt.figure(figsize=(20, 4))
        # plt.subplot(num_rows, num_cols, position (1-indexed))
        
        plt.subplot(1, 5, 1)
        plt.title("Image")
        plt.imshow(im, cmap="gray")

        plt.subplot(1, 5, 2)
        plt.title("FT of image")
        plt.imshow(np.log(np.abs(np.fft.fftshift(fft_im))), cmap="gray")

        plt.subplot(1, 5, 3)
        plt.title("FT of kernel")
        plt.imshow(np.abs(np.fft.fftshift(fft_kernel)), cmap="gray")

        plt.subplot(1, 5, 4)
        plt.title("FT of convolved image")
        plt.imshow(np.log(np.abs(np.fft.fftshift(fft_conv))), cmap="gray")

        plt.subplot(1, 5, 5)
        plt.title("Convolved Image")
        plt.imshow(conv_result, cmap="gray")
    ### END YOUR CODE HERE ###
    return conv_result


if __name__ == "__main__":
    verbose = True  # change if you want

    # Changing this code should not be needed
    im = skimage.data.camera()
    im = utils.uint8_to_float(im)

    # DO NOT CHANGE
    gaussian_kernel = np.array([
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1],
    ]) / 256
    image_gaussian = convolve_im(im, gaussian_kernel, verbose)

    # DO NOT CHANGE
    sobel_horizontal = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    image_sobelx = convolve_im(im, sobel_horizontal, verbose)

    if verbose:
        plt.show()

    utils.save_im("camera_gaussian.png", image_gaussian)
    utils.save_im("camera_sobelx.png", image_sobelx)
