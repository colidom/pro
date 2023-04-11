CONTROL_LETTER = 'TRWAGMYFPDXBNJZSQVHLCKE'

dni = int(input("Inserte si DNI: "))
control_digit = CONTROL_LETTER[dni % 23]

print(f"Su número NIF es: {dni}-{control_digit}")
