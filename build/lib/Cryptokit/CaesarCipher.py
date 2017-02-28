#!/usr/bin/env python
"""This module is designed to provide users Caesar Cipher tools."""
from __future__ import division, absolute_import, print_function, unicode_literals
__author__ = 'marcsantiago'

from helper_files import detectEnglish

try:
	from future_builtins import *
except ImportError:
	pass

try:
	input = raw_input
	range = xrange
except NameError:
	pass

def c_encipher(plain_text, key, file_mode=False):
	"""The encipher module takes plain text as enter a passed string
	argument or a basic .txt file.  A key must also be provide.  Since, this
	if a Caesar Cipher the key that is provide must be in the range of 1 through 26"""
	try:
		assert type(key) == type(int())
	except AssertionError as e:
		print("Entered key must be a an integer and a string: %s" % str(e))

	try:
		assert key > 0 and key < 27
	except:
		print("Key must be greater than 0 and less than 27.")

	translated = []

	if file_mode:
		with open(plain_text, 'r') as in_data:
			plain = in_data.read()
	else:
		plain = plain_text

	for ch in plain:
		if ch.isalpha():
			num = ord(ch)
			num += key

			if ch.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26

			elif ch.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated.append(chr(num))
		else:
			translated.append(ch)

	answer = input("Write data to file? [y], [n]\n")

	if answer.lower() in ["yes", "y"]:
		with open("enciphered_caesar.txt", 'w') as data:
			data.write("".join(translated))
			return "".join(translated)
	else:
		return "".join(translated)

def c_decipher(cypher_text, key, file_mode=False):
	"""The decipher module takes cypher text as enter a passed string
	argument or a basic .txt file.  A key must also be provide.  Since, this
	if a Caesar Cipher the key that is provide must be in the range of 1 through 26"""
	try:
		assert type(key) == type(int())
	except AssertionError as e:
		print("Entered key must be a an integer and a string: %s" % str(e))

	try:
		assert 0 < key < 27
	except:
		print("Key must be greater than 0 and less than 27.")

	key = -key

	translated = []

	if file_mode:
		with open(cypher_text, 'r') as in_data:
			plain = in_data.read()
	else:
		plain = cypher_text

	for ch in plain:
		if ch.isalpha():
			num = ord(ch)
			num += key

			if ch.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif ch.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated.append(chr(num))
		else:
			translated.append(ch)

	answer = input("Write data to file? [y], [n]\n")
	if answer.lower() in ["yes", "y"]:
		with open("deciphered_caesar.txt", 'w') as data:
			data.write("".join(translated))
			return "".join(translated)
	else:
		return "".join(translated)

def brute_force_decrypt(cypher_text, file_mode=False):
	"""This method trys all the possible keys on a cyphered text and returns the
	key and plain text string.  It does this using the imported dictionary module, which
	is a modified version of http://inventwithpython.com/hacking (BSD Licensed)'s dictionary module.
	If an English plaintext is not found all 26 garbage keys will be printed for you to double check."""
	if file_mode:
		with open(cypher_text, 'r') as in_data:
			cypher = in_data.read()
	else:
		cypher = cypher_text

	for key in range(1, 27):
		key = -key
		translated = []
		for ch in cypher:
			if ch.isalpha():
				num = ord(ch)
				num += key
				if ch.isupper():
					if num > ord('Z'):
						num -= 26
					elif num < ord('A'):
						num += 26
				elif ch.islower():
					if num > ord('z'):
						num -= 26
					elif num < ord('a'):
						num += 26

				translated.append(chr(num))
			else:
				translated.append(ch)

		if detectEnglish.isEnglish("".join(translated)):
			return "Key: %s String: %s" % (abs(key), "".join(translated))
