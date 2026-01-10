# =========================================
# ZADANIE 3 – BAG OF WORDS
# WERSJA BEZ NLTK DOWNLOAD / SSL
# =========================================

import re
import string
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud


# =========================================
# a) Wczytanie artykułu
# =========================================

with open("article.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("Długość oryginalnego tekstu:", len(text))


# =========================================
# b) Tokenizacja (REGEX)
# =========================================
tokens = re.findall(r"\b[a-zA-Z]+\b", text.lower())
print("Liczba słów po tokenizacji:", len(tokens))


# =========================================
# c) Usunięcie stop-words (lista ręczna)
# =========================================

stop_words = {
    "the", "and", "is", "in", "to", "of", "that", "it", "on", "for", "with",
    "as", "was", "were", "by", "are", "this", "be", "or", "from", "at",
    "an", "which", "but", "not", "have", "has", "had"
}

tokens_no_stop = [
    word for word in tokens if word not in stop_words
]

print("Liczba słów po usunięciu stop-words:", len(tokens_no_stop))


# =========================================
# d) Dodatkowe stop-words (ręcznie)
# =========================================

custom_stopwords = {"said", "also", "one", "two", "new", "would", "could"}
tokens_clean = [
    word for word in tokens_no_stop if word not in custom_stopwords
]

print("Liczba słów po dodatkowych stop-words:", len(tokens_clean))


# =========================================
# e) Lematyzacja / stemming
# =========================================
print("Lematyzacja: pominięta (brak zasobów NLTK – wersja offline)")


# =========================================
# f) Bag of Words + wykres TOP 10
# =========================================

bow = Counter(tokens_clean)
top_10 = bow.most_common(10)

words, counts = zip(*top_10)

plt.figure(figsize=(10, 5))
plt.bar(words, counts)
plt.title("10 najczęściej występujących słów")
plt.xlabel("Słowo")
plt.ylabel("Liczba wystąpień")
plt.show()


# =========================================
# g) Word Cloud
# =========================================

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate_from_frequencies(bow)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud – Bag of Words")
plt.show()
