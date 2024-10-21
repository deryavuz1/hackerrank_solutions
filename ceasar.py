def caesarCipher(s, k): 
    lowercase_alphabet = string.ascii_lowercase
    encrypted = []
    #k = k % 26 # shifts greater than 26
    
    for char in s:
        # check if the character is alpha-numeric
        if char.isalpha():
            # Pick the ASCII offset - if it's 65 - lowercase, uppercase 97
            offset = 65 if char.isupper() else 97
            # Shift character and wrap around the alphabet
            shifted_char = chr((ord(char) - offset + k) % 26 + offset)
            encrypted.append(shifted_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)
        
