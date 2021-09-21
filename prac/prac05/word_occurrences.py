count_words={}
text=input("Text:")
word1=text.split()
for word in word1:
    if word in word1:
        value=count_words.get(word,0)
        count_words[word]=value+1
word1=list(count_words.keys())
for word in word1:
    print(f"{word}: {count_words[word]}")


