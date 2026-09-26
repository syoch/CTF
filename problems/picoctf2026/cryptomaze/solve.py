from Crypto.Cipher import AES

taps = [63, 61, 60, 58]
cipher_msg = bytes.fromhex(
    "8f0e6d0f5b0dc1db201948b9e0cebd8fe0ab34ea7ca27b6e6277e35179203fd438338e7e04fbddef0c6260a4eb758417"
)


def lfsr_step(state: int):
    feedback = 0
    for t in taps:
        feedback ^= (state >> (63 - t)) & 1

    out = (state >> 63) & 1
    state = ((state << 1) & ((1 << 64) - 1)) | feedback
    return state, out


def main():
    state = 0b0010010111101100100101101001010101001101100010111100010001011011

    key = 0
    for _ in range(128):
        state, out = lfsr_step(state)
        key = (key << 1) | out

    key = key.to_bytes(16, "big")

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(cipher_msg)
    print(decrypted)


if __name__ == "__main__":
    main()
