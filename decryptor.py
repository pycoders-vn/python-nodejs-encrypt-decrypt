from Crypto import Random
from Crypto.Cipher import AES
import json 

secret_key = '7yBFR8L5wy42Pr9SAnEVp7PuKPQX7W3P'

BS = 16
def pad(data):
    padding = BS - len(data) % BS
    return data + padding * chr(padding)

def unpad(data):
    return data[0:-ord(data[-1])]

def decrypt_node(hex_data, key=secret_key, iv='0'*16):
    try:
        data = bytes.fromhex(hex_data)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypttext = cipher.decrypt(data).decode('utf-8')
        return decrypttext
    except:
        raise Exception("Can not decrypt please check secret key!")

# def encrypt_node(data, key='0'*32, iv='0'*16):
#     aes = AES.new(key, AES.MODE_CBC, iv)
#     return aes.encrypt(pad(data)).encode('hex')

# Example 1: 
# print(encrypt_node('this-needs-to-be-encrypted'))
# print(decrypt_node('b88e5f69c7bd5cd67c9c12b9ad73e8c1ca948ab26da01e6dad0e7f95448e79f4'))

# Example 2:
# Read encrypted data 
encrypted = ''
with open('encrypted_by_node.txt', 'r') as f:
    encrypted = f.read()

# Save decrypted data to json
decrypted = decrypt_node(encrypted)
with open('decrypted_by_python.json', 'w') as f:
    f.write(json.loads(decrypted))

print(decrypted)
