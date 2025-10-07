
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime


class ChatConradApp:
    """Classe principal do aplicativo CHAT CONRAD"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("CHAT CONRAD - Sistema de Gerenciamento")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f5f5f5")
        
        # Variáveis para armazenar dados
        self.mensagens = []
        self.menu_ativo = "Minhas salas"
        
        # Criar interface
        self.criar_header()
        self.criar_container_principal()
        self.criar_footer()
        
    def criar_header(self):
        """Cria o cabeçalho com menu de navegação"""
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=40)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        
        # Itens do menu
        menus = ["Home", "Suporte", "Gerenciador da sala", "Sobre Nós"]
        
        for i, menu in enumerate(menus):
            bg_color = "#e67e22" if menu == "Suporte" else "#2c3e50"
            btn = tk.Button(
                header_frame,
                text=menu,
                bg=bg_color,
                fg="white",
                font=("Arial", 10, "bold"),
                relief=tk.FLAT,
                padx=30,
                pady=10,
                cursor="hand2",
                command=lambda m=menu: self.mudar_menu_header(m)
            )
            btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            
    def criar_container_principal(self):
        """Cria o container principal com sidebar e conteúdo"""
        container = tk.Frame(self.root, bg="#f5f5f5")
        container.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        
        # Criar sidebar
        self.criar_sidebar(container)
        
        # Criar área de conteúdo
        self.criar_area_conteudo(container)
        
    def criar_sidebar(self, parent):
        """Cria a barra lateral com menu de navegação"""
        sidebar = tk.Frame(parent, bg="#e67e22", width=240)
        sidebar.pack(fill=tk.Y, side=tk.LEFT)
        sidebar.pack_propagate(False)
        
        # Itens do menu lateral
        menu_items = [
            ("👤", "Professor"),
            ("😊", "Perfil"),
            ("📅", "Agenda"),
            ("📹", "Vídeos salvos"),
            ("⭐", "Atividades"),
            ("📺", "Conteúdo salvo"),
            ("🎓", "Minhas salas"),
            ("⚙️", "configurações")
        ]
        
        for icon, text in menu_items:
            bg_color = "#f39c12" if text == "Minhas salas" else "white"
            fg_color = "white" if text == "Minhas salas" else "black"
            
            frame = tk.Frame(sidebar, bg=bg_color, relief=tk.RAISED, bd=1)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            btn = tk.Button(
                frame,
                text=f"{icon}  {text}",
                bg=bg_color,
                fg=fg_color,
                font=("Arial", 10),
                relief=tk.FLAT,
                anchor="w",
                padx=15,
                pady=10,
                cursor="hand2",
                command=lambda t=text: self.mudar_menu_lateral(t)
            )
            btn.pack(fill=tk.BOTH, expand=True)
        
        # Botão Sair
        btn_sair = tk.Button(
            sidebar,
            text="Sair",
            bg="#e67e22",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
            command=self.sair
        )
        btn_sair.pack(side=tk.BOTTOM, pady=20, padx=20, fill=tk.X)
        
    def criar_area_conteudo(self, parent):
        """Cria a área principal de conteúdo"""
        conteudo_frame = tk.Frame(parent, bg="#f5f5f5")
        conteudo_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=10, pady=10)
        
        # Container horizontal
        container_horizontal = tk.Frame(conteudo_frame, bg="#f5f5f5")
        container_horizontal.pack(fill=tk.BOTH, expand=True)
        
        # Coluna esquerda (Turmas e Conteúdo)
        self.criar_coluna_esquerda(container_horizontal)
        
        # Coluna central (Chat)
        self.criar_coluna_central(container_horizontal)
        
    def criar_coluna_esquerda(self, parent):
        """Cria a coluna esquerda com dropdowns"""
        coluna_esquerda = tk.Frame(parent, bg="#f5f5f5", width=400)
        coluna_esquerda.pack(fill=tk.Y, side=tk.LEFT, padx=(0, 10))
        coluna_esquerda.pack_propagate(False)
        
        # Seção Turmas
        frame_turmas = tk.LabelFrame(
            coluna_esquerda,
            text="Turmas",
            bg="white",
            font=("Arial", 10, "bold"),
            relief=tk.SOLID,
            bd=2
        )
        frame_turmas.pack(fill=tk.X, pady=(0, 20))
        
        self.combo_turmas = ttk.Combobox(
            frame_turmas,
            values=["turma 10", "turma 11", "turma 12"],
            state="readonly",
            font=("Arial", 10)
        )
        self.combo_turmas.set("turma 10")
        self.combo_turmas.pack(padx=10, pady=10, fill=tk.X)
        
        # Seção Conteúdo
        frame_conteudo = tk.LabelFrame(
            coluna_esquerda,
            text="Conteúdo",
            bg="white",
            font=("Arial", 10, "bold"),
            relief=tk.SOLID,
            bd=2,
            height=200
        )
        frame_conteudo.pack(fill=tk.BOTH, expand=True)
        frame_conteudo.pack_propagate(False)
        
        self.combo_conteudo = ttk.Combobox(
            frame_conteudo,
            values=["Conteúdo 10", "Conteúdo 11", "Conteúdo 12"],
            state="readonly",
            font=("Arial", 10)
        )
        self.combo_conteudo.set("Conteúdo 10")
        self.combo_conteudo.pack(padx=10, pady=10, fill=tk.X)
        
    def criar_coluna_central(self, parent):
        """Cria a coluna central com chat e formulários"""
        coluna_central = tk.Frame(parent, bg="white", relief=tk.SOLID, bd=2)
        coluna_central.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        # Container para as duas colunas do formulário
        form_container = tk.Frame(coluna_central, bg="white")
        form_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Coluna esquerda do formulário
        self.criar_coluna_form_esquerda(form_container)
        
        # Coluna direita do formulário
        self.criar_coluna_form_direita(form_container)
        
        # Área de mensagem
        self.criar_area_mensagem(coluna_central)
        
    def criar_coluna_form_esquerda(self, parent):
        """Cria a coluna esquerda do formulário"""
        coluna_esq = tk.Frame(parent, bg="white")
        coluna_esq.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(0, 10))
        
        # Botão Professores Chat
        btn_prof_chat = tk.Button(
            coluna_esq,
            text="PROFESSORES CHAT",
            bg="#e67e22",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
            command=lambda: messagebox.showinfo("Chat", "Abrindo PROFESSORES CHAT")
        )
        btn_prof_chat.pack(fill=tk.X, pady=(0, 5))
        
        # Botão Com os Alunos Chat
        btn_alunos_chat = tk.Button(
            coluna_esq,
            text="COM OS ALUNOS CHAT",
            bg="#e67e22",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
            command=lambda: messagebox.showinfo("Chat", "Abrindo COM OS ALUNOS CHAT")
        )
        btn_alunos_chat.pack(fill=tk.X, pady=(0, 10))
        
        # Campo Nome
        tk.Label(coluna_esq, text="Nome", bg="white", font=("Arial", 9, "bold")).pack(anchor="w")
        self.entry_nome = tk.Entry(coluna_esq, font=("Arial", 10))
        self.entry_nome.pack(fill=tk.X, pady=(0, 10))
        
        # Campo E-mail
        tk.Label(coluna_esq, text="E-mail", bg="white", font=("Arial", 9, "bold")).pack(anchor="w")
        self.entry_email = tk.Entry(coluna_esq, font=("Arial", 10))
        self.entry_email.pack(fill=tk.X, pady=(0, 10))
        
        # Seção vídeo aulas
        frame_video = tk.LabelFrame(
            coluna_esq,
            text="vídeo aulas",
            bg="white",
            font=("Arial", 9, "bold"),
            relief=tk.SOLID,
            bd=2
        )
        frame_video.pack(fill=tk.BOTH, expand=True)
        
        self.combo_aulas = ttk.Combobox(
            frame_video,
            values=["Aula 10", "Aula 11", "Aula 12"],
            state="readonly",
            font=("Arial", 10)
        )
        self.combo_aulas.set("Aula 10")
        self.combo_aulas.pack(padx=10, pady=10, fill=tk.X)
        
    def criar_coluna_form_direita(self, parent):
        """Cria a coluna direita do formulário"""
        coluna_dir = tk.Frame(parent, bg="white")
        coluna_dir.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        # Header com logo
        header_chat = tk.Frame(coluna_dir, bg="white")
        header_chat.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            header_chat,
            text="CHAT CONRAD",
            bg="white",
            font=("Arial", 18, "bold")
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        # Logo placeholder
        logo_frame = tk.Frame(header_chat, bg="white", relief=tk.SOLID, bd=2, width=80, height=80)
        logo_frame.pack(side=tk.LEFT)
        logo_frame.pack_propagate(False)
        
        tk.Label(logo_frame, text="✿", bg="white", font=("Arial", 24)).pack()
        tk.Label(logo_frame, text="CONRAD", bg="white", font=("Arial", 8, "bold")).pack()
        tk.Label(logo_frame, text="VIRTUAL SCHOOL", bg="white", font=("Arial", 6)).pack()
        
        # Campo Diploma
        tk.Label(coluna_dir, text="Diploma", bg="white", font=("Arial", 9, "bold")).pack(anchor="w")
        self.entry_diploma = tk.Entry(coluna_dir, font=("Arial", 10))
        self.entry_diploma.pack(fill=tk.X, pady=(0, 10))
        
        # Campo Número
        tk.Label(coluna_dir, text="Número", bg="white", font=("Arial", 9, "bold")).pack(anchor="w")
        self.entry_numero = tk.Entry(coluna_dir, font=("Arial", 10))
        self.entry_numero.pack(fill=tk.X, pady=(0, 10))
        
        # Seção Atividades
        frame_atividades = tk.LabelFrame(
            coluna_dir,
            text="Atividades",
            bg="white",
            font=("Arial", 9, "bold"),
            relief=tk.SOLID,
            bd=2
        )
        frame_atividades.pack(fill=tk.BOTH, expand=True)
        
        self.combo_atividades = ttk.Combobox(
            frame_atividades,
            values=["Atividade 10", "Atividade 11", "Atividade 12"],
            state="readonly",
            font=("Arial", 10)
        )
        self.combo_atividades.set("Atividade 10")
        self.combo_atividades.pack(padx=10, pady=10, fill=tk.X)
        
    def criar_area_mensagem(self, parent):
        """Cria a área de mensagem na parte inferior"""
        area_msg = tk.Frame(parent, bg="white")
        area_msg.pack(fill=tk.BOTH, padx=10, pady=(0, 10))
        
        tk.Label(
            area_msg,
            text="Pergunte alguma coisa",
            bg="white",
            fg="#7f8c8d",
            font=("Arial", 9)
        ).pack(anchor="w", pady=(0, 5))
        
        # Caixa de texto para mensagem
        self.text_mensagem = scrolledtext.ScrolledText(
            area_msg,
            height=4,
            font=("Arial", 10),
            wrap=tk.WORD
        )
        self.text_mensagem.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        # Botão enviar
        btn_enviar = tk.Button(
            area_msg,
            text="enviar",
            bg="white",
            font=("Arial", 10, "bold"),
            relief=tk.SOLID,
            bd=1,
            cursor="hand2",
            command=self.enviar_mensagem
        )
        btn_enviar.pack(anchor="e")
        
    def criar_footer(self):
        """Cria o rodapé"""
        footer = tk.Frame(self.root, bg="#ecf0f1", height=40)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        
        tk.Label(
            footer,
            text="Todos os Direitos Reservados.\nsite desenvolvido por alunos do Senac",
            bg="#ecf0f1",
            fg="#7f8c8d",
            font=("Arial", 8),
            justify=tk.CENTER
        ).pack(pady=5)
        
    def mudar_menu_header(self, menu):
        """Muda o menu ativo no header"""
        messagebox.showinfo("Navegação", f"Você clicou em: {menu}")
        
    def mudar_menu_lateral(self, menu):
        """Muda o menu ativo na sidebar"""
        self.menu_ativo = menu
        messagebox.showinfo("Menu", f"Você acessou: {menu}")
        
    def enviar_mensagem(self):
        """Envia a mensagem digitada"""
        mensagem = self.text_mensagem.get("1.0", tk.END).strip()
        
        if mensagem:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.mensagens.append({
                "texto": mensagem,
                "timestamp": timestamp
            })
            
            messagebox.showinfo(
                "Mensagem Enviada",
                f"Mensagem enviada com sucesso!\n\n{mensagem}"
            )
            
            self.text_mensagem.delete("1.0", tk.END)
        else:
            messagebox.showwarning(
                "Atenção",
                "Por favor, digite uma mensagem antes de enviar."
            )
            
    def sair(self):
        """Sai do aplicativo"""
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair?"):
            self.root.quit()


def main():
    """Função principal"""
    root = tk.Tk()
    app = ChatConradApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
