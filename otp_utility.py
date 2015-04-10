#!/usr/bin/env python
__author__ = 'marcsantiago'
import argparse

from Cryptokit.OneTimePadEncryption import encrypt_data, decrypt_data

parser = argparse.ArgumentParser(description='One Time Pad Encryption Command Line Utility')
parser.add_argument('-e', '--encrypt_string', help='Encrypts a string that the user has entered')
parser.add_argument('-d', '--decrypt_string', help='Decrypts a string. User must also key provided a key')
parser.add_argument('-k', '--key', help='User enters the key as a string')
parser.add_argument('-kf', '--key_file', help='User enters the key file path')
parser.add_argument('-ef', '--encrypt_file', help='Encrypts file data')
parser.add_argument('-df', '--decrypt_file', help='Decrypts data from file. key can be from file or string.')

args = vars(parser.parse_args())

if args['encrypt_string']:
  encrypt_data(args['encrypt_string'], string_file_mode=False)

elif args['encrypt_file']:
  encrypt_data(args['encrypt_file'], string_file_mode=True)

elif args['decrypt_string'] and args['key_file']:
  decrypt_data(args['decrypt_string'], args['key_file'], encrypted_string_file_mode=False, key_file_mode=True)

elif args['decrypt_string'] and args['key']:
  decrypt_data(args['decrypt_string'], args['key_file'], encrypted_string_file_mode=False, key_file_mode=False)

elif args['decrypt_file'] and args['key_file']:
  decrypt_data(args['decrypt_string'], args['key_file'], encrypted_string_file_mode=True, key_file_mode=True)

elif args['decrypt_file'] and args['key']:
  decrypt_data(args['decrypt_string'], args['key_file'], encrypted_string_file_mode=False, key_file_mode=False)

else:
    print("""
  -h, --help            show this help message and exit
  -e ENCRYPT_STRING, --encrypt_string ENCRYPT_STRING
                        Encrypts a string that the user has entered
  -d DECRYPT_STRING, --decrypt_string DECRYPT_STRING
                        Decrypts a string. User must also key provided a key
  -k KEY, --key KEY     User enters the key as a string
  -kf KEY_FILE,      --key_file KEY_FILE 
                        User enters the key file path
  -ef ENCRYPT_FILE,  --encrypt_file ENCRYPT_FILE
                        Encrypts file data
  -df DECRYPT_FILE,  --decrypt_file DECRYPT_FILE
                        Decrypts data from file. key can be from file or
                        string.
""")
