def detect_ecb_ciphertext(filename: str) -> str:
    with open(filename, 'r') as f:
        hex_lines = f.readlines()
    
    def has_repeated_blocks(hex_data: str, block_size: int = 16) -> bool:
        ciphertext = bytes.fromhex(hex_data.strip())
        blocks = [ciphertext[i:i + block_size] for i in range(0, len(ciphertext), block_size)]
        return len(blocks) != len(set(blocks))
    
    for line in hex_lines:
        if has_repeated_blocks(line):
            return line.strip()
    
    return None

if __name__ == "__main__":
    filename =r"C:\Users\hp\Desktop\fich.txt"  
    ecb_ciphertext = detect_ecb_ciphertext(filename)
    if ecb_ciphertext:
        print(f"Detected ECB ciphertext: {ecb_ciphertext}")
    else:
        print("No ECB ciphertext detected.")
