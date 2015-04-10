#!/usr/bin/env python
from __future__ import division, absolute_import, print_function, unicode_literals
__author__ = 'marcsantiago'
"""This function is provides an easy way to cipher and decipher messages using a vigenere cipher.
Provided in this module is also a means to decrypt a ciphered messsage using a dictionary attack."""
from string import ascii_uppercase, ascii_lowercase 
from helper_files.detectEnglish import isEnglish
from itertools import izip
try:
	from future_builtins import *
except ImportError:
	pass

try:
	input = raw_input
	range = xrange
except NameError:
	pass

def _key_gen(plain_text, key):
	"""This protected function takes the users plain text 
	and key file and returns a list of key values"""
	key_string = []
	key_length = len(plain_text)
	key_mapper =  dict(izip(range(1,27), izip(ascii_lowercase, ascii_uppercase))) 

	for i in range(key_length):
		index = i % len(key)
		for k, v in key_mapper.items():
			if key[index] in v:
				key_string.append(k)

	return key_string

def v_encipher(plain_text, key, file_mode=False):
	"""This function takes plaintext entered as either a string or a 
	file and encrypts it using the provided key"""
	if file_mode:
		with open(plain_text, 'r') as in_data:
			plain = in_data.read()
	else:
		plain = plain_text
	
	generated_key = _key_gen(plain, key)

	enciphered_string = []
	for index in range(len(plain)):

		if plain[index].isalpha():
			num = ord(plain[index])
			num += generated_key[index]

			if plain[index].isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26

			elif plain[index].islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			enciphered_string.append(chr(num))
		else:
			enciphered_string.append(plain[index])

	answer = input("Write data to file? [y], [n]\n")
	if answer.lower() in ["yes", "y"]:
		with open("enciphered_vigenere.txt", 'w') as data:
			data.write("".join(enciphered_string))
	
	return "".join(enciphered_string)

def v_decipher(cipher_text, key, file_mode=False):
	"""This function takes ciphertext entered as either a string or a 
	file and encrypts it using the provided key"""
	if file_mode:
		with open(cipher_text, 'r') as in_data:
			cipher = in_data.read()
	else:
		cipher = cipher_text
	
	generated_key = _key_gen(cipher, key)

	deciphered_string = []
	for index in range(len(cipher)):

		if cipher[index].isalpha():
			num = ord(cipher[index])
			num += -generated_key[index]

			if cipher[index].isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26

			elif cipher[index].islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			deciphered_string.append(chr(num))
		else:
			deciphered_string.append(cipher[index])

	answer = input("Write data to file? [y], [n]\n")
	if answer.lower() in ["yes", "y"]:
		with open("deciphered_vigenere.txt", 'w') as data:
			data.write("".join(deciphered_string))
	
	return "".join(deciphered_string)

def v_dictionaryattack(cipher_text, dictionary_file="helper_files/dictionary.txt", file_mode=False, percent_match=55):
	"""This function takes ciphertext entered as either a string or a 
	file and attempts to decrypted it using the provided dictionary, you may
	use your own dictionary"""
	key_mapper =  dict(izip(range(1,27), izip(ascii_lowercase, ascii_uppercase))) 

	if file_mode:
		with open(cipher_text, 'r') as in_data:
			cipher_text = in_data.read()

	print("Trying dictionary attack, this may take a while please wait.")
	with open(dictionary_file, 'r') as dictionary_list:
		for word in dictionary_list.read().split('\n'):
			key_string = []
			for i in range(len(cipher_text)):
				index = i % len(word)
				for k, v in key_mapper.items():
					if word[index] in v:
						key_string.append(k)

			deciphered_string = []
			for element in range(len(cipher_text)):
				if cipher_text[element].isalpha():
					num = ord(cipher_text[element])
					num += -key_string[element]

					if cipher_text[element].isupper():
						if num > ord('Z'):
							num -= 26
						elif num < ord('A'):
							num += 26

					elif cipher_text[element].islower():
						if num > ord('z'):
							num -= 26
						elif num < ord('a'):
							num += 26

					deciphered_string.append(chr(num))
				else:
					deciphered_string.append(cipher_text[element])


			if isEnglish("".join(deciphered_string), word_percentage=percent_match):
				return "Possible Match! --> Key: %s String: %s" % (word, "".join(deciphered_string))

	return "Message could not be deciphered, the key was not in the provided dictionary \
	or try reducing the word_percentage match value, the default is 55 percent."
			