age = 34
weight = 81
heartbeat = 70
platelets = 150000

if age >= 18 and age <= 65:
    if weight > 50:
        if heartbeat >= 50 and heartbeat <= 110:
            print("Es usted apto para donar sangre")
        else:
            print("No cumple ninguno de los requisitos para donar sangre")
    else:
        print("Su peso es demasiado bajo, no puede donar sangre")
else:
    print("NO está en edad de donar sangre, edades comprendidas de 18 a 65 años de edad")
