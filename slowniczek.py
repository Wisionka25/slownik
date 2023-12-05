'''
Zadanie zaliczeniowe z języka Python
Imię i nazwisko ucznia: Julia Wisniewska
Data wykonywania zadania: 01.12.2023 - ???
Treść zadania: Słownik dla trzech języków
Opis funkcjonalności aplikacji: ???
'''

from unidecode import unidecode

#Początek aplikacji- menu
def menu():
    print("********")
    print("Witam w aplikacji słownik w trzech językach")
    print("********")

#Działanie aplikacji
def entry():
    global slownik                                                          #Zmienna slownik ma być zmienną globalną
    slownik = {}                                                            #Stworzenie zmiennej(słownika) slownik
    slowo0 = input("Podaj słowo: ")                                         #Podanie słowa
    slowo = unidecode(slowo0.lower())                                       #Zmiana liter na małe
    jaki_numer = None                                                       #Sprawdzenie jakie klucze muszą zostać znalezione
    try:                                                                    #Sprawdzanie błędu
        with open('jezyki.txt','r') as plik:                                #Otwarcie pliku
            for linia in plik:                                              #Pętla po każdej linii w pliky .txt
                slowo_w_linii = linia.strip().split()                       #Usuwa białe znaki i dzieli je
                klucz = int(slowo_w_linii[0])                               #Zmienia elementu(numer) na klucz
                wartosci = unidecode(' '.join(slowo_w_linii[1:])).lower()   #Zmiana emelentu(slowa) na wartość w słowniku
                slownik[klucz] = wartosci                                   #Dodanie wartosci do kluczy (tworzenie słownika)  
                if wartosci == slowo:                                       #Sprawdza czy jakaś wartość slownika będzie taka sama jak podane słowo
                    jaki_numer = klucz                                      #Przypisujemy klucz ktory pasuje do wprowadzonego słowa
    except FileNotFoundError:                                               #Bład jeśli plik nie został znaleziony
        print("Plik nie istnieje")          
    except Exception as e:                                                  #Nieznany błąd
        print(f"Błąd: {e}")
    return jaki_numer                                                       #Zwraca numer klucza

    
    

#Stworzenie słownika(Polski-Angielski-Niemiecki)
def tlumacz(jaki_numer):                                        
    if jaki_numer != None:                                                  #Sprawdza czy klucz został znaleziony
        slownik2 = ["polski: ","angielski: ","niemiecki:"]                  #Stworzenie listy
        do_slownika2 = {}                                                   #Tworzy słownik do którego elemty listy będą kluczami 
        try:                                                                #Sprawdzanie błędu
            with open('jezyki.txt', 'r') as plik:                           #Otwarcie pliku
                for linia in plik:                                          #Pętla po każdej linii w pliky .txt
                    slowo_w_linii = linia.strip().split()                   #Usuwa białe znaki i dzieli je
                    klucz = int(slowo_w_linii[0])                           #Zmienia elementu(numer) na klucz
                    wartosci = ' '.join(slowo_w_linii[1:]).capitalize()     #Zmiana emelentu(slowa) na wartość w słowniku
                    slownik[klucz] = wartosci                               #Dodanie wartosci do kluczy (tworzenie słownika)
                    if klucz == jaki_numer:                                 #Sprawdza czy znaleziony numer klucza jest taki sam jak klucz podanego słowa
                        do_slownika2[slownik2.pop(0)] = wartosci            #Usuwając pierwszy element listy zapamiętuje go i zapisuje do niego wartość tworząc słownik
                        if not slownik2:                                    #Jeśli słownik pusty
                            break                                           #Przerwij
        except FileNotFoundError:                                           #Bład jeśli plik nie został znaleziony
            print("Plik nie istnieje")      
        except Exception as e:                                              #Nieznany błąd
            print(f"Błąd: {e}")
        for jezyk, do_slownika2 in do_slownika2.items():                    #Petla do przypisania kluczy i wartości
            print(f"{jezyk}: {do_slownika2}")                               #Drukowanie pary klucz-wartość
    else:
        print("Nie ma takiego słowa")

def dodaj(jaki_numer):
    if jaki_numer == None:
        odp=input("Czy chcesz dodać nowe słowo?(n/t): ")
        odp = odp.lower()
        if odp =='t':
            nowe = input("Prosze nam podać jakie słowo chcesz dodać: ")
            try: 
                with open("Do_dodania.txt","w") as dodaj:
                    dodaj.write(f"{nowe} \n")
            except FileNotFoundError:
                print("Plik nie znaleziony")
            except Exception as e:
                print(f"Błąd: {e}")

#-------------#
#Główne działania aplikacji
def main():
    menu()
    global slownik
    slownik = {}
    while True:
        jaki_numer = entry()
        tlumacz(jaki_numer)
        dodaj(jaki_numer)
        koniec = input("Czy chcesz kontynuować? (t/n)")
        if koniec in ('t','n','T','N'):
            if koniec != 't' and koniec != 'T':
                break
        else:
            print("Wybierz poprawnie")

if __name__ == "__main__":
    main()