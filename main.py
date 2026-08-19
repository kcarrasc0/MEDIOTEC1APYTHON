import customtkinter as ctk

# Configuração básica do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Cria a janela principal
app = ctk.CTk()
app.geometry("400x300")
app.title("Meu Primeiro App - Figma para Python")

# Adiciona um título
titulo = ctk.CTkLabel(app, text="Olá, Codespaces!", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

# Função do botão
def clique_botao():
    titulo.configure(text="Botão clicado! A interface funciona!")

# Adiciona um botão moderno (estilo Figma)
botao = ctk.CTkButton(app, text="Clique Aqui", command=clique_botao, corner_radius=8)
botao.pack(pady=20)

# Mantém a janela aberta
app.mainloop()