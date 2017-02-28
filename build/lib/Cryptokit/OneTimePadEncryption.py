#!/usr/bin/env python
from __future__ import division, absolute_import, print_function, unicode_literals
__author__ = 'marcsantiago'
"""This function was designed to apply a one time pad encryption
on textual data that either comes from a file or that is entered
manually by the user.  Note, the suffix of the key file and the suffix
of the encrypted message file will be the same.  This allows
users to associate key files with their corresponding
encrypted text files."""
from random import choice
from binascii import hexlify, unhexlify
from sys import exit, stdout, version_info
from os import remove
from zipfile import ZipFile
from datetime import datetime
from struct import unpack
from string import ascii_letters

try:
    from pyminizip import compress
except ImportError:
    print("This module requires the pyminizip module.")
    print("To install the pyminizip module on unix or linux,")
    print("type [pip install pyminizip] terminal.")
    print("If using python3 please use [pip3 install pyminizip].")

try:
    from future_builtins import *
except ImportError:
    pass

try:
    input = raw_input
    range = xrange
except NameError:
    pass

def _string_converter(text_data):
    """Takes a given string or file and converts it to binary."""
    if version_info >= (3, 0):
        return bin(int.from_bytes(text_data.encode(), 'big'))
    else:
        return bin(int(hexlify(text_data), 16))

def _read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def _key_generator(time):
    """Generates a random list that is equal to
    the length of the provided string."""
    print("Generating Key Please Wait...")
    filename = "_".join(["key", time])
    key_list = []
    for i in range(32):
        key_list.append(choice(ascii_letters))

    with open(filename + ".dat", 'w') as data:
        data.write("".join(key_list))
    return _string_converter("".join(key_list))

def _encrypt_key_file(zip_password, time):
    """Encrypts the key.dat file with a zip encryption using pyminizip.
    For more instructions regarding pyminizip you can visit pypi.python.org
    and search for the module or google it."""

    filename = "_".join(["key", time])
    compress(filename + ".dat", filename + ".zip", zip_password, int(9))
    remove(filename + ".dat")

def _unzip_file(zip_file, zip_password):
    """Unzips key.zip file using a supplied password."""

    if version_info >= (3, 0):
        ZipFile(zip_file).extractall(pwd=str.encode(zip_password))
        print("File unzipped.")
    else:
        ZipFile(zip_file).extractall(pwd=zip_password)
        print("File unzipped.")

def decrypt_data(encrypted_string, key, string_file_mode=False, key_file_mode=False):
    """Method that takes either the key or the encrypted string as a
    string or can the key and encrypted string a as file and decrypts
    the string using the provided string. NOTE** In order to use the the key.dat file
    you must first also be able to unzip it using a password."""

    print("Starting Decryption...")

    if key_file_mode:
        if ".zip" in key:
            zf = ZipFile(key)
            try:
                if zf.testzip() == None:
                    ZipFile(key).extractall()
                    print("Successfully extracted, please use the key file \
                        with the .dat extension file as your key and try again.\n")
                    exit(0)
            except:
                print("Key.zip is encrypted!\n")
                _unzip_file(key, input("Please enter the password to unzip the key file and try again.\n"))

        else:
            my_key = key
            with open(my_key, 'r') as key_data:
                my_key = key_data.read()
    else:
        my_key = key

    if string_file_mode:
        my_string = encrypted_string
        with open(my_string, 'r') as string_data:
            my_string = string_data.read()
    else:
        my_string = encrypted_string

    my_string_num_list = my_string
    my_key_num_list = _string_converter(my_key)[2:]

    print("Decrypting file...please wait, this may take a while depending on file size.")
    decrypt_list = []
    for j in range(2, len(my_string_num_list)):
        index = j % len(my_key_num_list)
        decrypt_list.append(int(my_string_num_list[j]) ^ int(my_key_num_list[index]))

    decrypted_string = int("0b" + "".join((str(i) for i in decrypt_list)), 2)

    if version_info >= (3, 0):
        message =  decrypted_string.to_bytes((decrypted_string.bit_length() + 7) // 8, 'big').decode()
    else:
        message = unhexlify('%x' % decrypted_string)

    with open("decrypted_message.txt", 'w') as out_message:
        out_message.write(message)
    print("Decryption Complete.")
    return message

def encrypt_data(plain_text, string_file_mode=False):
    """Method that takes either the key or plaintext as a
    string or file. The key is randomly generated for you!"""

    print("Starting Encryption...")

    timestamp = str(datetime.now().strftime("%y%m%d_%H%M%S"))
    filename = "_".join(["encrypted_message", timestamp])

    if string_file_mode:
        with open(plain_text) as plaintext_data:
            file_data = str(plaintext_data.read())
            string_list = _string_converter(file_data)
    else:
        string_list = _string_converter(plain_text)

    key_list = _key_generator(timestamp)[2:]

    print("Encrypting file...please wait, this may take a while depending on file size.")
    encrypted_list = []
    for j in range(2, len(string_list)):
        index = j % len(key_list)
        encrypted_list.append(int(string_list[j]) ^ int(key_list[index]))

    with open(filename + ".txt", 'w') as message:
        message.write( "0b" + "".join((str(i) for i in encrypted_list)))

    #_encrypt_key_file(input("Please type in a password to zip and encrypt the key.dat file.\n"), timestamp)
    print("Encryption Complete.")

    return "0b" + "".join((str(i) for i in encrypted_list))

# def main():
#     #encrypt_data("test.txt", string_file_mode=True)
#     decrypt_data("encrypted_message_150412_105314.txt", "key_150412_105314.dat", string_file_mode=True, key_file_mode=True)
#
# if __name__ in '__main__':
#     main()
