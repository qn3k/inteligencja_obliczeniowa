import math
from datetime import datetime

# Pobranie danych od użytkownika
imie = input("Jak masz na imię? ")
rok = int(input("Podaj rok urodzenia: "))
miesiac = int(input("Podaj miesiąc urodzenia: "))
dzien = int(input("Podaj dzień urodzenia: "))

print(f"\nWitaj {imie}!\n")

def days_since(rok, miesiac, dzien):
    """Zwraca liczbę dni od daty urodzenia do dziś."""
    try:
        # Walidacja daty – próba stworzenia obiektu datetime
        data_urodzin = datetime(rok, miesiac, dzien)
    except ValueError:
        print("❌ Podano niepoprawną datę urodzenia!")
        return 0

    dzis = datetime.now()

    if data_urodzin > dzis:
        print("❌ Data urodzenia nie może być w przyszłości!")
        return 0

    roznica = (dzis - data_urodzin).days
    return roznica

dni_od_uro = days_since(rok, miesiac, dzien)

if dni_od_uro == 0:
    print("Nie można obliczyć fal dla podanej daty.")
    exit()

# Funkcje obliczające wartości fal
def yp(dni):
    return round(math.sin((2 * math.pi * dni) / 23), 2)  # fizyczna
def ye(dni):
    return round(math.sin((2 * math.pi * dni) / 28), 2)  # emocjonalna
def yi(dni):
    return round(math.sin((2 * math.pi * dni) / 33), 2)  # intelektualna

# Wyliczenie wartości fal
fiz = yp(dni_od_uro)
emo = ye(dni_od_uro)
intel = yi(dni_od_uro)

# Wyświetlenie wyników
print(f"Twoja fala fizyczna: {fiz}")
if fiz < -0.5:
    print("Nie martw się falą fizyczną.")
    if yp(dni_od_uro + 1) > fiz:
        print("Jutro będzie lepiej!")
elif fiz > 0.5:
    print("Ależ dobra fala fizyczna! Tak trzymaj!")

print(f"\nTwoja fala emocjonalna: {emo}")
if emo < -0.5:
    print("Nie martw się falą emocjonalną.")
    if ye(dni_od_uro + 1) > emo:
        print("Jutro będzie lepiej!")
elif emo > 0.5:
    print("Ależ dobra fala emocjonalna! Tak trzymaj!")

print(f"\nTwoja fala intelektualna: {intel}")
if intel < -0.5:
    print("Nie martw się falą intelektualną.")
    if yi(dni_od_uro + 1) > intel:
        print("Jutro będzie lepiej!")
elif intel > 0.5:
    print("Ależ dobra fala intelektualna! Tak trzymaj!")

#czacior poprawil