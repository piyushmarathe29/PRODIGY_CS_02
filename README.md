This project is a simple image encryption tool built using Python and the PIL (Pillow) library. It allows users to encrypt and decrypt images through pixel manipulation by applying a basic mathematical operation on each pixel's RGB values using a specified key

FEATURES
Encrypt Image: Modify pixel RGB values based on an encryption key.
Decrypt Image: Restore the original image by reversing the encryption process using the same key.
Command-Line Interface: A simple, user-friendly interface for encrypting and decrypting images.

Requirements
Python 3.x
PIL (Pillow) Library

How It Works
The tool manipulates each pixel's RGB values by adding the encryption key to the values during encryption.
During decryption, it subtracts the key from the pixel values to restore the original image.


