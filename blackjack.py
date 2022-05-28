import random
import os
import time

def run():

    baraja = ["1","2","3","4","5","6","7","8","9","10","11","12"]

    cartabanca1 = int(random.choice(baraja))
    
    cartajugador1 = int(random.choice(baraja))
    
    print(' *** BLACKJACK ***\n\n\n')
    print(cartajugador1)
    print('Es tu carta\n\n')
    print('\n Quieres carta?\n\n')
         
    eleccion =input()
    os.system("clear")
    
    if eleccion == 's':
        cartajugador2 = int(random.choice(baraja))
        print(cartajugador2)
        time.sleep(3)
        print(' *** BLACKJACK ***\n\n\n')
        eleccion2 = input('Quieres seguir? ')
        os.system("clear")
        
        if eleccion2 == 's':
            total = cartajugador1 + cartajugador2
            print(total)
                
            if total > 21:
                print(' *** BLACKJACK ***\n\n\n')
                print('Te has pasado, la banca gana...')
            else:
                print(' *** BLACKJACK ***\n\n\n')
                print('Quieres otra carta? ')
                eleccion3 = input()
            if eleccion3 == 'n':
                if cartabanca1 < 21:
                    cartabanca2 = int(random.choice(baraja))
                    totalbanca = cartabanca1 + cartabanca2
                    print(totalbanca)
                    time.sleep(3)
                    if totalbanca < 21:
                        cartabanca3 = int(random.choice(baraja))
                        totalbanca = totalbanca + cartabanca3
                        print(totalbanca)
                        time.sleep(3)
                         
    
    
    else:
        print('GANA LA BANCA !!!')
    
run()
