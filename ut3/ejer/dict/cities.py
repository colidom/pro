# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    cities = {}
    list_cities = cinfo.split(";")
    for city_popul in list_cities:
        cities_and_popul = city_popul.replace(":", ",")
        cities = 

    return cities


if __name__ == "__main__":
    run("Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000")
