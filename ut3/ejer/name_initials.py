"""
Dado un nombre y apellidos en formato "apellidos, nombre", obtenga las iniciales de dicha
persona pasadas a mayúsculas y con punto al final.
"""


def run(fullname: str) -> str:
    upper_name = fullname.upper()
    f_name_splitted = upper_name.split(", ")
    surname_splited = f_name_splitted[0].split()
    if len(surname_splited) == 2:
        f_name = f_name_splitted[1]
        name_splitted = f_name.split(" ")
        if len(name_splitted) == 2:
            name = name_splitted[0]
            s_name_1 = surname_splited[0]
            s_name_2 = surname_splited[1]
            initials = f"{name[0]}.{s_name_1[0]}.{s_name_2[0]}."
        else:
            name = f_name_splitted[1]
            s_name_1 = surname_splited[0]
            s_name_2 = surname_splited[1]
            initials = f"{name[0]}.{s_name_1[0]}.{s_name_2[0]}."
    elif len(surname_splited) == 1:
        name = f_name_splitted[1]
        s_name_1 = surname_splited[0]
        initials = f"{name[0]}.{s_name_1[0]}."

    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
