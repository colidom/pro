months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month = 11

if month in months[0:3]:
    print("Primer trimestre")
elif month in months[3:6]:
    print("Segundo trimestre")
elif month in months[6:9]:
    print("Tercer trimestre")
elif month in months[9:12]:
    print("Cuarto trimestre")
