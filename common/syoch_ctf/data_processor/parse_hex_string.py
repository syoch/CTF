def parse_hex_string_as_int(hex_string: str) -> int:
    """16進数文字列をバイト列に変換し、それを整数に変換する

    Args:
        hex_string (str): 16進数文字列

    Returns:
        int: 変換された整数
    """
    data_hex = hex_string.replace("\n", "").replace(" ", "").strip().replace(":", "")
    data_bytes = bytes.fromhex(data_hex)

    data = int.from_bytes(data_bytes, "big")
    return data
