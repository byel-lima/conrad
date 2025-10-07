import tkinter as tk
from tkinter import ttk, messagebox

class TelaAvaliacao(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self._build()

    def _build(self):
        self.pack(fill='both', expand=True)
        frame = tk.Frame(self, bg="#d3651d")
        frame.pack(pady=60, fill="both", expand=True)

        
        lbl_titulo = tk.Label(
            frame,
            text="Avaliação",
            bg="#d3651d",
            fg="white",
            font=("Arial", 16, "bold")
        
        )
        lbl_titulo.pack(pady=10)

        
        form = tk.Frame(frame, bg="#d3651d")
        form.pack(padx=10, pady=5)


        tk.Label(form, text="ALUNO :", bg="#d3651d", fg="white").grid(row=1, column=0, sticky="e", pady=3)
        self.ent_data = tk.Entry(form, width=30)
        self.ent_data.grid(row=1, column=1, pady=3)

        tk.Label(form, text="Notas :", bg="#d3651d", fg="white").grid(row=2, column=0, sticky="e", pady=3)
        self.ent_hora = tk.Entry(form, width=30)
        self.ent_hora.grid(row=2, column=1, pady=3)

        tk.Label(form, text="RECLAMAÇÕES :", bg="#d3651d", fg="white").grid(row=3, column=0, sticky="ne", pady=3)
        self.txt_comentario = tk.Text(form, width=30, height=2)
        self.txt_comentario.grid(row=3, column=1, pady=3)

        #combox
        tk.Label(form, text="Nota :", bg="#d3651d", fg="white").grid(row=4, column=0, sticky="e", pady=3)
        self.cb_nota = ttk.Combobox(form, width=28, state='readonly', values=["1", "2", "3", "4", "5","6", "7", "8", "9", "10"])
        self.cb_nota.grid(row=4, column=1, pady=3)
        self.cb_nota.set("*?*")

        # BOTÃO DE ENVIO
        btn_enviar = tk.Button(
            frame,
            text="Enviar Avaliação",
            bg="#ffffff",
            fg="#d3651d",
            font=("Arial", 12, "bold"),
            width=18,
            command=self._enviar
        )
        btn_enviar.pack(pady=15)

    def _enviar(self):
        #nome = self.ent_nome.get().strip()
        data = self.ent_data.get().strip()
        hora = self.ent_hora.get().strip()
        comentario = self.txt_comentario.get("1.0", tk.END).strip()
        nota = self.cb_nota.get()

        if  not data or not hora or not comentario:
            messagebox.showwarning("Aviso", "Preencha todos os campos corretamente!")
            return

        messagebox.showinfo("Sucesso", f"Avaliação enviada com sucesso!\n\nNota: {nota}")
        self._limpar()

    def _limpar(self):
        for ent in (self.ent_data,self.ent_hora,self.txt_comentario("1.0"),self.cb_nota("5")):
            ent.delete(0,tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tela de Avaliação - CONRAD")
    root.geometry("600x700")
    TelaAvaliacao(root)
    root.mainloop()
