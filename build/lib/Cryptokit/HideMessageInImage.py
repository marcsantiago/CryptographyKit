#!/usr/bin/env python
from __future__ import division, absolute_import, print_function, unicode_literals
# This is module is designed to hide a string message inside of an image. Note, This
# is just for fun and applies no real encryption.  This is more of a way to obscure
# one's message inside of a png file
__author__ = 'marcsantiago'

try:
    from PIL import Image
except ImportError:
    print("This module requires the PIL module.")
    print("To install the PIL module on unix or linux,")
    print("type [pip install Pillow] terminal.")
    print("If using python3 please use [pip3 install Pillow].")

try:
    from easygui import buttonbox, enterbox, msgbox, fileopenbox
except ImportError:
    print("This module requires the easygui module.")
    print("To install the easygui module on unix or linux,")
    print("type [pip install easygui] terminal.")
    print("If using python3 please use [pip3 install easygui].")

def hide_or_show_message():
    """This method ask the user whether they want to encrypt a string or decrypt a *.png file."""
    temp_data = []
    answer = buttonbox("What would you like to do, encrypt a message or decrypt the image?", choices=["Encrypt", "Decrypt"])
    if answer == "Encrypt":
        plaintext = enterbox("Enter a message you would like to hide in an image.")
        im = Image.fromstring('L', (1, len(plaintext)), plaintext)
        filename = enterbox("Give your image a name.")

        if ".png" in filename:
            filename = filename.replace(".png", "")
        im.save(filename + ".png", format("PNG"))

    elif answer == "Decrypt":
        image_file = fileopenbox("Please pick an image file that you would like to decrypt.", filetypes=["*.png"])
        my_image = Image.open(image_file)
        pix = my_image.getdata()

        for i in list(pix):
            temp_data.append(i)

    return msgbox("".join([chr(i) for i in temp_data]))
