import sqlite3
import pathlib

'''
Classe DBConnect
Descrição: Classe responsável por fazer a comuniação com o banco de dados.
'''
class DBConnect:

    #variável que armazena a conexão do banco  
    con: sqlite3.Connection

    #abre a conexão com o banco
    def open_connection(self):
        self.con = sqlite3.connect(pathlib.Path('data/meds.db'))

    #fecha a conexão com o banco
    def close_connection(self):
        self.con.close()

    #faz o commit das alterações no banco
    def commit(self):
        self.con.commit()

    #inicializa a tabela no banco de dados
    def init_db(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE Medicamento (SUBSTANCIA, CNPJ, LABORATORIO, CODIGO_GGREM, REGISTRO, EAN_1, EAN_2, EAN_3, PRODUTO, APRESENTACAO, CLASSE_TERAPEUTICA, TIPO, REGIME_DE_PREÇO, PF_SEM_IMPOSTO, PF_0, PF_12, PF_17, PF_17_ALC, PF_17_5, PF_17_5_ALC, PF_18, PF_18_ALC, PF_20, PMC_0, PMC_12, PMC_17, PMC_17_ALC, PMC_17_5, PMC_17_5_ALC, PMC_18, PMC_18_ALC, PMC_20, RESTRICAO_HOSPITALAR, CAP, CONFAZ_87, ICMS_0, ANALISE_RECURSAL, PIS_COFINS, COMERCIALIZACAO_2020, TARJA)")

    #adiciona uma linha ao banco de dados. Row é um dicionário, portanto é preciso fazer a conversão dos valores do dicionário para uma tupla
    def add_row(self, row):
        cur = self.con.cursor()
        cur.execute("INSERT INTO Medicamento VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(row.values()))
    
    #seleciona medicamento por nome escolhido
    def select_by_name(self, name):
        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM Medicamento WHERE SUBSTANCIA LIKE '%{name}%' AND COMERCIALIZACAO_2020 == 'Sim'")
        return cur.fetchall()

    #seleciona medicamento por nome escolhido
    def select_by_code(self, code):
        cur = self.con.cursor()
        cur.execute(f"SELECT * FROM Medicamento WHERE EAN_1 == '{code}' ORDER BY PMC_0")
        return cur.fetchall()

    #conta número de medicamentos por parâmetro
    def count_by_pis_cofins(self, param):
        cur = self.con.cursor()
        cur.execute(f"SELECT count(PIS_COFINS) FROM Medicamento where PIS_COFINS == '{param}'")
        return cur.fetchall()
