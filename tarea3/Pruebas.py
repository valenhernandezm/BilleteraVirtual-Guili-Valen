'''
Created on May 11, 2016

@author: valentina
'''
import unittest
from BilleteraElectronica import *

class BilleteraTest(unittest.TestCase):
    def testBilleteraElectronicaExiste(self):
        BilleteraElectronica()
        
    def TestConstructBEExist(self):
        BilleteraElectronica("AfJ556tY", "Giuli", "Latella", 20173131, 0810596)