person1 = "piedra"
person2 = "papel"

if person1 == person2:
    print("Empate")
elif person1 == "piedra" and person2 == "tijera":
    print("Piedra rompe Tijera")
elif person1 == "tijera" and person2 == "piedra":
    print("Piedra rompe Tijera")
elif person1 == "tijera" and person2 == "papel":
    print("Tijera corta papel")
elif person1 == "papel" and person2 == "tijera":
    print("Tijera corta papel")
elif person1 == "papel" and person2 == "piedra":
    print("Papel envuelve piedra")
elif person1 == "piedra" and person2 == "papel":
    print("Papel envuelve piedra")
