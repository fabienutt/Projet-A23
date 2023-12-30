import base64

hex_string = "00000241B77283D0"
binary_data = bytes.fromhex(hex_string)
base64_encoded = base64.b64encode(binary_data).decode('utf-8')

print(base64_encoded)
