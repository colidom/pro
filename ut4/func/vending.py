# Ejercicio vending
""" 
            actículos
VENDING     precios
            pedido
            dinero
"""
articles = [
    {"id": 1, "name": "Coca", "price": 1.9, "stock": 10},
    {"id": 2, "name": "Fanta", "price": 1.9, "stock": 10},
    {"id": 3, "name": "Tirma", "price": 1.5, "stock": 10},
    {"id": 4, "name": "Escaldón", "price": 2.0, "stock": 5},
]


def vending(articles):

    # entrada = input("Elija un producto: ")
    print("\n| id | Stock | Nombre | Precio |")
    for article in articles:
        formato(article)


def formato(article):
    print(
        f"   {article['id']}    {article['stock']}      {article['name']}    {article['price']}€"
    )


vending(articles)
