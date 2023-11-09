#!/usr/bin/env python

# Standard Libaries
import json
import platform
import base64
import os
import requests

# Gimp specific Libary
from gimpfu import *


# Main Function + Gimp Filter Registration
def colorize(image, layer):
    # Get the system specific Path
    input_path, output_path, _current_system, _user_path = get_user_path()

    gimp.progress_init("Colorizing Image: '" + layer.name + "'...")

    # Creating a temporary file to send to server
    create_tmp_file(image, layer, input_path)

    # Send the temporary file to the server to process it
    colorize_on_server(input_path, output_path)

    # Replace the old Layer and paste the new added Layer
    replace_old_layer(image, layer, output_path)

    # Cleanup TEMP folder
    cleanup(input_path, output_path)

    pdb.gimp_progress_end()


register(
    "Colorize",
    "Colorize Image using PicWish API",
    "Colorize Image using PicWish API",
    "zyroz.dev (Noah W)",
    "MIT License",
    "2023",
    "<Image>/Filters/Enhance/Colorizer (PicWish API)",
    "*",
    [],
    [],
    colorize,
)


#  Get the system the plugin is running on and configure the user_path and tmp_path
def get_user_path():
    current_system = platform.system()

    os_dic = {
        "Windows": "USERPROFILE",  # Windows
        "Linux": "HOME",  # Linux
        "Darwin": "HOME",  # MacOS
    }

    user_path = os.environ.get(os_dic.get(current_system, ""), "Unknown OS")
    tmp_path = os.path.join(user_path, "tmp")

    # Intialise temporary file paths
    input_path = os.path.join(tmp_path, "input.png")
    output_path = os.path.join(tmp_path, "output.png")

    # Setup temporary Directory
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)

    return input_path, output_path, current_system, user_path


# Export the current layer as .png and save to temporary input location
def create_tmp_file(image, layer, path):
    # Try to save the image to the destination
    try:
        gimp.pdb.file_png_save(image, layer, path, "raw_filename", 0, 9, 0, 0, 0, 0, 0)
    except Exception as err:
        gimp.message("Unexpected error: " + str(err))


# Read API key from JSON file
def read_api_key():
    _input_path, _output_path, current_system, user_path = get_user_path()
    if current_system == "Linux":
        api_key_file = os.path.join(
            user_path,
            ".config",
            "GIMP",
            "2.10",
            "plug-ins",
            "colorize_api_key.json",
        )
    elif current_system == "Windows":
        api_key_file = os.path.join(
            user_path,
            "AppData",
            "Roaming",
            "GIMP",
            "2.10",
            "plug-ins",
            "colorize_api_key.json",
        )
    else:
        gimp.message("This Operating System is not supported!")
        return ""

    if os.path.exists(api_key_file):
        with open(api_key_file, "r") as file:
            api_key_data = json.load(file)
            return api_key_data["api_key"]
    else:
        return ""


# Send an API Request to the server and save the colorized image to the output_path
def colorize_on_server(input_path, output_path):
    api_key = read_api_key()

    response = requests.request(
        "POST",
        "https://techhk.aoscdn.com/api/tasks/visual/colorization",
        headers={"X-API-KEY": str(api_key)},
        data={"sync": "1", "return_type": "2", "format": "png"},
        files={"file": open(input_path, "rb")},
    )

    image_encoded = response.json()["data"]["image"]

    # Just for debbuging
    debug_path = os.path.join(
        tmp_path, "debug.json"
    )  # In order to run this also export the tmp_path from get_user_path()
    with open(debug_path, "w") as file:
        file.write(response.json())

    image_decoded = base64.b64decode(image_encoded)

    with open(output_path, "wb") as file:
        file.write(image_decoded)


# Replace the black & white image with its colorized version
def replace_old_layer(img, layer, path):
    # Get the current layer position.
    pos = 0
    for i in range(len(img.layers)):
        if img.layers[i] == layer:
            pos = i

    # Get the current layer name
    old_layer_name = layer.name

    # create a new layer from the colorized Image
    colorized_layer = pdb.gimp_file_load_layer(img, path)

    if not colorized_layer:
        gimp.message("Failed to load the image from the file.")
        return

    img.add_layer(colorized_layer, pos)

    # Just a temporary file name, it will get replaced once the old image is removed
    colorized_layer.name = old_layer_name + "_tmp"

    # Make the new layer visble and update everything
    colorized_layer.flush()
    colorized_layer.update(0, 0, colorized_layer.width, colorized_layer.height)

    # Remove the old image
    img.remove_layer(layer)

    # Rename the colorized version of the picture to be the same as the old one
    colorized_layer.name = old_layer_name


def cleanup(input_path, output_path):
    # Remove Black & White Image
    if os.path.exists(input_path):
        os.remove(input_path)

    # Remove Colorized Image
    if os.path.exists(output_path):
        os.remove(output_path)


main()
