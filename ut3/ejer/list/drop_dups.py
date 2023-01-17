words = ["this", "is", "a", "real", "real", "real", "story"]
non_repeated_words = []

for word in words:
    if word not in non_repeated_words:
        non_repeated_words.append(word)
print(non_repeated_words)
