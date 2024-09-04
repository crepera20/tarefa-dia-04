from Banco import Banco

class Cliente:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, endereco, cpf, cidade):  # Adicionando cidade como parâmetro
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cliente (nome, telefone, endereco, cpf, cidade)
            VALUES (?, ?, ?, ?, ?)  -- Adicionei a coluna cidade aqui
        ''', (nome, telefone, endereco, cpf, cidade))  # Certifique-se de que todos os valores estão corretos
        self.banco.conexao.commit()

    def alterar(self, idcli, nome, telefone, endereco, cpf, cidade):  # Adicionando cidade como parâmetro
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cliente SET nome=?, telefone=?, endereco=?, cpf=?, cidade=?
            WHERE idcli=?
        ''', (nome, telefone, endereco, cpf, cidade, idcli))  # Adicionei a coluna cidade aqui
        self.banco.conexao.commit()

    def excluir(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cliente WHERE idcli=?', (idcli,))
        self.banco.conexao.commit()

    def buscar(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cliente WHERE idcli=?', (idcli,))
        return cursor.fetchone()