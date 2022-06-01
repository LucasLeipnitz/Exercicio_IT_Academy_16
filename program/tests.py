import unittest
import tests_answers as answers
from data import csvreader as rd
from data import database as db

'''
Classes responsáveis pelos testes de unidade de CSVReader
'''
class TestReaderMethods(unittest.TestCase):
    
    csv_reader = rd.CSVReader('TA_PRECO_MEDICAMENTO.csv')

    def test_absolute_name(self):
        self.assertEqual(self.csv_reader.absolute_name, answers.TEST_1_READER_ANSWER)

    def test_load_in_memory_first_element(self):
        index = 0
        attribute = 'CNPJ'
        self.csv_reader.load_in_memory()
        self.assertEqual(self.csv_reader.data[index][attribute], answers.TEST_2_READER_ANSWER)

    def test_load_in_memory_last_element(self):
        index = -1
        attribute = 'CNPJ'
        self.csv_reader.load_in_memory()
        self.assertEqual(self.csv_reader.data[index][attribute], answers.TEST_3_READER_ANSWER)

    def test_load_in_memory_intermediary_element(self):
        index = 10
        attribute = 'CNPJ'
        self.csv_reader.load_in_memory()
        self.assertEqual(self.csv_reader.data[index][attribute], answers.TEST_4_READER_ANSWER)

    def test_attribute_1(self):
        index = 10
        attribute = "SUBSTÂNCIA"
        self.csv_reader.load_in_memory()
        self.assertEqual(self.csv_reader.data[index][attribute], answers.TEST_5_READER_ANSWER)

    def test_attribute_2(self):
        index = 10
        attribute = "PRODUTO"
        self.csv_reader.load_in_memory()
        self.assertEqual(self.csv_reader.data[index][attribute], answers.TEST_6_READER_ANSWER)

    '''
Classes responsáveis pelos testes de unidade de DBConnect
'''
class TestDBMethods(unittest.TestCase):
    
    base = db.DBConnect()
    
    def test_select_by_name_1(self):
        self.base.open_connection()
        consult = self.base.select_by_name("MONTELUCASTE")
        self.assertEqual(consult[0][13], answers.TEST_1_DB_ANSWER)
        self.base.close_connection()

    def test_select_by_name_2(self):
        self.base.open_connection()
        consult = self.base.select_by_name("MONTELUCASTE")
        self.assertEqual(consult[-1][13], answers.TEST_2_DB_ANSWER)
        self.base.close_connection()

    def test_select_by_code_1(self):
        self.base.open_connection()
        consult1, consult2 = self.base.select_by_code("7891317421618")
        self.assertEqual(consult1[23], answers.TEST_3_DB_ANSWER)
        self.base.close_connection()

    def test_select_by_pis_cofins(self):
        self.base.open_connection()
        consult = self.base.count_by_pis_cofins("Neutra")
        self.assertEqual(consult[0][0], answers.TEST_4_DB_ANSWER)
        self.base.close_connection()
    
    def test_select_by_pis_cofins(self):
        self.base.open_connection()
        consult = self.base.count_by_pis_cofins("Positiva")
        self.assertEqual(consult[0][0], answers.TEST_5_DB_ANSWER)
        self.base.close_connection()

    def test_select_by_pis_cofins(self):
        self.base.open_connection()
        consult = self.base.count_by_pis_cofins("Negativa")
        self.assertEqual(consult[0][0], answers.TEST_6_DB_ANSWER)
        self.base.close_connection()
        

if __name__ == '__main__':
    unittest.main()