def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

# Get input from the user
plaintext = input("Enter the text to encrypt: ")

# Get the shift value from the user
shift = int(input("Enter the shift value: "))

# Encrypt the text
encrypted_text = caesar_cipher_encrypt(plaintext, shift)

# Output the encrypted text
print("Encrypted Text:", encrypted_text)
