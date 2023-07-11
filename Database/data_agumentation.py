import os
import numpy as np
from keras.utils import img_to_array, load_img
from keras.preprocessing.image import ImageDataGenerator

# from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img


def rand_noise(image):
    # add random noise to the image
    low, high = -5, 5
    noise = np.random.uniform(low, high, image.shape)
    return image + noise


def generate_images(input_dir, output_dir, n_images):
    # Create an ImageDataGenerator object
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.15,
        height_shift_range=0.15,
        shear_range=0.2,
        zoom_range=0.2,
        # horizontal_flip=True,
        fill_mode="nearest",
        preprocessing_function=rand_noise,
    )

    # Load images from input directory
    for filename in os.listdir(input_dir):
        if filename.split('.')[1] not in ["png", "jpg", "jpeg", "tif", "tiff"]:
            print(os.path.join(input_dir, filename))
            continue
        img = load_img(os.path.join(input_dir, filename))
        x = img_to_array(img)
        # Reshape to (1, height, width, channels)
        x = x.reshape((1,) + x.shape)

        # Generate n_images using data augmentation
        i = 0
        for batch in datagen.flow(
            x,
            batch_size=1,
            save_to_dir=output_dir,
            save_prefix="aug_",
            save_format="jpg",
        ):
            i += 1
            if i >= n_images:
                # print(i)
                break


# \*** to test individually ***/
# root_dir = os.getcwd()
# # Example usage
# input_dir_name = 29
# input_dir = f"{root_dir}\\{input_dir_name}"
# output_dir_name = f"aug_{input_dir_name}"
# output_dir = f"{root_dir}\\{output_dir_name}"
# n_images = 1  # Number of output images to generate per input image


root_dir = os.getcwd()
os.mkdir(f"{root_dir}\\aug_database6")
for i in range(56):
    os.mkdir(f"{root_dir}\\aug_database6\\{i}")
    
# Example usage
for i in range(56):
    input_dir = f"{root_dir}\\database6\\{i}"
    # output_dir_name = f"aug_{input_dir_name}"
    output_dir = f"{root_dir}\\aug_database6\\{i}"

    no_of_images_in_input_dir = len(os.listdir(input_dir))
    n_images = 9
    # n_images = 1  # Number of output images to generate per input image

    generate_images(input_dir, output_dir, n_images)
    print(i)
