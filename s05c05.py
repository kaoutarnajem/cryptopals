def repeating_key_xor(plaintext, key): 

    plaintext_bytes = plaintext.encode()   

    key_bytes = key.encode()  # Convert the key to bytes 

    ciphertext_bytes = bytearray() 

    for i in range(len(plaintext_bytes)): 

        ciphertext_byte = plaintext_bytes[i] ^ key_bytes[i % len(key_bytes)]   

        ciphertext_bytes.append(ciphertext_byte) 

 

    return ciphertext_bytes.hex()  # Returns the ciphertext to hexadecimal 


plaintext = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal" 

key = "ICE" 

ciphertext = repeating_key_xor(plaintext, key) 

print("Texte chiffré (hex):", ciphertext) 
