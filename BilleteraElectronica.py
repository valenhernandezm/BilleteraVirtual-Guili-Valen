from decimal import Decimal
from datetime import datetime

class BilleteraElectronica:
    
    def __init__(self, ID, nombres, apellidos, CI, PIN):
        self.ID = ID
        self.nombres = nombres
        self.apellidos = apellidos
        self.CI = CI
        self.PIN = PIN
        self.creditos = []
        self.debitos = []
        self.balance = 0
        
