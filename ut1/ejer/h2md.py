html = '<h3>Cadenas de texto</h3>'

start_index_1 = html.find('<h')
end_index_2 = html.find('</h')

start_index_2 = start_index_1 + 3
heading = html[start_index_2 - 1]
heading_title = html[start_index_2 + 1 : end_index_2]

md_tag = '#' * int(heading)

markdown = f'{md_tag} {heading_title}'
print(markdown)
