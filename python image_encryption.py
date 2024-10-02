from PIL import Image

# Function to encrypt an image using pixel manipulation
def encrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Get image data
    pixels = img.load()
    
    # Get dimensions of the image
    width, height = img.size
    
    # Encrypt the image by modifying the pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            
            # Apply a basic operation (e.g., add key value to RGB)
            r_encrypted = (r + key) % 256
            g_encrypted = (g + key) % 256
            b_encrypted = (b + key) % 256
            
            # Set the encrypted pixel value back
            pixels[x, y] = (r_encrypted, g_encrypted, b_encrypted)
    
    # Save the encrypted image
    img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

# Function to decrypt an image
def decrypt_image(image_path, key, output_path):
    # Open the encrypted image
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Get image data
    pixels = img.load()
    
    # Get dimensions of the image
    width, height = img.size
    
    # Decrypt the image by reversing the pixel manipulation
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            
            # Reverse the operation (subtract key from RGB values)
            r_decrypted = (r - key) % 256
            g_decrypted = (g - key) % 256
            b_decrypted = (b - key) % 256
            
            # Set the decrypted pixel value back
            pixels[x, y] = (r_decrypted, g_decrypted, b_decrypted)
    
    # Save the decrypted image
    img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

# Main function
def main():
    while True:
        print("\nImage Encryption Tool")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            image_path = input("Enter the path of the image to encrypt: ")
            key = int(input("Enter the encryption key (integer): "))
            output_path = input("Enter the path to save the encrypted image: ")
            encrypt_image(image_path, key, output_path)
        
        elif choice == '2':
            image_path = input("Enter the path of the image to decrypt: ")
            key = int(input("Enter the decryption key (integer): "))
            output_path = input("Enter the path to save the decrypted image: ")
            decrypt_image(image_path, key, output_path)
        
        elif choice == '3':
            print("Exiting the tool.")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
