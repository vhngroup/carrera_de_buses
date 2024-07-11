import time
import random
import os
from bus import Bus

def console_clean(): 
    if os.name =='nt': # Valdiamos en que sistema operativo corre.
        os.system('cls')
    else:
        os.system('clear')

def main():
    bus1 = Bus()
    bus2 = Bus()
    print("CARRERA DE BUSES!!!")
    print("Colombia vs Uruguay")
    time.sleep(2)
    while True:
        console_clean()
        Bus.draw_start_runway()
        bus1.draw_bus(random.randint(1,2), "Colombia")
        Bus.draw_start_runway()
        bus1.draw_bus(random.randint(1,2), "Uruguay")
        Bus.draw_start_runway()
        if bus1.posicion>=100 or bus2.posicion >=100:
            if bus1.posicion >=100:
                print("Gana Colombia")
            else:
                print("Gana Uruguay")
            time.sleep(10)
            break

        time.sleep(0.1)

main()

