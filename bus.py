class Bus:
    def __init__(self):
        self.posicion = 0

    @staticmethod
    def draw_start_runway():
        print("----------------------------------------------------")

    def draw_bus(self, desface, nombre):
        self.posicion += desface
        print("                                     ")
        print("  " * self.posicion + nombre)
        print("  " * self.posicion + "-----------")
        print("  " * self.posicion +  "|_|_|_|_|_|_")
        print("  " * self.posicion + "|           |")
        print("  " * self.posicion +  "|---0-------0-|")
    
    @staticmethod
    def draw_end_runway():
        print("----------------------------------------------------")