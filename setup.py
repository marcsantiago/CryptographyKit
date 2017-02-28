import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'CryptographyKit',
  packages = ['Cryptokit', 'Cryptokit/helper_files'],
  version = '2.0.3',
  author = 'Marc Santiago',
  author_email = 'marcanthonysanti@gmail.com',
  url = 'https://github.com/marcsantiago/CryptographyKit',
  download_url = 'https://github.com/marcsantiago/CryptographyKit/archive/master.zip',
  keywords = ['Cryptography', 'One Time Pad Encryption, Caeser Cipher', 'Vigenere cipher'],
  description = 'This package is intended to provided users with a quick and simple way to perform\
  a one time pad encryption, Caeser cipher, or Vigenere cipher.  It will work with python 2 or 3.',
  long_description=read('README.txt'),
  classifiers = [],
)
