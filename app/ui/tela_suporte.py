import tkinter as tk
from tkinter import ttk, messagebox

class TelaSuporte(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self._build() # Monta a interface gráfica

    def _build(self):
        self.pack(fill='both', expand=True)
        ttk.Label(self, text='Contate-nos', font=('Arial', 16, 'bold')).pack(pady=6) 

       # - Formulário -    
        form = ttk.Frame(self)
        form.pack(fill='both', expand=True, padx=8, pady=4)

        # Configura expansão proporcional das colunas
        form.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=3)

        ttk.Label(form, text='Email: ', anchor='center').grid(row=0, column=0, sticky='we', padx=4, pady=2)
        self.ent_email = ttk.Entry(form, width=40)
        self.ent_email.grid(row=0, column=1, sticky='we', padx=4, pady=2)

        ttk.Label(form, text='Assunto: ', anchor='center').grid(row=1, column=0, sticky='we', padx=4, pady=2)
        self.ent_assunto = ttk.Entry(form, width=20)
        self.ent_assunto.grid(row=1, column=1, sticky='we', padx=4, pady=2)

        ttk.Label(form, text='Descrição: ', anchor='center').grid(row=2, column=0, sticky='we', padx=4, pady=2)
        self.ent_descricao = ttk.Entry(form, width=20)
        self.ent_descricao.grid(row=2, column=1, sticky='we', padx=4, pady=2)

        # - Botões
        botao = ttk.Frame(self)
        botao.pack(pady=2)
        ttk.Button(botao, text='Enviar', command=self._enviar).grid(row=0, column=0, padx=0)

    def _enviar(self):
        email = self.ent_email.get().strip()
        assunto = self.ent_assunto.get().strip()
        descricao = self.ent_descricao.get().strip()

        if not email or not assunto or not descricao:
            messagebox.showerror('ERRO!', 'Preencha todos os campos corretamente!')
            return
            
        messagebox.showinfo('SUCESSO!', 'Mensagem enviada com sucesso! \nEm breve sua mensagem será respondida. ')
        return

rodar_tela = tk.Tk()
rodar_tela.title("Suporte")
rodar_tela.geometry('430x270')

container = ttk.Frame(rodar_tela)
container.pack(fill='both', expand=True)

TelaSuporte(container)
rodar_tela.mainloop()
