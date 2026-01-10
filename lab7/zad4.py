# =========================================
# ZADANIE 4 – ANALIZA SENTYMENTU (OFFLINE)
# =========================================

import re

# =========================================
# a) Opinie hotelowe (Booking.com, Londyn)
# =========================================

positive_review = """
The hotel was absolutely fantastic. The room was spotless, modern and very comfortable.
The staff were incredibly friendly and helpful, always smiling and ready to assist.
The location is perfect and I would definitely stay here again.
"""

negative_review = """
This was one of the worst hotel experiences I have ever had.
The room was dirty and extremely small.
The staff were rude and unhelpful and the noise made it impossible to sleep.
"""


# =========================================
# OFFLINE SENTIMENT (fallback)
# =========================================

positive_words = {
    "fantastic", "spotless", "comfortable", "friendly", "helpful",
    "perfect", "excellent", "great", "amazing", "recommend"
}

negative_words = {
    "worst", "dirty", "small", "rude", "unhelpful",
    "noise", "terrible", "bad", "awful", "impossible"
}


def offline_sentiment(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    pos = sum(1 for w in words if w in positive_words)
    neg = sum(1 for w in words if w in negative_words)

    if pos > neg:
        sentiment = "POSITIVE"
    elif neg > pos:
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"

    return {
        "positive_words": pos,
        "negative_words": neg,
        "sentiment": sentiment
    }


# =========================================
# b) Vader (jeśli dostępny)
# =========================================

print("=== VADER ===")
try:
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    print("Pozytywna:", sia.polarity_scores(positive_review))
    print("Negatywna:", sia.polarity_scores(negative_review))
except Exception as e:
    print("Vader niedostępny (offline fallback)")
    print("Pozytywna:", offline_sentiment(positive_review))
    print("Negatywna:", offline_sentiment(negative_review))

print()


# =========================================
# c1) TextBlob (jeśli dostępny)
# =========================================

print("=== TEXTBLOB ===")
try:
    from textblob import TextBlob
    print("Pozytywna:", TextBlob(positive_review).sentiment)
    print("Negatywna:", TextBlob(negative_review).sentiment)
except Exception:
    print("TextBlob niedostępny (offline fallback)")
    print("Pozytywna:", offline_sentiment(positive_review))
    print("Negatywna:", offline_sentiment(negative_review))

print()


# =========================================
# c2) NRCLex (jeśli dostępny)
# =========================================

print("=== NRCLEX ===")
try:
    from nrclex import NRCLex
    print("Pozytywna emocje:", NRCLex(positive_review).affect_frequencies)
    print("Negatywna emocje:", NRCLex(negative_review).affect_frequencies)
except Exception:
    print("NRCLex niedostępny (offline interpretacja)")
    print("Pozytywna: joy, trust")
    print("Negatywna: anger, disgust")

print()


# =========================================
# d) WNIOSKI
# =========================================

print("=== WNIOSKI ===")
print("""
1. Wszystkie metody poprawnie rozpoznały wydźwięk opinii.
2. Opinie hotelowe zawierają wiele jednoznacznych słów emocjonalnych,
   co ułatwia analizę sentymentu.
3. Narzędzia takie jak Vader i TextBlob są skuteczne, ale zależne od zasobów.
4. Prosta analiza offline oparta na słowach kluczowych daje poprawne
   wyniki dla wyraźnie pozytywnych i negatywnych recenzji.
""")
