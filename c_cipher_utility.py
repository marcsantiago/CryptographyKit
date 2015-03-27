#!/usr/bin/env python
# The utility will not run if the helper_files folder is not in the same directory as the utility script
__author__ = 'marcsantiago'
import argparse

from Cryptokit.CaesarCipher import c_encipher, c_decipher, brute_force_decrypt


parser = argparse.ArgumentParser(description='Caesar Cipher Command Utility')
parser.add_argument('-e',  '--c_encipher_string', help='Encrypts a string that the user has entered')
parser.add_argument('-d',  '--c_decipher_string', help='Decrypts a string. User must also key provided a key')
parser.add_argument('-k',  '--key',               help='Key must be a number 1 through 26')
parser.add_argument('-b',  '--brute_force',       help='Will attempt to brute force c_decipher a ciphered message from a string')
parser.add_argument('-bf', '--brute_force_file',  help='Will attempt to brute force c_decipher a ciphered message from a text file')
parser.add_argument('-ef', '--c_encipher_file',   help='Encipher text file')
parser.add_argument('-df', '--c_decipher_file',   help='Decipher text file')

args = vars(parser.parse_args())

if args['c_encipher_string']:
  print(c_encipher(args['c_encipher_string'], int(args['key'])))

elif args['c_encipher_file']:
  print(c_encipher(args['c_encipher_file'], int(args['key']), file_mode=True))

elif args['c_decipher_string']:
  print(c_decipher(args['c_decipher_string'], int(args['key'])))

elif args['c_decipher_file']:
  print(c_decipher(args['c_decipher_file'], int(args['key']),  file_mode=True))

elif args['brute_force']:
  print(brute_force_decrypt(args['brute_force']))

elif args['brute_force_file']:
  print(brute_force_decrypt(args['brute_force_file'],  file_mode=True))

else:
     print("""
  -h, --help            show this help message and exit
  -e c_encipher_string,   --c_encipher_string c_encipher_string
                        Encrypts a string that the user has entered
  -d c_decipher_string,   --c_decipher_string c_decipher_string
                        Decrypts a string. User must also key provided a key
  -k KEY, --key KEY     Key must be a number 1 through 26
  -b BRUTE_FORCE,       --brute_force BRUTE_FORCE
                        Will attempt to brute force c_decipher a ciphered
                        message from a string
  -bf BRUTE_FORCE_FILE, --brute_force_file BRUTE_FORCE_FILE
                        Will attempt to brute force c_decipher a ciphered
                        message from a file
  -ef c_encipher_file,    --c_encipher_file c_encipher_file
                        c_encipher file data
  -df c_decipher_file,    --c_decipher_file c_decipher_file
 """)
