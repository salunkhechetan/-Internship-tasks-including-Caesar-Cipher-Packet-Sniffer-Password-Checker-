from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Open image
    img = Image.open(input_path)
    pixels = img.load()

    # Encrypt by modifying pixel values
    for i in range(img.size[0]):      # width
        for j in range(img.size[1]):  # height
            r, g, b = pixels[i, j]
            # Simple encryption: add key and wrap around 256
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")


def decrypt_image(input_path, output_path, key):
    # Open image
    img = Image.open(input_path)
    pixels = img.load()

    # Decrypt by reversing the operation
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")


# Example usage
if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").lower()
    input_file = input("Enter input image path: ")
    output_file = input("Enter output image path: ")
    key = int(input("Enter numeric key (e.g., 50): "))

    if choice == "e":
        encrypt_image(input_file, output_file, key)
    elif choice == "d":
        decrypt_image(input_file, output_file, key)
    else:
        print("Invalid choice. Please enter E or D.")