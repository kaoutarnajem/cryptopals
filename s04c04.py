import binascii

# Fonction pour lire les lignes d'un fichier
def get_lines(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except IOError:
        print("error: couldn't open file")
        return None

# Fonction pour convertir une chaîne hexadécimale en binaire
def hex_to_binary(hex_str):
    try:
        return binascii.unhexlify(hex_str)
    except binascii.Error:
        print("error: invalid hex in file")
        return None

# Fonction pour déchiffrer un texte chiffré avec une clé XOR à caractère unique
def xor_single_byte(data, key):
    return bytes([b ^ key for b in data])

# Fonction pour évaluer le score de chaque ligne chiffrée et détecter la clé
def detect_xor_single_byte(buffers):
    scores = []
    common_chars = b"ETAOIN SHRDLU"
    for index, buffer in enumerate(buffers):
        for key in range(256):
            decrypted = xor_single_byte(buffer, key)
            if all(chr(c).isprintable() for c in decrypted):
                score = sum([decrypted.count(c) for c in common_chars])
                scores.append((index, key, score, decrypted))
    return sorted(scores, key=lambda x: x[2], reverse=True)

# Fonction principale
def detect_single_byte_xor(filename):
    file_lines = get_lines(filename)
    if not file_lines:
        return 2

    buffers = [hex_to_binary(line) for line in file_lines if hex_to_binary(line)]

    scores = detect_xor_single_byte(buffers)
    if not scores:
        return 2

    winning_score = scores[0]
    index, key, score, decrypted = winning_score

    hex_str = file_lines[index]
    key_str = hex(key)

    print("top result:")
    print(f"line number: {index + 1}")
    print(f"hex string: {hex_str}")
    print(f"key: {key_str} score: {score}")
    print(f"xor message: {decrypted.decode()}")

    return 0

# Chemin du fichier
file_path = r"C:\Users\Lenovo\OneDrive\Bureau\file.txt"

# Appel de la fonction principale avec le chemin de fichier
detect_single_byte_xor(file_path)
