from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    """
    Encrypts an image by modifying its pixel values using a key.

    Parameters:
    - input_image_path (str): Path to the input image file
    - output_image_path (str): Path to save the encrypted image
    - key (int): Key used for encryption (must be the same for decryption)

    Returns:
    - None
    """
    # Open the image and convert it to RGB mode (to handle all images uniformly)
    img = Image.open(input_image_path).convert('RGB')
    img_array = np.array(img)  # Convert image to numpy array for pixel manipulation

    # Encrypt: Add the key to each pixel value (mod 256 to ensure valid pixel range)
    encrypted_array = (img_array + key) % 256

    # Convert the modified array back to an image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_image_path)  # Save the encrypted image
    print(f"Image successfully encrypted and saved as {output_image_path}")


def decrypt_image(encrypted_image_path, output_image_path, key):
    """
    Decrypts an image encrypted with the same key by reversing the pixel modifications.

    Parameters:
    - encrypted_image_path (str): Path to the encrypted image file
    - output_image_path (str): Path to save the decrypted image
    - key (int): Key used for decryption (must be the same as the encryption key)

    Returns:
    - None
    """
    # Open the encrypted image
    img = Image.open(encrypted_image_path).convert('RGB')
    img_array = np.array(img)  # Convert image to numpy array

    # Decrypt: Subtract the key from each pixel value (mod 256 to ensure valid pixel range)
    decrypted_array = (img_array - key) % 256

    # Convert the modified array back to an image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_image_path)  # Save the decrypted image
    print(f"Image successfully decrypted and saved as {output_image_path}")


# Main function to interact with the user
def main():
    """
    Main function to handle user input for encryption and decryption.
    """
    print("Welcome to the Image Encryption Tool!")
    choice = input("Do you want to (1) Encrypt or (2) Decrypt an image? Enter 1 or 2: ")

    if choice == "1":
        input_path = input("Enter the path to the image you want to encrypt: ")
        output_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter an encryption key (integer): "))
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        input_path = input("Enter the path to the encrypted image: ")
        output_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the decryption key (must match the encryption key): "))
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice. Please run the program again.")


# Execute the main function when the script is run
if __name__ == "__main__":
    main()
