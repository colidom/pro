def getint_recursive():
    try:
        value = int(input("Give me an integer number: "))
    except ValueError:
        print("Not a valid integer. Try it again!")
        getint_recursive()

    else:
        print(f"{value}")


getint_recursive()
