# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
    result = []
    for hex_code in hex_codes:
        decoded = int(hex_code, 16)
        chars = chr(decoded)
        result.append(chars)
        text = "".join(result)
    return text


if __name__ == "__main__":
    run(["1f49a", "2728", "1f389", "1f3c6"])
