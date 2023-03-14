# **********************************
# ORDENANDO IDS EN UNA BASE DE DATOS
# **********************************


def sort_id(db=list[dict[int, str]]) -> list[dict[int, str]]:
    data = db.copy()

    sorted_list = []
    counter = 1
    for dic in data:
        dic["id"] = counter
        counter += 1
        sorted_list.append(dic)

    return sorted_list
