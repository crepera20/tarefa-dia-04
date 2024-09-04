from Banco import Banco

class LoginModel:
    def __init__(self):
        self.banco = Banco()

    def buscar_usuario(self, usuario):
        # Consulta o banco de dados para verificar se o usuário existe
        try:
            # Supondo que a classe Banco tenha um método `buscar_usuario`
            usuario_encontrado = self.banco.buscar_usuario(usuario)

            if usuario_encontrado:
                print(f"Usuário encontrado: {usuario_encontrado}")
                return usuario_encontrado
            else:
                print("Usuário não encontrado.")
                return None
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o usuário: {e}")
            return None
