import tkinter as tk
from tkinter import messagebox

def cadastrar():
    messagebox.showinfo("Sucesso", "Cadastro do aluno realizado com sucesso!")

def voltar():
    janela.destroy()

# Janela principal
janela = tk.Tk()
janela.title("Cadastro de Aluno - CONRAD")
janela.geometry("600x700")
janela.configure(bg="#f4f4f4")
janela.resizable(False, False)

# Botão voltar
btn_voltar = tk.Button(janela, text="voltar", bg="#d3651d", fg="white", relief="flat", command=voltar)
btn_voltar.place(x=20, y=20)

# Frame central
frame = tk.Frame(janela, bg="#d3651d")
frame.pack(pady=60)

lbl_titulo = tk.Label(frame, text="Cadastro do aluno", bg="#d3651d", fg="white", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

# Campos de entrada
campos = [
    "Email",
    "Senha",
    "Confirmar Senha",
    "CPF",
    "RG",
    "Telefone",
    "Matrícula do Aluno"
]

entradas = {}

for label_text in campos:
    lbl = tk.Label(frame, text=label_text, bg="#d3651d", fg="white", font=("Arial", 10, "bold"))
    lbl.pack(anchor="w", padx=20)
    entry = tk.Entry(frame, width=35, font=("Arial", 11), show="*" if "Senha" in label_text else "")
    entry.pack(padx=20, pady=5, ipady=3)
    entradas[label_text] = entry

# Botão cadastrar
btn_cadastrar = tk.Button(frame, text="Cadastrar", bg="black", fg="white", font=("Arial", 10, "bold"), relief="flat", command=cadastrar)
btn_cadastrar.pack(pady=15)

# Logo e texto
lbl_logo = tk.Label(janela, text="🎓", font=("Arial", 35), bg="#f4f4f4")
lbl_logo.pack(pady=10)

lbl_conrad = tk.Label(janela, text="CONRAD VIRTUAL SCHOOL", font=("Arial Black", 14, "bold"), bg="#f4f4f4", fg="#0c2d57")
lbl_conrad.pack()

lbl_rodape = tk.Label(janela, text="Todos os Direitos Reservados\nsite desenvolvido por alunos do Senac", bg="#f4f4f4", fg="black", font=("Arial", 8))
lbl_rodape.pack(side="bottom", pady=10)

janela.mainloop()