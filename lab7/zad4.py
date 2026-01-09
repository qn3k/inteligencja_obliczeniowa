import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from nrclex import NRCLex

# Jednorazowe pobranie zasobów
nltk.download("vader_lexicon")



#Opinie
positive_review = """
The hotel was absolutely fantastic. The room was spotless, modern and very comfortable.
The staff were incredibly friendly and helpful, always smiling and ready to assist.
The location is perfect, just a few minutes walk from major attractions and the underground.
I would definitely stay here again and highly recommend this hotel to anyone visiting London.
"""

negative_review = """
This was one of the worst hotel experiences I have ever had.
The room was extremely small, dirty and smelled terrible.
The staff were rude and completely unhelpful when we complained.
The noise from the street made it impossible to sleep and the facilities were outdated.
I would never stay here again and do not recommend this place at all.
"""



# b) Analiza sentymentu – NLTK Vader
sia = SentimentIntensityAnalyzer()

print("=== VADER ===")
print("Pozytywna opinia:", sia.polarity_scores(positive_review))
print("Negatywna opinia:", sia.polarity_scores(negative_review))
print()


#TextBlob

print("=== TEXTBLOB ===")
print("Pozytywna opinia:", TextBlob(positive_review).sentiment)
print("Negatywna opinia:", TextBlob(negative_review).sentiment)
print()


#NRCLex – emocje

print("=== NRCLEX ===")
positive_emotions = NRCLex(positive_review).affect_frequencies
negative_emotions = NRCLex(negative_review).affect_frequencies

print("Pozytywna opinia – emocje:", positive_emotions)
print("Negatywna opinia – emocje:", negative_emotions)
print()


#wlasna interpretacja
print("=== INTERPRETACJA EMOCJI ===")
print("Pozytywna opinia: dominujące emocje to joy, trust")
print("Negatywna opinia: dominujące emocje to anger, disgust, sadness")
print()

'''
print("=== WNIOSKI ===")
print("""
1. Wszystkie narzędzia poprawnie rozpoznały wydźwięk obu opinii.
2. Vader bardzo dobrze radzi sobie z krótkimi, emocjonalnymi recenzjami hotelowymi.
3. TextBlob potwierdza wyniki Vadera, ale jest mniej szczegółowy.
4. NRCLex umożliwia analizę konkretnych emocji, a nie tylko polaryzacji.
5. Opinie hotelowe są dobrym materiałem do analizy sentymentu,
   ponieważ zawierają dużo jednoznacznych słów emocjonalnych.
""")
'''


'''
Analiza sentymentu dobrze radzi sobie z opiniami hotelowymi,
ponieważ zawierają one wyraźne słowa nacechowane emocjonalnie.
Modele oparte na transformerach (np. DistilRoBERTa) są najdokładniejsze,
ale Vader w zupełności wystarcza do prostych zastosowań, 
takich jak analiza recenzji z Booking.com.
'''