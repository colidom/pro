"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    upper_name = fullname.upper()
    f_name_splitted = upper_name.split(", ")
    surname_split = f_name_splitted[0].split()
    f_name_length = len(f_name_splitted)
    if f_name_length == 3:
        name = f_name_splitted[1]
        s_name_1 = f_name_splitted[0]
        s_name_2 = f_name_splitted[1]
        initials = f"{name[0]}.{s_name_1[0]}.{s_name_2[0]}."

    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
