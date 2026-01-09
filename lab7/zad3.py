import nltk
import string
import matplotlib.pyplot as plt

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from wordcloud import WordCloud


# Jednorazowe pobranie zasobów NLTK
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")



# a) Wczytanie artykułu
with open("article.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("Długość oryginalnego tekstu:", len(text))


# b) Tokenizacja
tokens = word_tokenize(text.lower())
print("Liczba słów po tokenizacji:", len(tokens))


# c) Usunięcie stop-words
stop_words = set(stopwords.words("english"))

tokens_no_stop = [
    word for word in tokens
    if word not in stop_words and word not in string.punctuation
]

print("Liczba słów po usunięciu stop-words:", len(tokens_no_stop))

# d) Dodatkowe stop-words (ręcznie)
custom_stopwords = ["said", "also", "one", "two", "new", "would"]
stop_words.update(custom_stopwords)

tokens_clean = [
    word for word in tokens_no_stop
    if word not in stop_words
]

print("Liczba słów po dodatkowych stop-words:", len(tokens_clean))


# e) Lematyzacja
lemmatizer = WordNetLemmatizer()

lemmatized_tokens = [
    lemmatizer.lemmatize(word)
    for word in tokens_clean
]

print("Liczba słów po lematyzacji:", len(lemmatized_tokens))
print("Użyty lematyzer: WordNetLemmatizer")


# f) Bag of Words + wykres 10 najczęstszych
bow = Counter(lemmatized_tokens)

top_10 = bow.most_common(10)

words, counts = zip(*top_10)

plt.figure(figsize=(10, 5))
plt.bar(words, counts)
plt.title("10 najczęściej występujących słów")
plt.xlabel("Słowo")
plt.ylabel("Liczba wystąpień")
plt.show()


# g) Word Cloud
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
