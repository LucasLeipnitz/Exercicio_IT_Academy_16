from argparse import FileType
import pathlib
import csv
import os.path

'''
Classe CSVReader
Descrição: Classe responsável por ler o arquivo csv e armazenar as informações dele em memória
'''
class CSVReader:

    csvfile: FileType
    absolute_name: str
    data = []

    #inicializa a classe com o caminho absoluto do arquivo csv.
    def __init__(self, file_name):
        self.absolute_name = os.getcwd() / pathlib.Path("data") /  pathlib.Path(file_name)

    #abre o arquivo csv para leitura.
    def open_file(self):
        self.csvfile = open(self.absolute_name, newline='')

    #fecha o arquivo csv.
    def close_file(self):
        self.csvfile.close()

    #carrega em data uma lista de todas as linhas, onde cada linha é um dicionário com a chave sendo a informação do header do arquivo e o valor sendo o valor de cada coluna da informação.
    def load_in_memory(self):
        self.open_file()
        reader = csv.DictReader(self.csvfile, delimiter=";")
        for row in reader:
            self.data.append(row)
        self.close_file()