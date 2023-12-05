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
    print("Witam w aplikacji słownik w trzech językach")
    print("********")

#Działanie aplikacji
def entry():
    global slownik
    slownik={}
    slowo=input("Podaj słowo: ")                                #podanie słowa
    jaki_numer=None                                             #sprawdzenie jaki klucz musi zostać znaleziony
    try:                                                        #sprawdzanie błędu
        with open('jezyki.txt','r') as plik:                    #otwarcie pliku
            for linia in plik:  
                slowo_w_linii=linia.strip().split()  #usuwa białe znaki i dzieli je
                klucz = int(slowo_w_linii[0])  #zmienia elementu(numer) na klucz
                wartosci=' '.join(slowo_w_linii[1:])   #dodanie emelentu(slowa) 
                slownik[klucz] = wartosci           #dodanie wartosci do kluczy (tworzenie słownika)  
                if wartosci==slowo:
                    jaki_numer=klucz            #przypisujemy klucz ktory pasuje do wprowadzonego slowa
                
                
    except Exception as e:
        print(f"Błąd: {e}")
    return jaki_numer

    
    

#Pytanie o nowe słowo
def dodaj(jaki_numer):
    if jaki_numer!=None:
        slownik2 = ["polski: ","angielski: ","niemiecki:"]
        i=0
        do_slownika2={}
        try:
            with open('jezyki.txt', 'r') as plik:
                for linia in plik:
                    slowo_w_linii = linia.strip().split()  
                    klucz = int(slowo_w_linii[0])  
                    wartosci = ' '.join(slowo_w_linii[1:])  
                    slownik[klucz] = wartosci      
                    i+=1     
                    if klucz == jaki_numer:
                        #slownik2.insert(i,wartosci)
                        do_slownika2[slownik2.pop(0)] = wartosci
                        if not slownik2:
                            break
        except Exception as e:
            print(f"Błąd: {e}")
        for jezyk, do_slownika2 in do_slownika2.items():
            print(f"{jezyk}: {do_slownika2}")


#-------------#
#Główne działania aplikacji
def main():
    menu()
    global slownik
    slownik={}
    while True:
        jaki_numer=entry()
        dodaj(jaki_numer)
        koniec = input("Czy chcesz kontynuować? (t/n)")
        if koniec in ('t','n','T','N'):
            if koniec != 't' and koniec != 'T':
                break
        else:
            print("Wybierz poprawnie")

if __name__ == "__main__":
    main()