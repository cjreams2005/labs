def caesar_cipher_encrypt(text, shift):
    return ''.join(map(lambda c: shift_char(c, shift), text))

def caesar_cipher_decrypt(text, shift):
    return ''.join(map(lambda c: shift_char(c, -shift), text))

def shift_char(c, shift):
    if c.isalpha():
        start = ord('A') if c.isupper() else ord('a')
        return chr(start + (ord(c) - start + shift) % 26)
    return c

print(caesar_cipher_encrypt("Hello, World!", 3))

print(caesar_cipher_decrypt("Khoor, Zruog!", 3))
