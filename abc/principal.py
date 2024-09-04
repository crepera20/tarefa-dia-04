import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

# Função para abrir uma nova janela
def abrir_janela(script):
    try:
        janela.withdraw()  # Esconde a janela atual
        subprocess.Popen(['python', script])  # Abre o arquivo especificado
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir {script}: {str(e)}")

# Função para sair da aplicação
def sair():
    sys.exit()
    self.root.destroy()

# Criação da janela principal
janela = tk.Tk()
janela.title("Rotas")
janela.state("zoomed")  # Aumenta o tamanho da janela

# Título
titulo = tk.Label(janela, text="Rotas", font=("Arial", 36, "bold"))  # Aumenta a fonte do título
titulo.pack(pady=40)  # Aumenta o espaçamento

# Criação dos botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)  # Aumenta o espaçamento entre o título e os botões

# Aumenta a largura e a altura dos botões
btn_usuarios = tk.Button(frame_botoes, text="Usuários", font=("Arial", 24), command=lambda: abrir_janela('app.py'), width=15, height=3)
btn_usuarios.grid(row=0, column=0, padx=20, pady=20)

btn_cidades = tk.Button(frame_botoes, text="Cidades", font=("Arial", 24), command=lambda: abrir_janela('cidades.py'), width=15, height=3)
btn_cidades.grid(row=0, column=1, padx=20, pady=20)

btn_clientes = tk.Button(frame_botoes, text="Clientes", font=("Arial", 24), command=lambda: abrir_janela('clientes.py'), width=15, height=3)
btn_clientes.grid(row=0, column=2, padx=20, pady=20)

btn_sair = tk.Button(frame_botoes, text="Sair", font=("Arial", 24), command=sair, width=15, height=3)
btn_sair.grid(row=0, column=3, padx=20, pady=20)

# Executar a janela
janela.mainloop()
