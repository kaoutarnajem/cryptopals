import base64

# Given hex string
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Step 1: Convert hex to raw bytes
raw_bytes = bytes.fromhex(hex_string)

# Step 2: Encode raw bytes in base64
base64_encoded = base64.b64encode(raw_bytes)

# Convert base64 bytes to string for pretty-printing
base64_string = base64_encoded.decode()

print(base64_string)
