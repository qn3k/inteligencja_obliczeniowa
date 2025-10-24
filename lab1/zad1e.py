import math
from datetime import date

# Pobranie danych od użytkownika
imie = input("Podaj swoje imię: ")
rok = int(input("Podaj rok urodzenia (np. 1990): "))
miesiac = int(input("Podaj miesiąc urodzenia (1-12): "))
dzien = int(input("Podaj dzień urodzenia (1-31): "))

# Obliczenie liczby dni życia
data_urodzenia = date(rok, miesiac, dzien)
dzisiaj = date.today()
t = (dzisiaj - data_urodzenia).days

# Obliczenie fal dzisiaj
fizyczna = math.sin(((2 * math.pi) / 23) * t)
emocjonalna = math.sin(((2 * math.pi) / 28) * t)
intelektualna = math.sin(((2 * math.pi) / 33) * t)

# Obliczenie fal jutro
fizyczna_jutro = math.sin(((2 * math.pi) / 23) * (t + 1))
emocjonalna_jutro = math.sin(((2 * math.pi) / 28) * (t + 1))
intelektualna_jutro = math.sin(((2 * math.pi) / 33) * (t + 1))

# Funkcja do interpretacji wyników
def interpretuj(nazwa, dzis, jutro):
    print(f"{nazwa}: {dzis:.3f}")
    if dzis < -0.5:
        print(f"  🫶 Nie martw się, {imie}, będzie lepiej!")
        if jutro > dzis:
            print("  🌤 Jutro Twoja energia w tej sferze wzrośnie!")
    elif dzis > 0.5:
        print(f"  🎉 Świetnie, {imie}! Dziś masz wysoki poziom w tej sferze!")
    else:
        print("  🙂 Dziś wszystko jest w równowadze.")

# Wyniki
print(f"\nCześć, {imie}!")
print(f"Dziś jest {t} dzień Twojego życia.\n")
print("Twoje fale biologiczne:\n")

interpretuj("Fala fizyczna", fizyczna, fizyczna_jutro)
interpretuj("Fala emocjonalna", emocjonalna, emocjonalna_jutro)
interpretuj("Fala intelektualna", intelektualna, intelektualna_jutro)

#czat v2
#czas 12 minut