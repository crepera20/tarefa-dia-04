import tkinter as tk
from tkinter import messagebox
import os
from clientes_model import Cliente

class ClientApp:
    def __init__(self, root):
        self.cliente = Cliente()  # Instancia a classe Cliente

        self.root = root
        self.root.title("Cadastro de Clientes")
        self.root.state("zoomed")

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        # Widgets
        self.lblIdCliente = tk.Label(self.frame, text="ID Cliente:", font=("Arial", 18))
        self.lblIdCliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtIdCliente = tk.Entry(self.frame, font=("Arial", 18))
        self.txtIdCliente.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = tk.Button(self.frame, text="Buscar", command=self.buscar_cliente, font=("Arial", 18))
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        self.lblTelefone = tk.Label(self.frame, text="Telefone:", font=("Arial", 18))
        self.lblTelefone.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.txtTelefone = tk.Entry(self.frame, font=("Arial", 18))
        self.txtTelefone.grid(row=2, column=1, padx=10, pady=10)

        self.lblEndereco = tk.Label(self.frame, text="Endereço:", font=("Arial", 18))
        self.lblEndereco.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.txtEndereco = tk.Entry(self.frame, font=("Arial", 18))
        self.txtEndereco.grid(row=3, column=1, padx=10, pady=10)

        self.lblCPF = tk.Label(self.frame, text="CPF:", font=("Arial", 18))
        self.lblCPF.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txtCPF = tk.Entry(self.frame, font=("Arial", 18))
        self.txtCPF.grid(row=4, column=1, padx=10, pady=10)

        self.lblCidade = tk.Label(self.frame, text="Cidade:", font=("Arial", 18))  # Novo label para cidade
        self.lblCidade.grid(row=5, column=0, padx=10, pady=10, sticky="e")  # Adiciona nova linha
        self.txtCidade = tk.Entry(self.frame, font=("Arial", 18))  # Novo campo de entrada para cidade
        self.txtCidade.grid(row=5, column=1, padx=10, pady=10)  # Adiciona nova linha

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_cliente, font=("Arial", 18))
        self.btnInserir.grid(row=6, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_cliente, font=("Arial", 18))
        self.btnAlterar.grid(row=6, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_cliente, font=("Arial", 18))
        self.btnExcluir.grid(row=6, column=2, padx=10, pady=10)

        self.lblMensagem = tk.Label(self.frame, text="", font=("Arial", 18))
        self.lblMensagem.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def buscar_cliente(self):
        id_cliente = self.txtIdCliente.get()
        resultado = self.cliente.buscar(id_cliente)
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtTelefone.delete(0, tk.END)
            self.txtTelefone.insert(tk.END, resultado[2])
            self.txtEndereco.delete(0, tk.END)
            self.txtEndereco.insert(tk.END, resultado[3])
            self.txtCPF.delete(0, tk.END)
            self.txtCPF.insert(tk.END, resultado[4])

            # Verifique se resultado[5] existe
            if len(resultado) > 5:
                self.txtCidade.delete(0, tk.END)
                self.txtCidade.insert(tk.END, resultado[5])  # Preenche com a cidade
            else:
                self.txtCidade.delete(0, tk.END)  # Limpa o campo caso a cidade não exista

            messagebox.showinfo("Sucesso", "Cliente encontrado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Cliente não encontrado!")


    def inserir_cliente(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        endereco = self.txtEndereco.get()
        cpf = self.txtCPF.get()
        cidade = self.txtCidade.get()  # Obtém a cidade do campo de entrada
        if nome and telefone and endereco and cpf and cidade:  # Verifica se todos os campos estão preenchidos
            print(f"Inserindo cliente: Nome={nome}, Telefone={telefone}, Endereço={endereco}, CPF={cpf}, Cidade={cidade}")  # Debug
            self.cliente.inserir(nome, telefone, endereco, cpf, cidade)  # Passa a cidade para a inserção
            messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def alterar_cliente(self):
        id_cliente = self.txtIdCliente.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        endereco = self.txtEndereco.get()
        cpf = self.txtCPF.get()
        cidade = self.txtCidade.get()  # Obtém a cidade do campo de entrada
        if id_cliente and nome and telefone and endereco and cpf and cidade:  # Verifica se todos os campos estão preenchidos
            self.cliente.alterar(id_cliente, nome, telefone, endereco, cpf, cidade)  # Passa a cidade para a alteração
            messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    def excluir_cliente(self):
        id_cliente = self.txtIdCliente.get()
        if id_cliente:
            self.cliente.excluir(id_cliente)
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha o campo ID Cliente.")

    def limpar_campos(self):
        self.txtIdCliente.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtTelefone.delete(0, tk.END)
        self.txtEndereco.delete(0, tk.END)
        self.txtCPF.delete(0, tk.END)
        self.txtCidade.delete(0, tk.END)  # Limpa o campo de cidade

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = ClientApp(root)
    root.mainloop()
