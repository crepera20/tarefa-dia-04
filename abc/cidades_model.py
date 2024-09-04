from Banco import Banco

class Cliente:
    def __init__(self):
        self.banco = Banco()  # Conexão ao banco de dados

    def inserir(self, nome, telefone, endereco, cpf, cidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cliente (nome, telefone, endereco, cpf, cidade)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, telefone, endereco, cpf, cidade))
        self.banco.conexao.commit()

    def alterar(self, idcli, nome, telefone, endereco, cpf, cidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cliente SET nome=?, telefone=?, endereco=?, cpf=?, cidade=?
            WHERE idcli=?
        ''', (nome, telefone, endereco, cpf, cidade, idcli))
        self.banco.conexao.commit()

    def excluir(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cliente WHERE idcli=?', (idcli,))
        self.banco.conexao.commit()

    def buscar(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cliente WHERE idcli=?', (idcli,))
        return cursor.fetchone()
