import csv
from collections import Counter
import re
import unittest

class CalculaGanador:
    @staticmethod
    def dni_valido(dni):
        return re.fullmatch(r'\d{8}', dni) is not None

    def leer_datos(self, archivo):
        try:
            with open(archivo, 'r') as csvfile:
                next(csvfile) 
                datareader = csv.reader(csvfile)
                return [fila for fila in datareader if fila[5] == '1' and self.dni_valido(fila[3])]
        except IOError:
            raise Exception("Error al leer el archivo")

    def calcular_ganador(self, data):
        total_votos = len(data)
        votos_por_candidato = Counter(fila[4] for fila in data)
        candidato_mayoria, votos_mayoria = votos_por_candidato.most_common(1)[0]

        if votos_mayoria > total_votos / 2:
            return [candidato_mayoria]
        else:
            return [candidato for candidato, _ in votos_por_candidato.most_common(2)]

class TestCalculaGanador(unittest.TestCase):
    def setUp(self):
        self.cg = CalculaGanador()

    def test_dni_valido(self):
        self.assertTrue(self.cg.dni_valido("12345678"))
        self.assertFalse(self.cg.dni_valido("1234567"))  
        self.assertFalse(self.cg.dni_valido("123456789"))
        self.assertFalse(self.cg.dni_valido("1234567a"))

    def test_calcula_ganador(self):
        
        data_test = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Candidato1', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Candidato1', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Candidato2', '1'],
        ]
        self.assertEqual(self.cg.calcular_ganador(data_test), ['Candidato1'])

    def test_calculo_con_datos_csv(self):
        
        datos_reales = self.cg.leer_datos('0204.csv')
        resultado_real = self.cg.calcular_ganador(datos_reales)

        self.assertEqual(resultado_real, ['CandidatoEsperado'], "Debería haber un ganador claro.")
        
if __name__ == '__main__':
    unittest.main()
