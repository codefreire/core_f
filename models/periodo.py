class Periodo:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.cuota = 0.0
        self.capital_inicio = 0.0
        self.interes = 0.0
        self.abono_capital = 0.0
        self.saldo = 0.0
    
    def get_cantidad(self):
        return self.cantidad
    
    def get_cuota(self):
        return self.cuota
    
    def set_cuota(self, cuota):
        self.cuota = cuota

    def get_capital_inicio(self):
        return self.capital_inicio
    
    def set_capital_inicio(self, capital_inicio):
        self.capital_inicio = capital_inicio
    
    def get_interes(self):
        return self.interes
    
    def set_interes(self, interes):
        self.interes = interes
    
    def get_abono_capital(self):
        return self.abono_capital
    
    def set_abono_capital(self, abono_capital):
        self.abono_capital = abono_capital
    
    def get_saldo(self):
        return self.saldo
    
    def set_saldo(self, saldo):
        self.saldo = saldo