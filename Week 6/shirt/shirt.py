import sys
from PIL import Image, ImageOps
import os


def main():
    # If all checks are passed within the check_args function, continue the program.
    if check_args() == True:
        # Opening the input and shirt image.
        with Image.open(sys.argv[1]) as input_image, Image.open("shirt.png") as shirt:
            # Getting the size of the shirt image.
            shirt_size = shirt.size
            # Resizing the input image to the size of the shirt
            input_image = ImageOps.fit(input_image, shirt_size)
            # Pasting the shirt onto the now resized input image.
            input_image.paste(shirt, box=None, mask=shirt)
            # Saving the result.
            input_image.save(sys.argv[2])


def check_args():
    # Checking if the correct amount of command-line arguments are given, if not, exiting the program with an error message.
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # Getting the file extensions of the input and out images.
        image_1_ext = os.path.splitext(sys.argv[1])
        image_2_ext = os.path.splitext(sys.argv[2])
        # Checking if the file extensions are the same, if not, exiting the program with an error message.
        if image_1_ext[1] != image_2_ext[1]:
            sys.exit("Input and output have different extensions")
        # Checking if the output image has a valid extension, exiting the program if not, with an error message.
        elif image_2_ext[1] not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid output")
        else:
            # Checking if the input image exists, else exiting with an error message.
            image_1 = sys.argv[1]
            if not os.path.exists(image_1):
                sys.exit("Input does not exist")
            else:
                # If all checks are passed, returning True.
                return True


if __name__ == "__main__":
    main()
