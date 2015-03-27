import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'CryptographyKit',
  packages = ['Cryptokit', 'Cryptokit/helper_files'],
  version = '1.0.0',
  author = 'Marc Santiago',
  author_email = 'marcanthonysanti@gmail.com',
  url = 'https://github.com/marcsantiago/Cryptokit', 
  download_url = 'https://github.com/marcsantiago/Cryptokit/archive/master.zip', 
  keywords = ['Crytography', 'One Time Pad Encryption, Ceaser Cipher', 'vigenere cipher'],
  description = 'This package is intended to provided users with a quick and simple ways to perform\
  a one time pad encryption, ceaser cipher, or vigenere cipher.  It will work with python 2 or 3.', 
  long_description=read('README.txt'),
  classifiers = [],
)