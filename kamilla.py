import csv
import pandas as pd

# zad.1
a= input("podaj nazwę pliku")
if a == 'c:/Users/oliwka/Desktop/projekty_r/Python_zaliczenie/wina/wine.data':
    with open('c:/Users/oliwka/Desktop/projekty_r/Python_zaliczenie/wina/wine.data', newline='') as filecsv:
        readcsv = csv.reader(filecsv)
        for index, wiersz in enumerate(readcsv):
            if index == 0:
                print(f'etykiety:{wiersz}')
            else:
                print(wiersz)
#zad.2 
df= pd.read_csv('c:/Users/oliwka/Desktop/projekty_r/Python_zaliczenie/wina/wine.data', sep=',')
e= df[:0]
print('etykiety', e)

#zad.3
print(df)
w= int(input("numer początkowy nr wiersza "))
z= int(input("numer końcowy nr wiersza "))
wiersze = df[w:(z+1)]
print(wiersze)

#zad.4
ztr= int(input("numer wiersza zbioru treningowego "))
zts= int(input("numer wiersza zbioru testowego "))
zwa= int(input("numer wiersza zbioru walidacyjnego "))
print('zbiów treningowy', df[:ztr])
print('zbiów treningowy', df[:zts])
print('zbiów treningowy', df[:zwa])

#5
klasy_decyzyjne=(df[df.columns[-1]]).unique()
print(klasy_decyzyjne)
print('liczba klas decyzyjnych: ', len(klasy_decyzyjne))
print(df)

#6
kd= int(input("podaj klasę decyzyjną "))
if kd in klasy_decyzyjne:
    print(df[(df[df.columns[-1]]) == kd])

#7
df1= df[(df[df.columns[-1]]) == kd]
df1.to_csv('dane_z_klas_decyzyjnych.csv', index=False)
    
