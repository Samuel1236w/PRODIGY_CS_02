 OVERVIEW   
This is a Python-based tool that allows you to encrypt and decrypt images using a simple key-based method. The tool manipulates the pixel values of the image to encrypt it, ensuring that only users with the correct key can decrypt and restore the original image.

FEATURES 

   - Image Encryption: Modify pixel values of an image to produce an encrypted, scrambled version.
   - Image Decryption: Reverse the modifications to restore the original image using the same encryption key.
   - Key-Based Security: Ensures that only users with the correct key can decrypt the image.

INSTALLATION 

a. Clone the Repository:

   git clone https://github.com/your-username/image-encryption-tool.git
   cd image-encryption-tool

b. Install Dependencies:
   Ensure you have Python installed on your system. Install the required libraries:

    pip install pillow numpy

c. Run the Program:
   Execute the script to start encrypting or decrypting images:

    python image_encryptor.py

HOW IT WORKS

a.  Encryption

   - Select the option to encrypt an image.
   - Provide the path to the image file you want to encrypt.
   - Specify the output path to save the encrypted image.
   - Enter an encryption key (integer) that will be used to modify the pixel values.

b.  Decryption

   - Select the option to decrypt an image.
   - Provide the path to the encrypted image file.
   - Specify the output path to save the decrypted image.
   - Enter the same key used during encryption to restore the original image.

  NOTE

  - Ensure that the same key is used for both encryption and decryption.
  - This tool supports image files in formats like JPG and PNG



