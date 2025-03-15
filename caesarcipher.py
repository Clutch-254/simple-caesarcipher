def matts_caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher.

    :param text: The input text to encrypt or decrypt.
    :param shift: The number of positions to shift each letter.
    :param mode: 'encrypt' or 'decrypt'.
    :return: The encrypted or decrypted text.
    """
    result = ""
    shift = shift % 26  # Ensure the shift is within 0-25

    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char  # Leave non-alphabetic characters unchanged
    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            encrypted_text = matts_caesar_cipher(text, shift, 'encrypt')
            print(f"Encrypted Text: {encrypted_text}")
        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            decrypted_text = matts_caesar_cipher(text, shift, 'decrypt')
            print(f"Decrypted Text: {decrypted_text}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()