import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import subprocess
from login_model import LoginModel  # Importa corretamente a classe LoginModel

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.state("zoomed")  # Aumenta o tamanho da janela

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)  # Expande para ocupar o espaço disponível

        # Carregar e exibir a imagem na parte superior
        self.img = PhotoImage(file="usuario.png")  # Substitua pelo caminho correto da imagem
        self.lblImagem = tk.Label(self.frame, image=self.img)
        self.lblImagem.grid(row=0, column=0, columnspan=2, pady=10)  # Colocando a imagem no topo

        self.lblUsuario = tk.Label(self.frame, text="Usuário:", font=("Arial", 18))
        self.lblUsuario.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txtUsuario = tk.Entry(self.frame, font=("Arial", 18))
        self.txtUsuario.grid(row=4, column=1, padx=10, pady=10)

        self.lblSenha = tk.Label(self.frame, text="Senha:", font=("Arial", 18))
        self.lblSenha.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.txtSenha = tk.Entry(self.frame, font=("Arial", 18), show="*")
        self.txtSenha.grid(row=5, column=1, padx=10, pady=10)

        # Botão de Login
        self.btnLogin = tk.Button(self.frame, text="Login", font=("Arial", 18), command=self.realizar_login)
        self.btnLogin.grid(row=6, column=0, columnspan=2, pady=20)

        self.login_model = LoginModel()  # Inicializa o modelo de login

    def realizar_login(self):
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()

        # Aqui você deve verificar se o usuário existe
        usuario_encontrado = self.login_model.buscar_usuario(usuario)

        if usuario_encontrado:
            # Verifica se a senha fornecida corresponde à senha armazenada
            if usuario_encontrado[5] == senha:  # O índice 5 é onde a senha está armazenada
                self.abrir_principal()  # Chama a função para abrir a tela principal
            else:
                messagebox.showerror("Login", "Senha incorreta.")
        else:
            messagebox.showerror("Login", "Usuário não encontrado.")

    def abrir_principal(self):
        # Fecha a janela de login e abre principal.py
        self.root.destroy()  # Fecha a janela atual
        subprocess.Popen(['python', 'principal.py'])  # Abre o arquivo principal.py

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
