from logging import exception
from data import medicine as md

'''Classe responsável pela interface com o usuário atráves do terminal'''
class Terminal:

    def main(self):
        print("\n######################### CONSULTA MEDICAMENTOS #########################")
        print(" Selecione uma das opções")
        option = input(" 1 - Consultar medicamento pelo nome\n 2 - Buscar pelo código de barras\n 3 - Comparativo PIS/COFINS\n 4 - Terminar o programa\n Insira aqui: ")
        return option

    def header(self, string):
        print("\n######################### " + string + " #########################")

    def data_input(self, option: int):
        if(option == 1):
            name = input(" Insira o nome: ")
            return name
        elif(option == 2):
            code = input(" Insira o código de barras: ")
            return code
        elif(option == 3):
            return None
        elif(option == 4):
            return None
        else:
            raise NotImplementedError

    def data_show_1(self, data):
        for medicine in data:
            print("Nome do medicamento: " + medicine.name + "\tProduto: " + medicine.product + "\tApresentação: " + medicine.presentation + "\tPF sem impost: " + medicine.pf)

    def data_show_2(self, data):
        print("Nome do medicamento com maior PMC: " + data[0].name + "PMC: " + str(data[0].pmc))
        print("Nome do medicamento com menor PMC: " + data[1].name + "PMC: " + str(data[1].pmc))
        print("Diferença entre os dois PMCs: " + str(data[0].pmc - data[1].pmc))


    def data_show_3(self, negative_percent, neutral_percent, positive_percent):
        print("CLASSIFICACAO\tPERCENTUAL\tTGRAFICO")
        print("Negativa\t" + str(negative_percent) + "\t" + "*"*int(negative_percent))
        print("Neutra  \t" + str(neutral_percent) + "\t" + "*"*int(neutral_percent))
        print("Positiva\t" + str(positive_percent) + "\t" + "*"*int(positive_percent))


    def error(self, error_message: str):
        print(error_message)

    def program_end(self):
        print(" Programa encerrado")