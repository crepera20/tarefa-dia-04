import tkinter as tk
from tkinter import messagebox
import os
from usuarios_model import Usuario

class Application:
    def __init__(self, root):
        self.usuario = Usuario()

        self.root = root
        self.root.title("Cadastro de Usuários")
        self.root.state("zoomed")

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Widgets
        self.lblIdUsuario = tk.Label(self.frame, text="ID do Usuário:", font=("Arial", 18))
        self.lblIdUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtIdUsuario = tk.Entry(self.frame, font=("Arial", 18))
        self.txtIdUsuario.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = tk.Button(self.frame, text="Buscar", command=self.buscar_usuario, font=("Arial", 18))
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        self.lblTelefone = tk.Label(self.frame, text="Telefone:", font=("Arial", 18))
        self.lblTelefone.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.txtTelefone = tk.Entry(self.frame, font=("Arial", 18))
        self.txtTelefone.grid(row=2, column=1, padx=10, pady=10)

        self.lblEmail = tk.Label(self.frame, text="E-mail:", font=("Arial", 18))
        self.lblEmail.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.txtEmail = tk.Entry(self.frame, font=("Arial", 18))
        self.txtEmail.grid(row=3, column=1, padx=10, pady=10)

        self.lblUsuario = tk.Label(self.frame, text="Usuário:", font=("Arial", 18))
        self.lblUsuario.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txtUsuario = tk.Entry(self.frame, font=("Arial", 18))
        self.txtUsuario.grid(row=4, column=1, padx=10, pady=10)

        self.lblSenha = tk.Label(self.frame, text="Senha:", font=("Arial", 18))
        self.lblSenha.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.txtSenha = tk.Entry(self.frame, font=("Arial", 18), show="*")
        self.txtSenha.grid(row=5, column=1, padx=10, pady=10)

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_usuario, font=("Arial", 18))
        self.btnInserir.grid(row=6, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_usuario, font=("Arial", 18))
        self.btnAlterar.grid(row=6, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_usuario, font=("Arial", 18))
        self.btnExcluir.grid(row=6, column=2, padx=10, pady=10)

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def buscar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        try:
            idUsuario = int(idUsuario)
            resultado = self.usuario.buscar(idUsuario)
            if resultado:
                self.txtNome.delete(0, tk.END)
                self.txtNome.insert(tk.END, resultado[1])
                self.txtTelefone.delete(0, tk.END)
                self.txtTelefone.insert(tk.END, resultado[2])
                self.txtEmail.delete(0, tk.END)
                self.txtEmail.insert(tk.END, resultado[3])
                self.txtUsuario.delete(0, tk.END)
                self.txtUsuario.insert(tk.END, resultado[4])
                self.txtSenha.delete(0, tk.END)
                self.txtSenha.insert(tk.END, resultado[5])
                messagebox.showinfo("Sucesso", "Busca realizada com sucesso!")
            else:
                messagebox.showerror("Erro", "Usuário não encontrado!")
        except ValueError:
            messagebox.showerror("Erro", "ID do usuário deve ser um número.")

    def inserir_usuario(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()

        if nome and telefone and email and usuario and senha:
            try:
                self.usuario.inserir(nome, telefone, email, usuario, senha)
                messagebox.showinfo("Sucesso", "Usuário inserido com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao inserir usuário: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def alterar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()

        if idUsuario and nome and telefone and email and usuario and senha:
            try:
                self.usuario.alterar(idUsuario, nome, telefone, email, usuario, senha)
                messagebox.showinfo("Sucesso", "Usuário alterado com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao alterar usuário: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def excluir_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        if idUsuario:
            try:
                self.usuario.excluir(idUsuario)
                messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir usuário: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, insira o ID do usuário para excluir!")

    def limpar_campos(self):
        self.txtIdUsuario.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtTelefone.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)
        self.txtUsuario.delete(0, tk.END)
        self.txtSenha.delete(0, tk.END)

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
