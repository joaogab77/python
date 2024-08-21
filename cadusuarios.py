import tkinter as tk
from tkinter import messagebox


def inserir_dados():
    messagebox.showinfo("Inserir", "Dados inseridos com sucesso!")


def alterar_dados():
    messagebox.showinfo("Alterar", "Dados alterados com sucesso!")


def excluir_dados():
    messagebox.showinfo("Excluir", "Dados excluídos com sucesso!")


def buscar_usuario():
    id_usuario = entry_idusuario.get()

    encontrado = False

    if encontrado:

        pass
    else:
        messagebox.showwarning("Buscar", f"Usuário com ID {id_usuario} não encontrado.")

        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_usuario.delete(0, tk.END)
        entry_senha.delete(0, tk.END)


root = tk.Tk()
root.title("Formulário de Usuário")
root.geometry("350x400")

lbl_title = tk.Label(root, text="Informe os dados", font=("Helvetica", 14))
lbl_title.pack(pady=10)

frame_idusuario = tk.Frame(root)
frame_idusuario.pack(pady=5)

lbl_idusuario = tk.Label(frame_idusuario, text="Idusuario:")
lbl_idusuario.pack(side=tk.LEFT)

entry_idusuario = tk.Entry(frame_idusuario)
entry_idusuario.pack(side=tk.LEFT, padx=5)

btn_buscar = tk.Button(frame_idusuario, text="Buscar", command=buscar_usuario)
btn_buscar.pack(side=tk.LEFT)

# Campo para Nome
lbl_nome = tk.Label(root, text="Nome:")
lbl_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

# Campo para Telefone
lbl_telefone = tk.Label(root, text="Telefone:")
lbl_telefone.pack()
entry_telefone = tk.Entry(root)
entry_telefone.pack()

# Campo para E-mail
lbl_email = tk.Label(root, text="E-mail:")
lbl_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Campo para Usuário
lbl_usuario = tk.Label(root, text="Usuário:")
lbl_usuario.pack()
entry_usuario = tk.Entry(root)
entry_usuario.pack()

# Campo para Senha
lbl_senha = tk.Label(root, text="Senha:")
lbl_senha.pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

# Botões
btn_inserir = tk.Button(root, text="Inserir", command=inserir_dados)
btn_inserir.pack(pady=5)

btn_alterar = tk.Button(root, text="Alterar", command=alterar_dados)
btn_alterar.pack(pady=5)

btn_excluir = tk.Button(root, text="Excluir", command=excluir_dados)
btn_excluir.pack(pady=5)

# Executar a aplicação
root.mainloop()
