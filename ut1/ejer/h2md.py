html = '<h3>Cadenas de texto</h3>'
html_start_tag = html.replace('<h3>', '#' * 3)
print(f"{html_start_tag[:-5]}")
