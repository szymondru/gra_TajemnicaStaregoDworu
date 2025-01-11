# TAJEMNICA STAREGO DWORU
# Gra tekstowa, w której wcielasz się w postać młodego detektywa, który otrzymuje tajemniczy list, 
# w którym nieznany nadawca prosi go o pomoc w rozwiązaniu zagadki zniknięcia dziedzica Starego Dworu. 
# Dwór, ukryty głęboko w lesie, skrywa mroczne sekrety, które tylko Ty możesz odkryć. 
# Musisz podjąć decyzje, które wpłyną na dalszy rozwój fabuły. 
# Czy uda Ci się rozwiązać zagadkę i odnaleźć dziedzica? 
# To zależy od Twoich wyborów.



import random
import time



# Funkcje

def dalej():
    time.sleep(3)
    input('\n\rWciśnij "Enter", aby przejść dalej. \n')

def wybor(odpowiedz):
    try:
        odpowiedz = odpowiedz.strip().lower()
        if odpowiedz == 'exit':
            print('\n\r'
                  'Postanawiasz zakończyć grę.')
            koniec()
        odpowiedzi = {'tak': True, 't': True, 'nie': False, 'n': False}
        while odpowiedz not in odpowiedzi:
            print('\n\r'
                  'Podana przez Ciebie odpowiedź jest niepoprawna. Jeśli chcesz zakończyć grę, wpisz: \"exit\". ')
            odpowiedz = input('\n\r'
                              'Wpisz poprawną odpowiedź (tak/nie), aby kontynuować grę : ').strip().lower()
        return odpowiedzi[odpowiedz]
    except Exception as blad:
        print(f"Wystąpił nieoczekiwany błąd: {blad}")
        koniec()

koniec_gry = False

def wahanie_koniec_gry(odpowiedz):
    odpowiedz = input('\n\r'
                      'Po chwili zaczynasz mieć wątpliwości co do ostatniej decyzji. Czy chcesz ją zmienić?: ')
    if wybor(odpowiedz):
        print('\n\rZmieniasz swój wybór. ')
        time.sleep(2)
        print('Gra toczy się dalej. ')
        time.sleep(2)
    else:
        global koniec_gry
        koniec_gry = True

def koniec():
    time.sleep(2)
    print('\n\n\rKONIEC GRY\n\n')
    time.sleep(2)
    input(' \n\rWciśnij "Enter", aby zakończyć grę. \n ')
    exit()



# Funkcje zawierające instrukcje 3 głównych etapów gry i bardziej skomplikowanych możliwości wewnątrz nich

# ETAP 1: Droga do Starego Dworu

def etap1():
    odpowiedz = input('\n\rPodczas drogi do dworu napotykasz rozwidlenie dróg. '
                      'Jedna ścieżka prowadzi przez ciemny las, druga jest dłuższa, ale bardziej uczęszczana. '
                      '\nCo robisz? Czy wybierasz ścieżkę prowadzącą w lewo (w stronę ciemnego lasu)?: ')
    if wybor(odpowiedz):
        if random.choice([True, False]):
            print('\n\r'
                  'Ścieżka prowadzi przez mroczny las, ale udaje Ci się dotrzeć do dworu bez problemów.')
        else:
            walka_ze_zwierzeciem()     
    else:
        print('\n\r'
              'Zdecydowałeś się wybrać dłuższą, ale bardziej bezpieczną drogę. '
              'Mimo że podróżujesz wolniej, jesteś pewniejszy, że dojdziesz do celu bez większych problemów. '
              'Po pewnym czasie dostrzegasz zarys starego dworu. ')            
    dalej()

# ETAP 1: Ewentualna walka ze zwierzęciem

def walka_ze_zwierzeciem():
    odpowiedz = input('\n\r'
        'W drodze do rozwidlenia natrafiasz na dzikie zwierzę, które stanowi realne zagrożenie. '
        'Zwierzę wyłania się zza drzew i rusza w Twoją stronę. Czy próbujesz je odstraszyć?: ')
    time.sleep(2)
    if wybor(odpowiedz):
        print('\n\r'
              'Walczysz z dzikim zwierzęciem, które próbuje Cię zaatakować.')
        time.sleep(3)
        print('\n\r'
              'Udało Ci się odstraszyć zwierzę, używając ostrego kamienia i swojego instynktu. '
              'Wracasz na właściwą drogę, ale straciłeś sporo czasu.')
    else:
        print('\n\r'
              'Zwierzę zaatakowało Cię, zmuszając Cię do ucieczki. '
              'Straciłeś cenny czas, ale udało Ci się przeżyć. Decydujesz się wrócić na początek ścieżki i pójść drugą trasą.')
        odpowiedz = input('\n\r'
                          'Docierasz ponownie do rozwidlenia. '
                          'Czy podejmujesz się dalszej próby poszukiwania Dziedzica?: ')
        if wybor(odpowiedz):
            print('\n\rWyruszasz w dalszą podróż. ')
        else:
            wahanie_koniec_gry(odpowiedz)
            if koniec_gry:
                print('\n\r'
                'Po ciężkim starcie z dzikim zwierzęciem postanawiasz wrócić do domu. '
                'Tajemnica pozostaje nierozwiązana. ')
                koniec()



# ETAP 2: Stary Dwór

def etap2():
    odpowiedz = input('\n\r'
        'W końcu docierasz do Starego Dworu. Mimo że z zewnątrz wygląda na opuszczony, w środku czuć tajemniczy klimat. '
        'Ciężkie powietrze, zapach stęchlizny i ciche odgłosy dochodzące z piwnicy sprawiają, że zaczynasz się niepokoić. '
        'Zauważasz dwie drogi: jedna prowadzi w dół, do piwnicy, a druga na górę, do zapomnianych pokoi na piętrze. '
        'Co robisz? Czy schodzisz do piwnicy?: ')
    odpowiedz = wybor(odpowiedz)
    if odpowiedz:
        losowe_etap2 = random.choice([True, False])
        if losowe_etap2:
            dziennik()
        else:
            czlowiek()
    else:
        obraz()

# ETAP 2: Dziennik

def dziennik():
    print('\n'
          'W ostatnim pomieszczeniu piwnicy znajdujesz tajemniczy dziennik. '
          'Jest stary, pokryty kurzem i zarośnięty pajęczynami, '
          'ale po kilku chwilach zagłębiania się w jego treść odkrywasz, że dziedzic dworu miał '
          'podejrzanych przyjaciół i sekrety, które mogły doprowadzić do jego zniknięcia. '
          'Dziennik zawiera wskazówki, które prowadzą Cię dalej. ')
    dalej()
    etap3()

# ETAP 2: Obraz

def obraz():
    odpowiedz = input('\n'
                      'Postanawiasz udać się na górę. Tam znajdujesz stary obraz przedstawiający '
                      'dziedzica dworu. Obraz zdaje się Cię dziwnie przyciągać. Czy zbliżasz się, '
                      'by przyjrzeć się obrazowi bliżej?: ')
    odpowiedz = wybor(odpowiedz)
    if odpowiedz:
        print('\n'
              'W obrazie dostrzegasz ukryty mechanizm, który po lekkim naciśnięciu odsłania '
              'tajemne przejście prowadzące do ukrytej komnaty. Wchodzisz do środka i odkrywasz '
              'więcej wskazówek, które pomogą Ci rozwiązać zagadkę. \n')
        dalej()
    else:
        print('\n'
              'Obraz nie wzbudza Twojego zainteresowania. Podążasz dalej, ale czujesz, '
              'że coś umknęło Ci sprzed oczu. Wkrótce opuszczasz piętro. ')
        wahanie_koniec_gry(odpowiedz)
        if koniec_gry:
            print('W budynku nie znajdujesz niczego, co mogłoby pomóc Ci w rozwiązaniu zagadki. '
            'Postanawiasz wrócić do domu. Tajemnica pozostaje nierozwiązana. ')
            koniec()

# Etap 2: Tajemniczy nieznajomy

def czlowiek():
    odpowiedz = input('\n'
                      'W piwnicy spotykasz dziwnego, zamyślonego człowieka. Jego oczy są pełne niepokoju, '
                      'jakby coś przed nim ukrywał. Czy pytasz go o pomoc?: ')
    odpowiedz = wybor(odpowiedz)
    if odpowiedz:
        print('\n'
            'Człowiek opowiada Ci o sekretach dworu i wspomina o dziwnych wydarzeniach sprzed lat, '
            'ale nie jest całkiem szczery. Wydaje się coś ukrywać, a może nawet zmyślać. Postanawiasz '
            'zaufać intuicji i przyjąć jego opowieść z rezerwą. \n'
            'Mijasz go i idziesz zbadać pozostałą część. ')
        dziennik()
    else:
        print('\n'
              'Zignorowałeś człowieka i zdecydowałeś się kontynuować poszukiwania samodzielnie. '
              'Czułeś, że coś jest nie tak, ale nie miałeś zamiaru się w to wciągać. Wychodzisz z piwnicy.')
        obraz()
    dalej()



# ETAP 3: Zakończenie

def etap3():
    odpowiedz = input('\n'
        'Dzięki zebranym wskazówkom i informacjom zaczynasz układać obraz całej sprawy. '
        'Dowiadujesz się, że dziedzic Starego Dworu został porwany przez swojego wspólnika w interesach, '
        'który zagrał na jego zaufaniu. Porwanie miało miejsce na tle finansowych rozgrywek, a dwór skrywał '
        'wiele nielegalnych transakcji i tajemniczych powiązań. Znalezione przez ciebie notatki zawierały '
        'liczne informacje na temat wspólnika-porywacza i jego kryjówki.\nCzy chcesz wezwać policję, aby '
        'pomogła Ci uwolnić dziedzica?: ')
    odpowiedz = wybor(odpowiedz)
    if odpowiedz:
        print('\nPolicja przybywa na miejsce i udaje Ci się uwolnić dziedzica. Sprawa zostaje wyjaśniona. '
              '\nGRATULACJE! Udało Ci się rozwiązać zagadkę. ')
    else:
        if wahanie_koniec_gry(odpowiedz):
            print('\nPolicja przybywa na miejsce i udaje Ci się uwolnić dziedzica. Sprawa zostaje wyjaśniona. '
              '\nGRATULACJE! Udało Ci się rozwiązać zagadkę. ')
        else:
            print('\nPostanawiasz działać na własną rękę. Próbujesz uwolnić dziedzica, ale porywacz Cię przechytrza. '
            'Ogłusza cię i ucieka. \nDziedzic pozostaje zaginiony. ')
            koniec()



# Kod główny gry

print(' \nTAJEMNICA STAREGO DWORU \n ')
print('\n'
    'Jako młody detektyw otrzymujesz tajemniczy list, w którym nieznany nadawca prosi Cię o pomoc '
    'w rozwiązaniu zagadki zniknięcia dziedzica Starego Dworu. Dwór, ukryty głęboko w lesie, skrywa '
    'mroczne sekrety, które tylko Ty możesz odkryć. Wybierz, którą drogą pójdziesz, i dowiedz się, '
    'co naprawdę wydarzyło się w tym zapomnianym miejscu. Czeka Cię niebezpieczna przygoda, pełna '
    'tajemnic i nieoczekiwanych decyzji. \n\nW trakcie gry odpowiadaj na pytania: (tak/nie). \n'
    'Jeśli postanowisz przedwcześnie zakończyć grę, wpisz: \"exit\". \n\n')
dalej()
odpowiedz = input('\n'
    'Otrzymujesz list od nieznanego nadawcy, który prosi Cię o pomoc w rozwiązaniu zagadki zniknięcia '
    'dziedzica starego dworu. Podobno od czasu jego zniknięcia dwór opustoszał, a w okolicznych wsiach '
    'zaczęły krążyć niepokojące plotki. Czy przyjmujesz to wyzwanie?: ')
odpowiedz = wybor(odpowiedz)
if odpowiedz:
    print('\n'
        'Wyruszasz w podróż do Starego Dworu ukrytego głęboko w lesie. '
        'Droga jest długa, pełna niebezpieczeństw, ale także pełna tajemnic, które musisz odkryć. '
        'Wiesz, że ta sprawa nie będzie łatwa, ale zdeterminowany, aby znaleźć odpowiedzi, '
        'podążasz przed siebie. ')
    etap1()
    etap2()
    etap3()
else:
    wahanie_koniec_gry(odpowiedz)
    if koniec_gry:
        print('\n'
        'Postanawiasz zostać w domu. Tajemnica pozostaje nierozwiązana. ')
koniec()



# Koniec gry.
