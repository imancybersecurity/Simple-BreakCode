def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    # Get input from the user
    encrypted_text = input("Enter the encrypted text: ")
    shift = int(input("Enter the shift value: "))

    # Decrypt the text
    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

    # Output the decrypted text
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
