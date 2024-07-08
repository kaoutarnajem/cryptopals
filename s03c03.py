def xor_decrypt(hex_string): 

    ciphertxt_bytes = bytes.fromhex(hex_string) 
  
    def score_txt(text): 

        # Fréquence des lettres en anglais 

        frequencies = { 

            'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 

            'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 

            'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 

            'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 

            'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 'z': 0.00074, 

            ' ': 0.13000  

        } 

        return sum([frequencies.get(chr(byte), 0) for byte in text.lower()]) 

    # Décryptage en essayant toutes les clés possibles (0-255) 
    good_score = 0 
    good_key = None 
    decrypted_txt = None 

    for P in range(256): 

        #  XOR avec la clé actuelle 

        text_decrypted = bytes([byte ^ P for byte in ciphertxt_bytes]) 

        # Calculer le score du texte 

        score = score_txt(text_decrypted) 

        # Si le score est meilleur, mettre à jour le meilleur score et le message déchiffré 

        if score > good_score: 

            good_score = score 

            good_key = P 

            decrypted_txt = text_decrypted 

    return good_key, decrypted_txt 

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736" 

key, message = xor_decrypt(hex_string) 

print(f"Key is: {key}") 

print(f"Decrypted text is: {message.decode('latin1')}") # .decode('latin1') convertit cette séquence d'octets en une chaîne de caractères (str) en utilisant l'encodage 'latin1' 
      

     

    
