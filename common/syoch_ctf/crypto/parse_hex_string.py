def parse_hex_string(hex_string):
    data_hex = hex_string.replace("\n", "").replace(" ", "").strip().replace(":", "")
    data_bytes = bytes.fromhex(data_hex)

    data = int.from_bytes(data_bytes, "big")
    return data
