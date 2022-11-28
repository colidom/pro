word = "Supercalifragilisticoespialidoso"
vowels = ["a", "e", "i", "o", "u"]
n_vowels = 0

for letter in word:
    if letter in vowels:
        n_vowels += 1
print(n_vowels)
