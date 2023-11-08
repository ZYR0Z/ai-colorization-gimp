#!/usr/bin/env python

from gimpfu import *

import os
import requests
import base64



# Initalise all user specific paths
user_path = os.environ["USERPROFILE"]
tmp_path = os.path.join(user_path, "tmp")


def create_tmp_file(image, layer, file_path):
    # Check if the tmp dir exists, else create it
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)

    # Try to save the image to the destination
    try:
        gimp.pdb.file_png_save(
            image, layer, file_path, "raw_filename", 0, 9, 0, 0, 0, 0, 0
        )
    except Exception as err:
        gimp.message("Unexpected error: " + str(err))


def colorize_on_server(file_path, colorized_path):
    response = requests.request(
        "POST",
        "https://techhk.aoscdn.com/api/tasks/visual/colorization",
        headers={"X-API-KEY": "YOUR API CODE HERE"},
        data={"sync": "1", "return_type": "2"},
        files={"file": open(file_path, "rb")},
    )

    data_json = response.text
    img_data = response.json()["data"]["image"]

    # Just for debbuging
    # data_file_path = str(tmp_path) + "\\" + "data.json"
    # with open(data_file_path, "w") as file:
    #     file.write(data_json)

    image_data = base64.b64decode(img_data)

    with open(colorized_path, "wb") as file:
        file.write(image_data)


def replace_old_layer(img, layer, colorized_path):
    # Get the layer position.
    pos = 0
    for i in range(len(img.layers)):
        if img.layers[i] == layer:
            pos = i

    new_layer = pdb.gimp_file_load_layer(img, colorized_path)

    if not new_layer:
        gimp.message("Failed to load the image from the file.")
        return

    oldName = layer.name

    img.add_layer(new_layer, pos)

    new_layer.name = oldName + "_tmp"

    new_layer.flush()
    new_layer.update(0, 0, new_layer.width, new_layer.height)

    img.remove_layer(layer)

    new_layer.name = oldName


def cleanup(file_path, colorized_path):
    # Remove Black & White Image
    if os.path.exists(file_path):
        os.remove(file_path)

    # Remove Colorized Image
    if os.path.exists(colorized_path):
        os.remove(colorized_path)


def colorize(image, layer):
    file_path = str(tmp_path) + "\\bw_tmp.png"
    colorized_path = str(tmp_path) + "\\" + "colorized.jpg"

    gimp.progress_init("Colorizing Image: '" + layer.name + "'...")

    # Creating a temporary file to send to server
    create_tmp_file(image, layer, file_path)

    # Send the tmp file to the server to process it
    colorize_on_server(file_path, colorized_path)

    # Replace the old Layer and paste the new added Layer
    replace_old_layer(image, layer, colorized_path)

    # Cleanup TEMP folder
    cleanup(file_path, colorized_path)

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

main()
