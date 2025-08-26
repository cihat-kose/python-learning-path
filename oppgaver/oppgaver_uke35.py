# %%
# If-setning
# 1. Norsk: Les inn et tall fra tastaturet. (Husk å bruke casting til riktig datatype.)
#    - Hvis tallet er større enn 10, skriv ut "Tallet er større enn 10".
#    - Hvis tallet er mindre enn 10, skriv ut "Tallet er mindre enn 10".
#    - Hvis tallet er lik 10, skriv ut "Tallet er lik 10".
# Türkçe: Klavyeden bir sayı oku (doğru veri tipine çevirmeyi unutma).
#    - Sayı 10'dan büyükse "Sayı 10'dan büyüktür" yazdır.
#    - Sayı 10'dan küçükse "Sayı 10'dan küçüktür" yazdır.
#    - Sayı 10'a eşitse "Sayı 10'a eşittir" yazdır.
# Konsept: input(), casting, if-elif-else, print(), int/float

# 2. Norsk: Les inn to tall og lagre dem i int-variabler x og y.
#    a) Hvis x og y er like, skriv "x og y er like".
#    b) Hvis x > y, skriv "x er større enn y", ellers "x er mindre enn y".
# Türkçe: Klavyeden iki sayı al, x ve y değişkenlerine kaydet.
#    a) x ve y eşitse "x ve y eşittir" yazdır.
#    b) x > y ise "x y'den büyüktür", değilse "x y'den küçüktür" yazdır.
# Konsept: input(), int, karşılaştırma operatörleri, if-else, print()

# %%
# For-løkke
# 1. Norsk: Skriv ut tallene fra 0 til 9.
# Türkçe: 0'dan 9'a kadar olan sayıları yazdır.
# Konsept: for, range(), print()

# 2. Norsk: Skriv ut tallene fra 5 til 15.
# Türkçe: 5'ten 15'e kadar olan sayıları yazdır.
# Konsept: for, range(start, stop), print()

# 3. Norsk: Skriv ut alle partallene opp til 20.
# Türkçe: 20'ye kadar olan tüm çift sayıları yazdır.
# Konsept: for, range(), modulus %, koşul

# 4. Norsk: Skriv ut alle oddetallene opp til 20.
# Türkçe: 20'ye kadar olan tüm tek sayıları yazdır.
# Konsept: for, range(), %, koşul

# 5. Norsk: Skriv ut tallene fra 30 og ned til 10.
# Türkçe: 30'dan 10'a kadar geriye doğru sayıları yazdır.
# Konsept: for, range(start, stop, step)

# 6. Norsk: Skriv ut alle oddetallene fra 30 til 10.
# Türkçe: 30'dan 10'a doğru tüm tek sayıları yazdır.
# Konsept: for, range() ters adım, %

# 7. Norsk: Summer tallene fra 1 til 10. Skriv ut summen etter hver iterasjon.
# Türkçe: 1'den 10'a kadar sayıları topla. Her yinelemeden sonra ara toplamı yazdır.
# Konsept: for, akümülatör değişkeni, print()

# 8. Norsk: Summer alle partallene opp til 20.
# Türkçe: 20'ye kadar tüm çift sayıların toplamını hesapla.
# Konsept: for, koşul, toplam

# 9. Norsk: Summer alle oddetallene opp til 20.
# Türkçe: 20'ye kadar tüm tek sayıların toplamını hesapla.
# Konsept: for, koşul, toplam

# 10. Norsk: Les inn et tall og skriv ut gangetabellen ved hjelp av en for-løkke.
# Türkçe: Bir sayı al ve bu sayının çarpım tablosunu for döngüsü ile yazdır.
# Konsept: input(), int, for, çarpma, formatlı çıktı

# %%
# While-løkke
# 1. Norsk: Skriv ut tallene fra 1 til 10.
# Türkçe: 1'den 10'a kadar sayıları yazdır.
# Konsept: while, sayaç, artırım

# 2. Norsk: Skriv ut tallene fra 5 til 15.
# Türkçe: 5'ten 15'e kadar sayıları yazdır.
# Konsept: while, koşul, artırım

# 3. Norsk: Skriv ut tallene fra 30 til 10.
# Türkçe: 30'dan 10'a kadar sayıları yazdır.
# Konsept: while, azaltım (decrement)

# 4. Norsk: Skriv ut partallene opp til 20.
# Türkçe: 20'ye kadar çift sayıları yazdır.
# Konsept: while, %, koşul

# 5. Norsk: Skriv ut alle kvadrattallene opp til 100.
# Türkçe: 100'e kadar tüm kare sayıları yazdır.
# Konsept: while, i*i, koşul

# 6. Norsk: Skriv ut alle kvadrattallene mindre enn en innlest verdi.
# Türkçe: Klavyeden girilen değerden küçük tüm kare sayıları yazdır.
# Konsept: input(), int, while, kare

# %%
# Doble tall
# 1. Norsk: Start med 1 og dobbel tallet i 10 iterasjoner. Resultat: 1, 2, 4, ..., 512
# Türkçe: 1 ile başla ve her yinelemede sayıyı ikiye katla, 10 iterasyon yap. Sonuç: 1, 2, 4, ..., 512
# Konsept: for/while, çarpma, liste/print

# %%
# Fibonaccitall (Vanskelig)
# 1. Norsk: Skriv ut Fibonacci-følgen, start med 1, 1 og fortsett til ønsket grense.
# Türkçe: Fibonacci dizisini ekrana yazdır; 1, 1 ile başla ve belirlenen sınıra kadar devam et.
# Konsept: döngü, değişken kaydırma, toplama, while/for

# %%
# Listeoperasjoner
# 1. Norsk: Legge til/fjerne og manipulere elementer (append, insert, extend, remove, pop, clear, sort, sorted, reverse).
# Türkçe: Listeye eleman ekleme/çıkarma ve düzenleme (append, insert, extend, remove, pop, clear, sort, sorted, reverse).
# Konsept: list metotları, yerinde değişiklik vs kopya

# 2. Norsk: Søk og indeksering (index, count).
# Türkçe: Arama ve indeksleme (index, count).
# Konsept: list arama fonksiyonları

# 3. Norsk: Kopiering og kloning (copy).
# Türkçe: Kopyalama ve klonlama (copy).
# Konsept: sığ kopya, referans

# 4. Norsk: Listefunksjoner (len, max, min, sum).
# Türkçe: Liste fonksiyonları (len, max, min, sum).
# Konsept: yerleşik fonksiyonlar

# %%
# Sorter og Reverser
# 1. Norsk: Sorter ulike samlinger:
#    - [3,1,4,1,5,9,2,6,5] stigende
#    - ['apple','Banana','Cherry'] alfabetisk, case-uavhengig
#    - (6,2,9,1,5,3) synkende
#    - ['apple','banana','cherry'] etter ordlengde
#    - liste av dicts etter bestemt nøkkel
# Türkçe: Çeşitli koleksiyonları sırala:
#    - [3,1,4,1,5,9,2,6,5] artan
#    - ['apple','Banana','Cherry'] büyük-küçük harften bağımsız alfabetik
#    - (6,2,9,1,5,3) azalan
#    - ['apple','banana','cherry'] kelime uzunluğuna göre
#    - sözlük listesi belirli bir anahtara göre
# Konsept: sort(), sorted(), key=, reverse=True, tuple→list

# 2. Norsk: Reverser samlinger:
#    - [1,2,3,4,5]
#    - 'hello' til liste og reversed
#    - (1,2,3,4,5)
#    - reversed på dictionary-nøkler
#    - Reverser ordrekkefølgen i 'Python er gøy'
# Türkçe: Koleksiyonları ters çevir:
#    - [1,2,3,4,5]
#    - 'hello' → listeye çevir ve reversed ile ters çevir
#    - (1,2,3,4,5)
#    - sözlük anahtarlarını reversed ile dolaş
#    - 'Python er gøy' cümlesindeki kelimelerin sırasını tersine çevir
# Konsept: reversed(), slice [::-1], list(), join()

# %%
# Filter
# 1. Norsk: Filtrer ut oddetall fra [1,2,3,4,5,6].
# Türkçe: [1,2,3,4,5,6] listesinden tek sayıları filtrele.
# Konsept: filter(), lambda, %

# 2. Norsk: Finn ord med mer enn 5 bokstaver i ['apple','banana','cherry','date'].
# Türkçe: ['apple','banana','cherry','date'] listesinden 5 harften uzun kelimeleri bul.
# Konsept: filter(), len, lambda

# 3. Norsk: Filtrer negative tall fra (-5,-3,2,4,-1,6).
# Türkçe: (-5,-3,2,4,-1,6) tuple'ından negatif sayıları çıkar.
# Konsept: filter(), lambda, tuple→list

# 4. Norsk: Bruk filter + map for kvadrater av [1,2,3,4,5] som er > 10.
# Türkçe: [1,2,3,4,5] listesinin karelerinden 10'dan büyük olanları üret (filter + map).
# Konsept: map(), filter(), lambda, composability

# 5. Norsk: Filtrer partall fra en dictionary med tall som nøkler.
# Türkçe: Anahtarları sayılardan oluşan bir sözlükte çift anahtarları filtrele.
# Konsept: dict.keys(), filter(), comprehension

# %%
# Zip
# 1. Norsk: Kombiner ['a','b','c'] og [1,2,3] til liste av tupler.
# Türkçe: ['a','b','c'] ile [1,2,3]'ü zip ile eşleştirip tuple listesi oluştur.
# Konsept: zip(), list()

# 2. Norsk: Summer parvise elementer i [1,2,3] og [4,5,6] med zip+map.
# Türkçe: [1,2,3] ve [4,5,6] listelerinin eşleşen elemanlarını toplayarak yeni liste oluştur (zip + map).
# Konsept: zip(), map(), lambda / operator.add

# 3. Norsk: Lag en dictionary fra ['Anna','Bob','Charlie'] og [25,30,35] med zip.
# Türkçe: İki listeden zip ile sözlük oluştur: ['Anna','Bob','Charlie'] → [25,30,35].
# Konsept: zip(), dict()

# 4. Norsk: Kombiner tre lister med zip: ['a','b','c'], [1,2,3], ['apple','banana','cherry'].
# Türkçe: Üç listeyi zip ile birleştir.
# Konsept: zip() çoklu argüman

# 5. Norsk: Bruk zip for å splitte [('a',1),('b',2),('c',3)] i to lister.
# Türkçe: [('a',1),('b',2),('c',3)] listesini zip(*) ile iki ayrı listeye ayır.
# Konsept: unzip tekniği, * operatörü

# %%
# Map
# 1. Norsk: Øk alle verdier i [1,2,3,4] med 1.
# Türkçe: [1,2,3,4] listesindeki tüm değerleri 1 artır.
# Konsept: map(), lambda, list()

# 2. Norsk: Konverter ['1','2','3'] til heltall.
# Türkçe: ['1','2','3'] dizgesini tam sayılara dönüştür.
# Konsept: map(int, ...), type dönüşümü

# 3. Norsk: Funksjon som returnerer første bokstav i hvert ord i ['apple','banana','cherry'] via map.
# Türkçe: ['apple','banana','cherry'] için her kelimenin ilk harfini döndüren fonksiyonu map ile uygula.
# Konsept: map(), lambda / def, indeksleme

# 4. Norsk: Lag en liste med lengdene av ordene i ['apple','banana','cherry'].
# Türkçe: ['apple','banana','cherry'] kelimelerinin uzunluklarını içeren yeni bir liste oluştur.
# Konsept: map(len, ...), list()

# 5. Norsk: Lag en dictionary fra to lister: nøkler ['a','b','c'], verdier [1,2,3] med map.
# Türkçe: İki listeden map kullanarak sözlük oluştur: anahtarlar ['a','b','c'], değerler [1,2,3].
# Konsept: map() + zip() / dict comprehension

