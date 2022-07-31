class Credito:
    def __init__(self, monto, interes, plazo):
        self.monto = monto
        self.interes = interes
        self.plazo = plazo
        self.periodos = [None] * plazo

    def get_monto(self):
        return self.monto
    
    def get_interes(self):
        return self.interes
    
    def get_plazo(self):
        return self.plazo
    
    def get_periodos(self):
        return self.periodos