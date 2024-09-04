import tkinter as tk
from tkinter import messagebox
import os
from cidades_model import Cliente  # Altere para Cliente

class CityApp:
    def __init__(self, root):
        self.cliente = Cliente()  # Altere para Cliente()

        self.root = root
        self.root.title("Cadastro de Cidades")
        self.root.state("zoomed")  # Maximiza a janela

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Widgets
        self.lblIdCidade = tk.Label(self.frame, text="ID da Cidade:", font=("Arial", 18))
        self.lblIdCidade.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtIdCidade = tk.Entry(self.frame, font=("Arial", 18))
        self.txtIdCidade.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = tk.Button(self.frame, text="Buscar", command=self.buscar_cidade, font=("Arial", 18))
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        self.lblNome = tk.Label(self.frame, text="Nome da Cidade:", font=("Arial", 18))
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        self.lblUF = tk.Label(self.frame, text="UF:", font=("Arial", 18))
        self.lblUF.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.txtUF = tk.Entry(self.frame, font=("Arial", 18))
        self.txtUF.grid(row=2, column=1, padx=10, pady=10)

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_cidade, font=("Arial", 18))
        self.btnInserir.grid(row=3, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_cidade, font=("Arial", 18))
        self.btnAlterar.grid(row=3, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_cidade, font=("Arial", 18))
        self.btnExcluir.grid(row=3, column=2, padx=10, pady=10)

        self.lblMensagem = tk.Label(self.frame, text="", font=("Arial", 18))
        self.lblMensagem.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def buscar_cidade(self):
        idCidade = self.txtIdCidade.get()
        resultado = self.cliente.buscar(idCidade)  # Alterado para cliente
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtUF.delete(0, tk.END)
            self.txtUF.insert(tk.END, resultado[2])
            messagebox.showinfo("Sucesso", "Cidade encontrada com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Cidade não encontrada!")

    def inserir_cidade(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()  # Adicione uma entrada para telefone
        endereco = self.txtEndereco.get()  # Adicione uma entrada para endereço
        cpf = self.txtCPF.get()  # Adicione uma entrada para CPF
        cidade = self.txtCidade.get()  # Adicione uma entrada para a cidade

        if nome and telefone and endereco and cpf and cidade:  # Verifique todos os campos
            self.cliente.inserir(nome, telefone, endereco, cpf, cidade)  # Chame o método com todos os parâmetros
            messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")


    def alterar_cidade(self):
        idCidade = self.txtIdCidade.get()
        nome = self.txtNome.get()
        uf = self.txtUF.get()
        if idCidade and nome and uf:
            self.cliente.alterar(idCidade, nome, uf)  # Altere para cliente
            messagebox.showinfo("Sucesso", "Cidade alterada com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def excluir_cidade(self):
        idCidade = self.txtIdCidade.get()
        if idCidade:
            if self.cliente.existem_clientes_associados(idCidade):  # Verifica clientes
                messagebox.showwarning("Aviso", "Não é possível excluir a cidade. Existem clientes associados a ela.")
            else:
                self.cliente.excluir(idCidade)  # Exclusão da cidade
                messagebox.showinfo("Sucesso", "Cidade excluída com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha o campo ID da Cidade.")

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = CityApp(root)
    root.mainloop()
