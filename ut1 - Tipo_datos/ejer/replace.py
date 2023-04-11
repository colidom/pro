song = '''You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness'''

start_index = song.find('voices')
end_index = start_index + len('voices')

first_part = song[:start_index]
second_part = song[end_index:]
modified_song = first_part + 'sounds' + second_part

print(modified_song)
