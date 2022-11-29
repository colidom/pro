ALPHABET = "abcdefghijklmnopqrstuvwxyz"
text = "hello-world"

for char in text:
    if not char in ALPHABET:
        print("Non-alphabetic char found!")
        break
else:
    print("All chars are alphabetic")
