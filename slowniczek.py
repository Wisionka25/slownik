'''
Zadanie zaliczeniowe z języka Python
Imię i nazwisko ucznia: Julia Wisniewska
Data wykonywania zadania: 01.12.2023 - ???
Treść zadania: Słownik dla trzech języków
Opis funkcjonalności aplikacji: ???
'''
#Początek aplikacji- menu
def menu():
    print("********")
    print("Witam w aplikacji")
    print("********")

#Działanie aplikacji
def entry():
    #pass
    slowo=input("Podaj słowo: ")               #podanie słowa
    try:
        with open('jezyki.txt','r') as plik:
            slownik={}
            for linia in plik:
                slowo_w_linii=linia.strip().split()  #
                klucz = int(slowo_w_linii[0])  #zmienia element(numer) na klucz
                wartosci=' '.join(slowo_w_linii[1:])
                slownik[klucz] = wartosci
                
                
    except Exception as e:
        print(f"Błąd: {e}")
    

#Pytanie o nowe słowo
def dodaj():
    pass




#-------------#
#Główne działania aplikacji
def main():
    menu()
    while True:
        entry()
        dodaj()
        koniec = input("Czy chcesz kontynuować? (t/n)")
        if koniec in ('t','n','T','N'):
            if koniec != 't' and koniec != 'T':
                break
        else:
            print("Wybierz poprawnie")

if __name__ == "__main__":
    main()