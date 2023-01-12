'''
Number Guessing Game
--------------------
'''

import random

def game():
    guess_attempts=0
    guess=random.randint(0,9)
    guess_player=0

    print(f'Witem w grze "Zgadnij liczbę"')

    run=input(f'Czy chcesz zagrać? \n(Tak/Nie)\n')

    if run.lower()=='nie':
        print(f'Do widzenia')
        return
    elif run.lower()=='tak':
        print(f'No to zaczynamy!')
    elif run=="":
        print(f'Nie podałeś odpowiedzi, więc zaczynamy grę!')
    else:
        print(f'Nie rozumiem, więc napisz jeszcze raz!')
        game()

    while guess!=guess_player:
        try:
            guess_player=int(input(f"Zgadnij liczbę pomiędzy 0 a 9: "))
            
            if guess_player<0 or guess_player>9:
                raise ValueError('Podaj liczbę z zakresu 0-9')
                
            if guess==guess_player:
                print(f'Gratulacje, zgadłeś!')
                print(f"Zajęło Ci to", guess_attempts, "prób do zgadnięcia liczby.")
                restart=input(f'Czy chcesz zagrać jeszcze raz?\n(Tak/Nie)\n')
                if restart.lower()=='nie':
                    print(f'Do widzenia')
                    break
                elif restart=="":
                    print(f'Nie podałeś odpowiedzi, więc zaczynamy od nowa!')
                    guess_attempts=0
                    guess=random.randint(0,9)
                    guess_player=0
                    continue
                else:
                    print(f'No to zaczynamy!')
                    guess_attempts=0
                    guess=random.randint(0,9)
                    guess_player=0
                    continue
            else:
                if guess_player<guess:
                    print(f'{guess_player} jest za mała')
                else:
                    print(f'{guess_player} jest za duża')

            guess_attempts+=1
        except ValueError as err:
            print(f'Wartość {guess_player} jest nieprawidłowa. {err}')
            
if __name__=='__main__':
    game()