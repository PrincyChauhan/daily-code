def count_words(text):
    words=text.split()
    return len(words)

text=(input("Enter a text: "))
print(count_words(text))
