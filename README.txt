AUTHOR: Marc Santiago 
EMAIL: marcanthonysanti@gmail.com 

This kit is intended to provided users with quick and simple forms of encryptions.  Some modules like
HideMessageInImage and CaesarCipher, while not very strong forms of encryption are provided for the
sake of having them easily available and for fun :-).

USAGE:
External Modules Required
-------------------------------------------------
-------------------------------------------------
pyminizip, PIL, and easygui
All these modules can be installed via the pip command

[pip install pyminizip] or [pip3 install pyminizip]
[pip install Pillow]    or [pip3 install Pillow]
[pip install easygui]   or [pip3 install easygui]


Import Modules
-------------------------------------------------
-------------------------------------------------
from Cryptokit.OneTimePadEncryption import encrypt_data, decrypt_data
from Cryptokit.CaesarCipher import c_encipher, c_decipher, brute_force_decrypt
from Cryptokit.VigenereCipher import v_encipher, v_decipher, v_dictionaryattack
from Cryptokit.HideMessageInImage import hide_or_show_message


Description of Methods:
-------------------------------------------------
-------------------------------------------------

Module --> OneTimePadEncryption
-------------------------------

encrypt_data(plain_text, string_file_mode=False) --> Takes plain text as either a string
or a text document and returns a key file and  encrypted message file. Date times are used to match
the key file with the encrypted message file.

decrypt_data(key, encrypted_string, key_file_mode=False, string_file_mode=False)
--> Takes a key and an enencrypted message as either a text document or a file. It will return the
plain text document assuming the right key is supplied.

Module --> CaesarCipher
-------------------------------

c_encipher(plain_text, key, plain_text_file_mode=False) --> Plain text is shifted up by the key
provided.  The key must be in the range of 1-26.

c_decipher(cypher_text, key, cypher_text_file_mode=False) --> Cipher text is shifted by the key
provided.  The key must be in range of 1-26. The key must be the same key used to encipher other
wise garbage data will be returned.

brute_force_decrypt(cypher_text, cypher_text_file_mode=False) --> This will attempt to return the
key used and the plain text translation of the enciphered text.

Module --> VigenereCipher
-------------------------------

v_encipher(plain_text, key, file_mode=False) --> Plain text is enciphered using the given key
provided key. The key that is provided must be in a string containing only English characters.

v_decipher(cipher_text, key, file_mode=False) --> Cipher text is deciphered using the key that was
used to encipher the message.  The key that is provided must be in a string containing only English
characters.

v_dictionaryattack(cipher_text, dictionary_file="helper_files/dictionary.txt", file_mode=False,
percent_match=55) --> Function that takes cipher text either as a string or as a text file and trys
and returns the plain text message. Things to note; the dictionary_file argument is passed a default
dictionary, which is used to try and crack the cipher text.  The percent_match arugument is used to
specify how close the deciphered message has to be to English, see the detectEnglish module located
in the helper_files folder for more information.


Module --> HideMessageInImage
-------------------------------

hide_or_show_message() --> This will prompt the user to type in a message.  It will return a png file with
your message hidden inside. Run the function again to if you want to decrypt a png file.


COMMAND LINE TOOLS HAVE BEEN PROVIDED FOR CONVENIENCE: 
------------------------------------------------------
------------------------------------------------------

FILE NAME: otp_utility.py 
FILE LOCATION: https://github.com/marcsantiago/CryptographyKit/blob/master/otp_utility.py

FILE NAME: c_cipher_utility.py 
FILE LOCATION: https://github.com/marcsantiago/CryptographyKit/blob/master/c_cipher_utility.py

FILE NAME: v_cipher_utility.py 
FILE LOCATION: https://github.com/marcsantiago/CryptographyKit/blob/master/v_cipher_utility.py
