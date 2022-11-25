val1 = int(input("Introduzca el primer valor: "))
val2 = int(input("Introduzca el segundo valor: "))
operation = input("Introduzca la operación: ")

match operation:
    case "+":
        result = val1 + val2
    case "-":
        result = val1 - val2
    case "*":
        result = val1 * val2
    case "/":
        result = val1 / val2
    case _:
        print("Operación inválida")
        pass

if result is not None:
    print(f"{val1}{operation}{val2} = {result}")
