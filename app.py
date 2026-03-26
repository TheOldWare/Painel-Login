import customtkinter as ctk

# Configuração de aparencia do tema
ctk.set_appearance_mode("dark")

# Criação das funções de funcionalidades


def validar_login():
    user = usuario_text.get()
    senha = senha_texto.get()
    if user == "ware" and senha == "12345":
        resultado.configure(text="Login sucedido!", text_color="green")
    else:
        resultado.configure(text="Login errado!", text_color="red")

# Criação da janela principal
app = ctk.CTk()
app.title("Minha Aplicação")
app.geometry("400x400")

# Criação dos campos

# label
usuario_painel = ctk.CTkLabel(app, text="Usuário")
usuario_painel.pack(pady=10)

# entry
usuario_text = ctk.CTkEntry(app, placeholder_text="Email")
usuario_text.pack(pady=10)

# Senha:
senha_painel = ctk.CTkLabel(app, text="Senha")
senha_painel.pack(pady=10)

senha_texto = ctk.CTkEntry(app, placeholder_text="Sua senha", show="*")
senha_texto.pack(pady=10)

# button
botao_login = ctk.CTkButton(app, text="Login", command=validar_login)
botao_login.pack(pady=10)

# campo de feedback de login
resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

# Iniciar aplicação
app.mainloop()
