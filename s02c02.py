def fixed_xor(hex_string1, hex_string2):
    # Convertir les chaînes hexadécimales en données binaires
    binary1 = bytes.fromhex(hex_string1)
    binary2 = bytes.fromhex(hex_string2)
    
    # Initialiser un tableau pour stocker le résultat de XOR
    result = bytearray()
    
    # Réaliser l'opération XOR octet par octet
    for b1, b2 in zip(binary1, binary2):
        result.append(b1 ^ b2)  # XOR des octets correspondants et ajout au résultat
    
    # Convertir le résultat en chaîne hexadécimale
    hex_result = result.hex()
    
    return hex_result

# Exemple d'utilisation
hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

# Appel de la fonction pour obtenir le résultat
resultat_xor = fixed_xor(hex_string1, hex_string2)
print(resultat_xor)
