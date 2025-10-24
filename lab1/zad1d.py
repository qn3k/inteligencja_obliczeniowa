import math
from datetime import date, datetime

# Pobranie danych od użytkownika
imie = input("Podaj swoje imię: ")
rok = int(input("Podaj rok urodzenia (np. 1990): "))
miesiac = int(input("Podaj miesiąc urodzenia (1-12): "))
dzien = int(input("Podaj dzień urodzenia (1-31): "))

# Obliczenie liczby dni życia
data_urodzenia = date(rok, miesiac, dzien)
dzisiaj = date.today()
t = (dzisiaj - data_urodzenia).days

# Obliczenie fal
fizyczna = math.sin(((2 * math.pi) / 23) * t)
emocjonalna = math.sin(((2 * math.pi) / 28) * t)
intelektualna = math.sin(((2 * math.pi) / 33) * t)

# Wynik
print(f"\nCześć, {imie}!")
print(f"Dziś jest {t} dzień Twojego życia.")
print("\nTwoje fale biologiczne:")
print(f"Fala fizyczna:      {fizyczna:.3f}")
print(f"Fala emocjonalna:   {emocjonalna:.3f}")
print(f"Fala intelektualna: {intelektualna:.3f}")

#czat v1