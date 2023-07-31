import re

# 4. Escriba un programa en Python que determine si un email dado tiene el formato correcto.
email = """Los email correctos son colidom@outlook.com, colidom@gmail.com pero los incorrectos son colidom.outlook.com y colidom.gmail.com"""


def check_email(email):
    return re.findall(r"[a-zA-Z0-9._%+-]+@+[a-zA-Z0-9_%+-]+\.[a-zA-Z]+", email)


mail = check_email(email)
print(f"Correct emails finded: {mail} \n")
