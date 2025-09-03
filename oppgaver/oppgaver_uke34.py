# This file is part of the Python learning path in Gokstad Akademiet's two-year Backend Programming program.
# Exercises focus on core Python concepts and intentionally exclude SQL or database content.
# %%
# Ny rekkefølge 1 (Oppgave 13)
# Spør brukeren om deres favorittfarge og skriv ut en melding som sier "Din favorittfarge er FARGE".
# Kullanıcıya favori rengini sor ve "Favori rengin RENGİN" şeklinde bir mesaj yazdır.
# Konsept: input(), print(), String

farge = input("Hva er favorittfargen din? ")
print(f"Favorittfargen din {farge}.")

# %%
# Ny rekkefølge 2 (Oppgave 1)
# Be brukeren om sitt navn og skriv ut en hilsen med navnet.
# Konsept: input(), print(), String

navn = input("Hva er navnet ditt? :")
print(f"Hei {navn}, hyggelig å møte deg!")

# %%
# Ny rekkefølge 3 (Oppgave 18)
# Norsk: Be brukeren om en tekst og skriv ut den femte bokstaven i teksten.
# Türkçe: Kullanıcıdan bir metin iste ve metindeki beşinci harfi yazdır.
# Konsept: input(), print(), String, Indexing

ordet = input("Skriv en tekst: ")
if len(ordet) >= 5:
    print("Den femte bokstaven er:", ordet[4])
else:
    print("Teksten er for kort, du bør legge inn et ord med minst fem bokstaver.")

# %%
# Ny rekkefølge 4 (Oppgave 34)
# Be brukeren om et ord og skriv ut ordet med store bokstaver.
# Konsept: input(), print(), String, Manipulation

ordet = input("Skriv en tekst: ")
print(ordet.upper())

# %%
# Ny rekkefølge 5 (Oppgave 6)
# Be brukeren om en tekst og tell antall tegn i teksten. Skriv ut resultatet.
# Konsept: input(), String, print(), len-funksjon

ordet = input("Skriv en tekst: ")
print(f"Teksten som legges inn har {len(ordet)} tegn")

# %%
# Ny rekkefølge 6 (Oppgave 2)
# Be brukeren om to tall, legg dem sammen, og skriv ut resultatet.
# Konsept: input(), Aritmetikk, print(), Int

tall1 = int(input("Skriv det første tallet: "))
tall2 = int(input("Skriv det andre tallet: "))

print(f"Summen av tallene er: {tall1 + tall2}")

# %%
# Ny rekkefølge 7 (Oppgave 3)
# Be brukeren om to tall og finn gjennomsnittet av dem. Skriv ut resultatet.
# Konsept: input(), Aritmetikk, print(), Float

tall1 = float(input("Skriv det første tallet: "))
tall2 = float(input("Skriv det andre tallet: "))

print(f"Gjennomsnittet av tallene er = {(tall1 + tall2) / 2}")

# %%
# Ny rekkefølge 8 (Oppgave 4)
# Konverter en temperatur fra Celsius til Fahrenheit og skriv ut resultatet.
# Konsept: Aritmetikk, print(), Float

celsius = float(input("Skriv temperaturen i Celsius: "))
fahrenheit = (celsius * 9) / 5 + 32

print(f"{celsius} Celsius er = {fahrenheit} Fahrenheit.")

# %%
# Ny rekkefølge 9 (Oppgave 12)
# Konverter en temperatur fra Fahrenheit til Celsius og skriv ut resultatet.
# Konsept: Aritmetikk, print(), Float

fahrenheit = float(input("Skriv temperaturen i Fahrenheit: "))
celsius = (fahrenheit - 32) / 5

print(f"{fahrenheit} Fahrenheit = {celsius} Celsius.")

# %%
# Ny rekkefølge 10 (Oppgave 5)
# La brukeren gi inn et antall minutter og konverter dette til timer og minutter.
# Konsept: input(), Aritmetikk, print(), Int

minutter = int(input("Skriv antall minutter: "))

timer = minutter // 60
rester = minutter % 60

print(f"{minutter} minutter er = {timer} time(r) og {rester} minutt(er).")

# %%
# Ny rekkefølge 11 (Oppgave 16)
# Spør brukeren om sin høyde i cm og konverter den til fot (1 fot = 30.48 cm).
# Konsept: input(), Aritmetikk, print(), Float

høyden = float(input("Skriv høyden din i cm:"))
fot = høyden / 30.48

print(f"Høyden din er {fot:.2f} fot.")

# %%
# Ny rekkefølge 12 (Oppgave 26)
# Be brukeren om deres timepris og antall timer de jobbet denne uken, og beregn deres ukelønn.
# Konsept: input(), Aritmetikk, print(), Float

timepris = float(input("Hva er din timepris? :"))
jobbtimer = float(input("Hvor mange timer jobber du hver uke? :"))
ukelønn = timepris * jobbtimer

print(f"Ukelønnen din er = {ukelønn:.2f} kroner.")

# %%
# Ny rekkefølge 13 (Oppgave 28)
# Be brukeren om en pris på en vare og en rabatt i prosent, beregn den rabatterte prisen.
# Konsept: input(), Aritmetikk, print(), Float

varepris = float(input("Skriv vareprisen: "))
rabatt = float(input("Skriv rabatten i prosent :"))

rabattert_pris = varepris * (100 - rabatt) / 100
print(f"Den rabatterte prisen er = {rabattert_pris:.2f} kroner.")

# %%
# Ny rekkefølge 14 (Oppgave 9)
# Be brukeren om et ord, og skriv ut ordet baklengs.
# Konsept: input(), String, print(), Slicing

ordet = input("Skriv et ord: ")
baklengs_tekst = ordet[::-1]

print(f"Ordet baklengs er: {baklengs_tekst}")

# %%
# Ny rekkefølge 15 (Oppgave 29)
# Spør brukeren om et ord og skriv ut det tredje og det nest siste tegnet i ordet.
# Konsept: input(), print(), String, Indexing

ordet = input("Skriv et ord: ")

if len(ordet) >= 3:
    tredje_tegn = ordet[2]
    nest_siste_tegn = ordet[-2]
    print(f"Det tredje tegnet er {tredje_tegn} og det nest siste tegnet er {nest_siste_tegn}")
else:
    print("Ordet er for kort til å finne tredje og nest siste tegn")

# %%
# Ny rekkefølge 16 (Oppgave 30)
# Norsk: Be brukeren om en setning og skriv ut hvert ord i setningen på en ny linje.
# Konsept: input(), print(), String, Splitting

setning = input("Skriv en setning: ")

ord_liste = setning.split()

for ord in ord_liste:
    print(ord)

# %%
# Ny rekkefølge 17 (Oppgave 33)
# Norsk: Spør brukeren om en setning og skriv ut antall ord i setningen.
# Türkçe: Kullanıcıdan bir cümle iste ve cümledeki kelime sayısını yazdır.
# Konsept: input(), print(), String, Splitting

# %%
# Ny rekkefølge 18 (Oppgave 31)
# Norsk: Be brukeren om en tekst og skriv ut om teksten inneholder bokstaven 'a'.
# Türkçe: Kullanıcıdan bir metin iste ve metnin ‘a’ harfi içerip içermediğini yazdır.
# Konsept: input(), print(), String, Logic

# %%
# Ny rekkefølge 19 (Oppgave 10)
# Norsk: Spør brukeren om en hel streng, og finn ut om strengen er et palindrom.
# Türkçe: Kullanıcıdan bir metin iste, palindrom olup olmadığını kontrol et.
# Konsept: input(), String, print(), Slicing

# %%
# Ny rekkefølge 20 (Oppgave 22)
# Norsk: Be brukeren om et ord og skriv ut antall vokaler i ordet.
# Türkçe: Kullanıcıdan bir kelime iste ve kelimedeki sesli harf sayısını yazdır.
# Konsept: input(), print(), String, Looping

# %%
# Ny rekkefølge 21 (Oppgave 38)
# Norsk: Be brukeren om et ord, bytt ut alle vokalene med bokstaven 'x', og skriv ut det nye ordet.
# Türkçe: Kullanıcıdan bir kelime iste, tüm sesli harfleri ‘x’ ile değiştirip yazdır.
# Konsept: input(), print(), String, Manipulation

# %%
# Ny rekkefølge 22 (Oppgave 21)
# Norsk: Spør brukeren om et heltall og skriv ut om tallet er oddetall eller partall.
# Türkçe: Kullanıcıdan bir tam sayı iste, tek mi çift mi olduğunu yazdır.
# Konsept: input(), Aritmetikk, print(), Int

# %%
# Ny rekkefølge 23 (Oppgave 35)
# Norsk: La brukeren gi inn et tall og avgjøre om tallet er positivt, negativt, eller null.
# Türkçe: Kullanıcıdan bir sayı iste, pozitif mi negatif mi sıfır mı olduğunu yazdır.
# Konsept: input(), print(), Logic, Int

# %%
# Ny rekkefølge 24 (Oppgave 36)
# Norsk: Spør brukeren om tre tall og skriv ut det største tallet.
# Türkçe: Kullanıcıdan üç sayı iste ve en büyüğünü yazdır.
# Konsept: input(), Aritmetikk, print(), Logic

# %%
# Ny rekkefølge 25 (Oppgave 39)
# Norsk: Spør brukeren om et tall og skriv ut alle heltall opp til det tallet.
# Türkçe: Kullanıcıdan bir sayı iste ve 1’den o sayıya kadar olan tüm sayıları yazdır.
# Konsept: input(), print(), Looping, Int

# %%
# Ny rekkefølge 26 (Oppgave 32)
# Norsk: Be brukeren om et tall og skriv ut tallets faktorielle.
# Türkçe: Kullanıcıdan bir sayı iste ve faktöriyelini hesaplayıp yazdır.
# Konsept: input(), Aritmetikk, print(), Int, Looping

# %%
# Ny rekkefølge 27 (Oppgave 24)
# Norsk: Be brukeren om et tall og skriv ut den kvadratiske roten av tallet.
# Türkçe: Kullanıcıdan bir sayı iste ve karekökünü hesaplayıp yazdır.
# Konsept: input(), Aritmetikk, print(), Float


# %%
# Ny rekkefølge 28 (Oppgave 7)
# Norsk: Spør brukeren om sin fødselsdato og beregn deres alder.
# Türkçe: Kullanıcıdan doğum tarihini iste ve yaşını hesapla.
# Konsept: input(), Aritmetikk, print(), Int

# %%
# Ny rekkefølge 29 (Oppgave 8)
# Norsk: La brukeren gi inn en pris, beregn 15% tips og skriv ut både tips og totalprisen.
# Türkçe: Kullanıcıdan bir fiyat iste, %15 bahşiş ve toplam fiyatı hesaplayıp yazdır.
# Konsept: input(), Aritmetikk, print(), Float

# %%
# Ny rekkefølge 30 (Oppgave 11)
# Norsk: Be brukeren om deres vekt i kilo og høyde i meter, og beregn deres BMI.
# Türkçe: Kullanıcıdan kilosunu ve boyunu iste, BMI hesapla.
# Konsept: input(), Aritmetikk, print(), Float

# %%
# Ny rekkefølge 31 (Oppgave 14)
# Norsk: Be brukeren om radiusen på en sirkel og beregn sirkelens omkrets.
# Türkçe: Kullanıcıdan dairenin yarıçapını iste, çevresini hesapla.
# Konsept: input(), Aritmetikk, print(), Float

# %%
# Ny rekkefølge 32 (Oppgave 15)
# Norsk: Be brukeren om radiusen på en sirkel og beregn sirkelens areal.
# Türkçe: Kullanıcıdan dairenin yarıçapını iste, alanını hesapla.
# Konsept: input(), Aritmetikk, print(), Float

# %%
# Ny rekkefølge 33 (Oppgave 17)
# Norsk: Be brukeren om to adjektiv, et substantiv og et verb, og lag en setning med disse ordene.
# Türkçe: Kullanıcıdan iki sıfat, bir isim ve bir fiil iste, bunlarla cümle kur.
# Konsept: input(), print(), String

# %%
# Ny rekkefølge 34 (Oppgave 19)
# Norsk: Spør brukeren om en streng, og skriv ut om strengen er kortere, lik eller lengre enn 5 tegn.
# Türkçe: Kullanıcıdan bir metin iste, 5 karakterden kısa mı uzun mu eşit mi olduğunu yazdır.
# Konsept: input(), print(), String, len-funksjon

# %%
# Ny rekkefølge 35 (Oppgave 20)
# Norsk: La brukeren gi inn et beløp i en valuta og konverter dette til en annen valuta basert på en gitt kurs.
# Türkçe: Kullanıcıdan bir para miktarı iste, verilen kura göre başka para birimine çevir.
# Konsept: input(), Aritmetikk, print(), Float

# %%
# Ny rekkefølge 36 (Oppgave 23)
# Norsk: La brukeren gi inn sin fødselsdato og finn ut hvilket stjernetegn de er født under.
# Türkçe: Kullanıcıdan doğum tarihini iste, burcunu hesapla.
# Konsept: input(), print(), String, Logic

# %%
# Ny rekkefølge 37 (Oppgave 25)
# Norsk: Be brukeren om to ord og sjekk om de er anagrammer av hverandre.
# Türkçe: Kullanıcıdan iki kelime iste, birbirinin anagramı olup olmadığını kontrol et.
# Konsept: input(), print(), String, Logic

# %%
# Ny rekkefølge 38 (Oppgave 27)
# Norsk: La brukeren gi inn et antall sekunder og konverter dette til timer, minutter, og sekunder.
# Türkçe: Kullanıcıdan saniye iste, saat, dakika, saniyeye çevir.
# Konsept: input(), Aritmetikk, print(), Int

# %%
# Ny rekkefølge 39 (Oppgave 37)
# Norsk: Be brukeren om en tekst og skriv ut antall mellomrom i teksten.
# Türkçe: Kullanıcıdan bir metin iste, boşluk sayısını yazdır.
# Konsept: input(), print(), String, Counting

# %%
# Ny rekkefølge 40 (Oppgave 40)
# Norsk: La brukeren gi inn en setning og skriv ut setningen i omvendt rekkefølge.
# Türkçe: Kullanıcıdan bir cümle iste, cümleyi ters çevirip yazdır.
# Konsept: input(), print(), String, Slicing
