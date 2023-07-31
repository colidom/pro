# ******************
# SUMA CRIPTOGRÁFICA
# ******************
from pathlib import Path

CRYPTO_HASH = {
    "sd": "-",
    "vo": ".",
    "ax": "0",
    "gh": "1",
    "hj": "2",
    "uv": "3",
    "ws": "4",
    "pk": "5",
    "et": "6",
    "mc": "7",
    "rh": "8",
    "wb": "9",
}


def run(crypto_path: str) -> float:
    numbers = []
    with open(crypto_path, "r") as f:
        for line in f:
            buffer = []
            cdata = line.strip()
            for i in range(0, len(cdata), 2):
                code = cdata[i : i + 2]
                decoded_value = CRYPTO_HASH.get(code, "")
                buffer.append(decoded_value)
            fnumber = "".join(buffer)
            numbers.append(float(fnumber))
    sum_cr = sum(numbers)
    return sum_cr


if __name__ == "__main__":
    run("data/sum_crypto/data1.crypto")
