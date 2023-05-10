def getint():
    while True:
        try:
            value = int(input("Give me an integer number: "))
        except ValueError:
            print("Not a valid integer. Try it again!")
        else:
            print(f"{value}")
            break


getint()
