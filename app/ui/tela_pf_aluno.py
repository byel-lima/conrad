"""
CHAT CONRAD - Sistema de Gerenciamento de Atividades (Aluno)
Aplicativo desenvolvido com Tkinter
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ChatConradAlunoApp:
    """Classe principal do aplicativo CHAT CONRAD para alunos"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("CHAT CONRAD - Gerenciador de Atividades")
        self.root.geometry("1100x650")
        self.root.configure(bg="#f5f5f5")
        
        # Variáveis para armazenar dados
        self.menu_ativo = "Atividades"
        
        # Criar interface
        self.criar_header()
        self.criar_container_principal()
        self.criar_footer()
        
    def criar_header(self):
        """Cria o cabeçalho com menu de navegação"""
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=40)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        
        # Itens do menu
        menus = ["Home", "Suporte", "Gerenciador de Atividades", "Sobre Nós"]
        
        for i, menu in enumerate(menus):
            bg_color = "#e67e22" if menu in ["Suporte", "Gerenciador de Atividades"] else "#2c3e50"
            btn = tk.Button(
                header_frame,
                text=menu,
                bg=bg_color,
                fg="white",
                font=("Arial", 10, "bold"),
                relief=tk.FLAT,
                padx=25,
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
        sidebar = tk.Frame(parent, bg="#e67e22", width=260)
        sidebar.pack(fill=tk.Y, side=tk.LEFT)
        sidebar.pack_propagate(False)
        
        # Itens do menu lateral
        menu_items = [
            ("👤", "Aluno"),
            ("😊", "Perfil"),
            ("📅", "Agenda"),
            ("📹", "Vídeos salvos"),
            ("📁", "Cteúdo"),
            ("🎓", "Minhas inscrições"),
            ("⚙️", "Configurações"),
            ("⭐", "Atividades")
        ]
        
        for icon, text in menu_items:
            bg_color = "#f39c12" if text == "Atividades" else "white"
            fg_color = "white" if text == "Atividades" else "black"
            
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
        btn_sair.pack(side=tk.BOTTOM, pady=20, padx=30, fill=tk.X)
        
    def criar_area_conteudo(self, parent):
        """Cria a área principal de conteúdo"""
        conteudo_frame = tk.Frame(parent, bg="#f5f5f5")
        conteudo_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=20, pady=20)
        
        # Container horizontal
        container_horizontal = tk.Frame(conteudo_frame, bg="#f5f5f5")
        container_horizontal.pack(fill=tk.BOTH, expand=True)
        
        # Coluna esquerda (Atividades)
        self.criar_coluna_esquerda(container_horizontal)
        
        # Coluna direita (Botões e Logo)
        self.criar_coluna_direita(container_horizontal)
        
    def criar_coluna_esquerda(self, parent):
        """Cria a coluna esquerda com atividades"""
        coluna_esquerda = tk.Frame(parent, bg="#f5f5f5")
        coluna_esquerda.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=(0, 20))
        
        # Seção Atividades salvas
        frame_atividades_salvas = tk.LabelFrame(
            coluna_esquerda,
            text="Atividades salvas",
            bg="white",
            font=("Arial", 11, "bold"),
            relief=tk.SOLID,
            bd=2
        )
        frame_atividades_salvas.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Frame interno para padding
        inner_frame1 = tk.Frame(frame_atividades_salvas, bg="white")
        inner_frame1.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        self.combo_atividades_salvas = ttk.Combobox(
            inner_frame1,
            values=["Aula 10", "Aula 11", "Aula 12"],
            state="readonly",
            font=("Arial", 11),
            width=25
        )
        self.combo_atividades_salvas.set("Aula 10")
        self.combo_atividades_salvas.pack(anchor="w")
        
        # Seção Novas atividades
        frame_novas_atividades = tk.LabelFrame(
            coluna_esquerda,
            text="Novas atividades",
            bg="white",
            font=("Arial", 11, "bold"),
            relief=tk.SOLID,
            bd=2
        )
        frame_novas_atividades.pack(fill=tk.BOTH, expand=True)
        
        # Frame interno para padding
        inner_frame2 = tk.Frame(frame_novas_atividades, bg="white")
        inner_frame2.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        self.combo_novas_atividades = ttk.Combobox(
            inner_frame2,
            values=["Aula 10", "Aula 11", "Aula 12"],
            state="readonly",
            font=("Arial", 11),
            width=25
        )
        self.combo_novas_atividades.set("Aula 10")
        self.combo_novas_atividades.pack(anchor="w")
        
    def criar_coluna_direita(self, parent):
        """Cria a coluna direita com botões e logo"""
        coluna_direita = tk.Frame(parent, bg="#f5f5f5")
        coluna_direita.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        # Container para os botões
        botoes_container = tk.Frame(coluna_direita, bg="#f5f5f5")
        botoes_container.pack(fill=tk.X, pady=(0, 30))
        
        # Botão ALUNOS CHAT
        btn_alunos_chat = tk.Button(
            botoes_container,
            text="ALUNOS CHAT",
            bg="#e67e22",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
            height=2,
            command=lambda: messagebox.showinfo("Chat", "Abrindo ALUNOS CHAT")
        )
        btn_alunos_chat.pack(fill=tk.X, pady=(0, 10))
        
        # Botão COM OS PROFESSORES CHAT
        btn_professores_chat = tk.Button(
            botoes_container,
            text="COM OS PROFESSORES CHAT",
            bg="#e67e22",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
            height=2,
            command=lambda: messagebox.showinfo("Chat", "Abrindo COM OS PROFESSORES CHAT")
        )
        btn_professores_chat.pack(fill=tk.X, pady=(0, 10))
        
        # Botão BANCO DE QUESTÕES E EXERCÍCIOS
        btn_banco_questoes = tk.Button(
            botoes_container,
            text="BANCO DE QUESTÕES E EXERCÍCIOS",
            bg="#e67e22",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
            height=2,
            command=lambda: messagebox.showinfo("Banco", "Abrindo BANCO DE QUESTÕES E EXERCÍCIOS")
        )
        btn_banco_questoes.pack(fill=tk.X)
        
        # Seção CHAT CONRAD com logo
        self.criar_secao_logo(coluna_direita)
        
    def criar_secao_logo(self, parent):
        """Cria a seção com o logo do CHAT CONRAD"""
        logo_container = tk.Frame(parent, bg="white", relief=tk.SOLID, bd=2)
        logo_container.pack(fill=tk.BOTH, expand=True, pady=(30, 0))
        
        # Título
        titulo_frame = tk.Frame(logo_container, bg="white")
        titulo_frame.pack(pady=(20, 10))
        
        tk.Label(
            titulo_frame,
            text="CHAT CONRAD",
            bg="white",
            font=("Arial", 20, "bold")
        ).pack()
        
        # Logo
        logo_frame = tk.Frame(logo_container, bg="white")
        logo_frame.pack(expand=True)
        
        # Canvas para desenhar o logo
        canvas = tk.Canvas(logo_frame, width=180, height=180, bg="white", highlightthickness=0)
        canvas.pack()
        
        # Desenhar escudo (hexágono simplificado como retângulo arredondado)
        canvas.create_rectangle(20, 20, 160, 160, outline="#2c3e50", width=3)
        
        # Desenhar flor (símbolo laranja no centro)
        center_x, center_y = 90, 70
        petal_length = 25
        
        # Desenhar pétalas (4 pétalas em forma de cruz)
        # Pétala superior
        canvas.create_oval(center_x-10, center_y-petal_length-10, center_x+10, center_y-10, 
                          fill="#e67e22", outline="#e67e22")
        # Pétala inferior
        canvas.create_oval(center_x-10, center_y+10, center_x+10, center_y+petal_length+10, 
                          fill="#e67e22", outline="#e67e22")
        # Pétala esquerda
        canvas.create_oval(center_x-petal_length-10, center_y-10, center_x-10, center_y+10, 
                          fill="#e67e22", outline="#e67e22")
        # Pétala direita
        canvas.create_oval(center_x+10, center_y-10, center_x+petal_length+10, center_y+10, 
                          fill="#e67e22", outline="#e67e22")
        
        # Centro da flor
        canvas.create_oval(center_x-8, center_y-8, center_x+8, center_y+8, 
                          fill="#2c3e50", outline="#2c3e50")
        
        # Texto CONRAD
        texto_frame = tk.Frame(logo_container, bg="white")
        texto_frame.pack(pady=(0, 20))
        
        tk.Label(
            texto_frame,
            text="CONRAD",
            bg="white",
            font=("Arial", 16, "bold"),
            fg="#2c3e50"
        ).pack()
        
        tk.Label(
            texto_frame,
            text="VIRTUAL SCHOOL",
            bg="white",
            font=("Arial", 9),
            fg="#2c3e50"
        ).pack()
        
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
        
    def sair(self):
        """Sai do aplicativo"""
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair?"):
            self.root.quit()


def main():
    """Função principal"""
    root = tk.Tk()
    app = ChatConradAlunoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()