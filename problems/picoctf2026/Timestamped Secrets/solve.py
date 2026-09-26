from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

cipher = bytes.fromhex(
    "77c36bef0245021f9d9b7e396b52d2efbdbe6f8e4b79146e5d87c93416453b5f"
)
timestamp = 1770242597

key = sha256(str(timestamp).encode()).digest()[:16]

aes = AES.new(key, AES.MODE_ECB)
message = unpad(aes.decrypt(cipher), AES.block_size)
print(message.decode())
