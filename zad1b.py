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

def yp(dni_od_uro):
    return round(math.sin((2*math.pi * dni_od_uro)/23), 2)  # fizyczna fala
def ye(dni_od_uro):
    return round(math.sin((2*math.pi * dni_od_uro)/28), 2)  # emocjonalna fala
def yi(dni_od_uro):
    return round(math.sin((2*math.pi * dni_od_uro)/33), 2)  # intelektualna fala

print(f"Twoja fala fizyczna: {yp(dni_od_uro)} ")
if yp(dni_od_uro) < -0.5:
    print("Nie martw sie falą fizyczną")
    if yp(dni_od_uro+1)>yp(dni_od_uro):
        print("Jutro będzie lepiej!")
if yp(dni_od_uro) > 0.5:
    print("Alez dobra fala fizyczna! Tak trzymaj!")

print(f"Twoja fala emocjonalna: {ye(dni_od_uro)} ")
if ye(dni_od_uro) < -0.5:
    print("Nie martw sie falą emocjolaną")
    if ye(dni_od_uro+1)>ye(dni_od_uro):
        print("Jutro będzie lepiej!")
if ye(dni_od_uro) > 0.5:
    print("Alez dobra fala emocjonalna! Tak trzymaj!")

print(f"Twoja fala intelektualna: {yi(dni_od_uro)} ")  
if yi(dni_od_uro) < -0.5:
    print("Nie martw sie falą intelektualną")
    if yi(dni_od_uro+1)>yi(dni_od_uro):
        print("Jutro będzie lepiej!")
if yi(dni_od_uro) > 0.5:
    print("Alez dobra fala intelektualną! Tak trzymaj!")     

#czas 37 minut
#oryginal