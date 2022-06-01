import os.path
import logic as l
import unicodedata
from data import medicine as md
from interface import terminal_interface as it


'''
Classe Manager
Descrição: Classe responsável por fazer a administração entre a interface com o usuário (frontend) e a lógica do programa (backend), armazenar e tratar os dados de entrada e de pesquisa e controlar em que estado o programa está.
'''
class Manager:

    '''
    Atributos: 
    interface (tipo terminal_interface): contém as funções de comunicação e interface com o usuário
    logic (tipo Logic): contém as funçãões responsável pela lógica do programa
    medicines (tipo Lista de Medicine): lista em que cada elemento contém dados de um remédio
    option (int): contém a opção de tarefa selecionada pelo usuário
    data (string): contém os dados de entrada do usuário
    exit_program (bool): contém estado de finalização do programa
    '''

    interface = it.Terminal()
    logic = l.Logic()
    medicines: md.Medicine() = []
    option: int = -1
    data: str = ""
    exit_program: bool = False

    '''
    Métodos:

    add_medicine():
    entrada: uma tupla que representa uma linha da base de dados
    saída: um elemento Medicine adicionado a lista de medicines
    objetivo: converter uma linha em formato de tupla para um objeto Medicine adicionado a lista, para facilitar consultas.
    '''
    def add_medicine(self, row):
        medicine = md.Medicine(*row)
        self.medicines.append(medicine)

    '''
    clear_medicines():
    entrada: nenhuma
    saída: lista vazia
    objetivo: limpar a lista de medicines, transformando ela em uma lista vazia.
    '''
    def clear_medicines(self):
        self.medicines = []

    '''treat_option():
    entrada: uma string que representa a opção de tarefa selecionada pelo usuário
    saída: um inteiro que representa a opção de tarefa selecionada pelo usuário
    objetivo: converte para int e trata exceções da opção de tarefa escolhida pelo usuário.
    Se não for possível converter para int ou está fora do intervalo 1 a 4, a opção é inválida e uma exceção será lançada.
    '''
    def treat_option(self, option):
        try: 
            option = int(option)
            if(option > 4 or option < 1):
                raise NotImplementedError
            return option
        except ValueError:
            self.interface.error(" Opção inválida: não é um número")
            return -1
        except NotImplementedError:
            self.interface.error(" Escolha uma opção éntre 1 e 4")
            return -1
    
    '''
    treat_data():
    entrada: uma string que representa os dados de entrada do usuário para uma tarefa
    saída: um inteiro ou uma string que representa os dados de entrada do usuário para uma tarefa
    objetivo: para a tarefa 4, converte para int se possível. Para as demais, filtra e converte para maiusculo a string em data.
    '''
    def treat_data(self, data):
        if(self.option == 2):
            try:
                data = int(data)
                return data
            except ValueError:
                self.interface.error(" Opção inválida: não é um número")
                return -1
            except NotImplementedError:
                self.interface.error(" Escolha uma opção éntre 1 e 2")
                return -1
        else:
            try:
                return self.lower_with_accent_to_upper(self.filter_string(data))
            except:
                self.interface.error("Ocorreu um erro com a entrada")
                return -1

    '''Filtra a string, retirnando aspas simples dela'''
    def filter_string(self, string):
        return string.replace("'", "")

    '''Retira ascentos e converte para letras maíusculas em toda a string'''
    def lower_with_accent_to_upper(self, string):
        processed_string = unicodedata.normalize("NFD", string)
        processed_string = processed_string.encode("ascii", "ignore")
        processed_string = processed_string.decode("utf-8")
        return processed_string.upper()   


    '''
    task_1():
    entrada: string que representa o nome de entrada do usuário para a tarefa
    saída: um vetor de objetos Medicine que representa os medicamentos consultados e um int -1 na opção de tarefa
    objetivo: chama uma consulta dos medicamentos similares ao nome consultado, cria um objeto Medicine para cada com o resultado e insere -1 em option voltar ao menu inicial.
    Se a pesquisa retornar None, chama a interface para imprimir um erro.
    '''
    def task_1(self):
        consult = self.logic.consult_name(self.data)
        self.interface.header("RESULTADO DA PESQUISA")
        if(consult is None):
            self.interface.error(" Nenhuma medicamento encontrado com este nome")
        else:
            for medicine in consult:
                self.add_medicine(medicine)
            self.interface.data_show_1(self.medicines)

        self.option = -1

    '''
    task_2():
    entrada: string que representa o código de entrada do usuário para a tarefa
    saída: dois objetos Medicine que representa a bolsa consultada e um int -1 na opção de tarefa
    objetivo: chama uma consulta por medicamentos através do código de barra e imprime o com maior e menor PMC e a diferença.
    Se a pesquisa retornar None, chama a interface para imprimir um erro.
    '''
    def task_2(self):
        if(self.data != -1):
            consult = self.logic.consult_code(self.data)
            self.interface.header("RESULTADO DA PESQUISA")
            if(consult is None):
                self.interface.error(" Nenhum remédio encontrado com este código")
            else:
                for medicine in consult:
                    self.add_medicine(medicine)
                self.interface.data_show_2(self.medicines)

        self.option = -1

    '''
    task_3():
    entrada:
    saída: um float que representa a média da pesquisa e um int -1 na opção de tarefa
    objetivo: chama uma consulta de Logic para encontrar a porcentagem de avaliações dos medicamentos, retorna o resultado e insere -1 em option voltar ao menu inicial.
    Se a pesquisa retornar None, chama a interface para imprimir um erro.
    '''
    def task_3(self):
        negative_percent, neutral_percent, positive_percent = self.logic.compare()
        self.interface.header("RESULTADO DA PESQUISA")
        self.interface.data_show_3(negative_percent, neutral_percent, positive_percent)
        self.option = -1

    '''
    task_4():
    entrada: nenhuma
    saída: booleano que representa fim de execução do programa
    objetivo: atribui True a variavel exit_pogram para encerrar o programa e chama interface para imprimir que o programa está sendo encerrado.
    '''
    def task_4(self):
        self.interface.program_end()
        self.exit_program = True
            
    '''
    main():
    entrada: nenhuma
    saída: nenhuma
    objetivo: primeira função chamada pelo programa. Responsável por receber as informações do usuário, tratá-las e escolher qual tarefa será feita com seus respectivos dados baseado nas informação. 
    Cria base de dados caso ela não exista. Tem o loop principal do programa que ficará ativo até a opção 5 ser selecionada.
    '''
    def main(self):
        path_file = os.getcwd() + "\\data\\" + "meds.db"
        if(not os.path.exists(path_file)):
            self.logic.create_database()
        while(not self.exit_program):
            self.clear_medicines()
            if(self.option == -1):
                self.option = self.treat_option(self.interface.main())
            else:
                self.data = self.interface.data_input(self.option)
                if(self.option == 1):
                    self.data = self.treat_data(self.data)
                    self.task_1()
                elif(self.option == 2):
                    self.data = self.treat_data(self.data)
                    self.task_2()
                elif(self.option == 3):
                    self.task_3()
                elif(self.option == 4):
                    self.task_4()
            
 
if __name__ == '__main__' :
    manager = Manager()
    manager.main()