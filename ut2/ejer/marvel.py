""" 
Escriba un programa que permita adivinar un personaje de Marvel en base a las tres preguntas siguientes:
¿Puede volar?
¿Es humano?
¿Tiene máscara?
"""
can_fly = True
is_human = True
has_mask = False

if can_fly:
    if is_human:
        if has_mask:
            print("Ironman")
        else:
            print("Captain Marvel")
    else:
        if has_mask:
            print("Ronan Accuser")
        else:
            print("Vision")
else:
    if is_human:
        if has_mask:
            print("Spiderman")
        else:
            print("Hulk")
    else:
        if has_mask:
            print("Black Bolt")
        else:
            print("Thanos")
