import math
from datetime import datetime

imie = input("Jak masz na imię? ")
rok = int(input("Podaj rok urodzenia: "))
miesiac = int(input("Podaj miesiąc urodzenia: "))
dzien = int(input("Podaj dzień urodzenia: "))

print(f"Witaj {imie}!")

def days_since(rok, miesiac, dzien):
    if rok > 2025:
        return 0
    if miesiac < 1 and miesiac >12:
        return 0
    if dzien <1 and dzien >31:
        return 0
    data_urodzin= datetime(rok, miesiac, dzien)
    dzis = datetime.now()
    roznica = (dzis - data_urodzin).days
    #print(f"Minęło {roznica} dni od Twojego urodzenia")
    return roznica

dni_od_uro = days_since(rok,miesiac,dzien)

yp = round(math.sin((2*math.pi * dni_od_uro)/23), 2)  # fizyczna fala
ye = round(math.sin((2*math.pi * dni_od_uro)/28), 2)  # emocjonalna fala
yi = round(math.sin((2*math.pi * dni_od_uro)/33), 2)  # intelektualna fala

print(f"Twoja fala fizyczna: {yp} ")
print(f"Twoja fala emocjonalna: {ye} ")
print(f"Twoja fala intelektualna: {yi} ")