# Caesar Cipher Program

## Description
This is a simple Python program that implements the Caesar Cipher encryption technique. The Caesar Cipher is one of the oldest and simplest forms of encryption, where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features
- Encrypt plaintext messages using a specified shift value
- Decrypt ciphertext messages using the same shift value
- Preserves case (uppercase/lowercase) of the original text
- Maintains non-alphabetic characters (numbers, spaces, punctuation) unchanged
- Interactive command-line interface

## How to Use

1. Run the program: `python caesar_cipher.py`
2. Choose from the available options:
   - Option 1: Encrypt a message
   - Option 2: Decrypt a message
   - Option 3: Exit the program
3. Follow the prompts to enter your text and shift value
4. View the encrypted or decrypted result

## Examples

### Encryption
```
Enter the text to encrypt: Hello, World!
Enter the shift value (integer): 3
Encrypted Text: Khoor, Zruog!
```

### Decryption
```
Enter the text to decrypt: Khoor, Zruog!
Enter the shift value (integer): 3
Decrypted Text: Hello, World!
```

## Technical Details
- The shift value is automatically adjusted to be between 0-25 (modulo 26)
- The algorithm maintains the original case of each letter
- Non-alphabetic characters remain unchanged
- The same function (`matts_caesar_cipher`) handles both encryption and decryption by adjusting the direction of the shift

## Requirements
- Python 3.x

## Author
Matthew Bethwel Gwada

## Note
This implementation is intended for educational purposes and does not provide secure encryption for sensitive data.
