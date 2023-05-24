import re

# 2. Escriba un programa en Python que encuentre todas las URLs en un texto dado.

url = """Aprende Python es una web para aprender a programar en Python, puedes acceder mediante los enlaces 
https://www.aprendepython.es, http://www.aprendepython.es, https://aprendepython.es, http://aprendepython.es 
pero no desde 
httpsx://www.aprendepython.es, httpx://www.aprendepython.es, httpsx://aprendepython.es, httpx://aprendepython.es 
"""
regular_expression = r"https?:\/\/(?:www\.)?[a-zA-Z0-9]+\.[a-z]\S"


def valid_url(url):
    return re.findall(regular_expression, url)


url = valid_url(url)
print(f"Url finded: {url} \n")
