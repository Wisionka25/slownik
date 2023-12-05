slownik={}
try:                                                        #sprawdzanie błędu
        with open('jezyki.txt','r') as plik:                    #otwarcie pliku
            for linia in plik:  
                slowo_w_linii=linia.strip().split()  #usuwa białe znaki i dzieli je
                klucz = int(slowo_w_linii[0])  #zmienia elementu(numer) na klucz
                wartosci=' '.join(slowo_w_linii[1:])   #dodanie emelentu(slowa) 
                slownik[klucz] = wartosci           #dodanie wartosci do kluczy (tworzenie słownika)  
                # if wartosci==slowo:
                #     jaki_numer=klucz            #przypisujemy klucz ktory pasuje do wprowadzonego slowa
            print(slownik)
                
except Exception as e:
    print(f"Błąd: {e}")