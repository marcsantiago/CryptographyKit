#!/usr/bin/env python
# The utility will not run if the helper_files folder is not in the same directory as the utility script
__author__ = 'marcsantiago'
import argparse

from Cryptokit.VigenereCipher import v_encipher, v_decipher, v_dictionaryattack

parser = argparse.ArgumentParser(description='Vigenere Cipher Command Utility')
parser.add_argument('-e',  '--v_encipher_string',       help='Encrypts a string that the user has entered')
parser.add_argument('-d',  '--v_decipher_string',       help='Decrypts a string. User must also key provided a key')
parser.add_argument('-k',  '--key',                     help='Key can only contain english characters')
parser.add_argument('-a',  '--dictionary_attack',       help='Will attempt a dictionary attack')
parser.add_argument('-af', '--dictionary_attack_file',  help='Will attempt a dictionary attack on a ciphered text file')
parser.add_argument('-ef', '--v_encipher_file',         help='Encipher text file')
parser.add_argument('-df', '--v_decipher_file',         help='Decipher text file')

args = vars(parser.parse_args())

if args['v_encipher_string']:
	print(v_encipher(args['v_encipher_string'], args['key']))

elif args['v_encipher_file']:
	print(v_encipher(args['v_encipher_string'], args['key'], file_mode=True))

elif args['v_decipher_string']:
	print(v_encipher(args['v_decipher_string'], args['key']))

elif args['v_decipher_file']:
	print(v_encipher(args['v_decipher_file'], args['key'], file_mode=True))

elif args['dictionary_attack']:
	print(v_encipher(args['dictionary_attack']))

elif args['dictionary_attack_file']:
	# For More Functionality On the Dictionary Attack Call the Module Directly
	# There is a parameter to change the dictionary and percent similarity to English
	print(v_encipher(args['dictionary_attack_file'], file_mode=True))

else:
	print("""
  -h, --help                  show this help message and exit
  -e V_ENCIPHER_STRING,       --v_encipher_string V_ENCIPHER_STRING
						      Encrypts a string that the user has entered
  -d V_DECIPHER_STRING,       --v_decipher_string V_DECIPHER_STRING
						      Decrypts a string. User must also key provided a key
  -k KEY, --key KEY           Key can only contain english characters
  -a DICTIONARY_ATTACK,       --dictionary_attack DICTIONARY_ATTACK
						      Will attempt a dictionary attack
  -af DICTIONARY_ATTACK_FILE, --dictionary_attack_file DICTIONARY_ATTACK_FILE
						      Will attempt a dictionary attack on a ciphered text
						      file
  -ef V_ENCIPHER_FILE,        --v_encipher_file V_ENCIPHER_FILE
						      Encipher text file
  -df V_DECIPHER_FILE,        --v_decipher_file V_DECIPHER_FILE
						      Decipher text file
	""")

