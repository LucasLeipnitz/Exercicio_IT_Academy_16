from data import csvreader as rd
from data import database as db

'''
Classe Logic
Descrição: Classe responsável pela lógica das tarefas do programa. Armazena dois objetos responsáveis por fazer a comunicação com o banco de dados e o arquivo CSV disponibilizado.
'''
class Logic:
    
    '''
    Atributos: 
    base (tipo DBConnect): contém as funções responsáveis por conectar e fazer as consultas com o banco de dados 
    csv_reader (tipo CSVReader): contém funções e variáveis responsáveis por ler o arquivo csv e armazenar as linhas do arquivo em memória
    '''
    base = db.DBConnect()
    csv_reader = rd.CSVReader('TA_PRECO_MEDICAMENTO.csv')
    
    '''
    Métodos:

    create_database()
    entrada: nenhuma
    saída: nenhuma
    objetivo: responsável por criar o arquivo SQLite do banco de dados e a tabela Medicamentos, chamar csv_reader para ler o arquivo csv e salvar as linhas em memória e adicionar cada linha ao banco dados.
    '''
    def create_database(self):
        self.base.open_connection()
        self.base.init_db()
        self.csv_reader.load_in_memory()
        for row in self.csv_reader.data:
            self.base.add_row(row)
        self.base.commit()
        self.base.close_connection()  

    '''
    consult_name():
    entrada: string que contém o nome a ser consultado
    saída: lista de tuplas que representa a consulta
    objetivo: chama base para fazer a consulta de medicamentos que completam o nome inserido.
    '''
    def consult_name(self, name):
        self.base.open_connection()
        consult = self.base.select_by_name(name)
        self.base.close_connection()
        meds = []
        for medicine in consult:
            new_med = []
            new_med.append(medicine[0])
            new_med.append(medicine[8])
            new_med.append(medicine[9])
            new_med.append(medicine[13])
            new_med.append(medicine[23])
            meds.append(tuple(new_med))
        return meds

    '''
    consult_code():
    entrada: string que contém o código a ser consultado
    saída: lista de tuplas que representa a consulta
    objetivo: chama base para fazer a consulta de medicamentos com o código inserido.
    '''
    def consult_code(self, code):
        self.base.open_connection()
        consult = self.base.select_by_code(code)
        self.base.close_connection()
        meds = []
        new_med = []
        new_med.append(consult[0][0])
        new_med.append(consult[0][8])
        new_med.append(consult[0][9])
        new_med.append(float(consult[0][13].replace(',','.')))
        new_med.append(float(consult[0][23].replace(',','.')))
        meds.append(tuple(new_med))
        new_med = []
        new_med.append(consult[-1][0])
        new_med.append(consult[-1][8])
        new_med.append(consult[-1][9])
        new_med.append(float(consult[-1][13].replace(',','.')))
        new_med.append(float(consult[-1][23].replace(',','.')))
        meds.append(tuple(new_med))
        return meds

    def compare(self):
        self.base.open_connection()
        neutral_counter = self.base.count_by_pis_cofins("Neutra")[0][0]
        positive_counter = self.base.count_by_pis_cofins("Positiva")[0][0]
        negative_counter = self.base.count_by_pis_cofins("Negativa")[0][0]
        self.base.close_connection()

        total = negative_counter + neutral_counter + positive_counter
        negative_percent = negative_counter*100/total
        positive_percent = positive_counter*100/total
        neutral_percent = neutral_counter*100/total
        return negative_percent, neutral_percent, positive_percent

logic = Logic()
#print(logic.consult_name("MONTELUCASTE")[0][0])
logic.consult_name("MONTELUCASTE")
#consult1, consult2 = logic.consult_code('7891317421618')
#print(consult1[23])
#print(consult2[23])
#print(logic.compare())