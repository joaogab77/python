import tkinter
from tkinter import *

class Principal:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", 10)


        self.janela = Frame(master)
        self.janela.pack()


        self.titulo = Label(self.janela, text="Menu Principal", font=("Arial", 25, "bold"))
        self.titulo.pack(pady=20)


        self.janela_botoes = Frame(master)
        self.janela_botoes["padx"] = 20
        self.janela_botoes.pack()


        self.btn_usuarios = Button(self.janela_botoes, text="Usuários", font=self.fontePadrao, width=20, command=self.usuarios)
        self.btn_usuarios.pack(pady=5)


        self.btn_cidades = Button(self.janela_botoes, text="Cidades", font=self.fontePadrao, width=20, command=self.cidades)
        self.btn_cidades.pack(pady=5)


        self.btn_clientes = Button(self.janela_botoes, text="Clientes", font=self.fontePadrao, width=20, command=self.clientes)
        self.btn_clientes.pack(pady=5)


        self.btn_fechar = Button(self.janela_botoes, text="Fechar", font=self.fontePadrao, width=20, command=self.fechar)
        self.btn_fechar.pack(pady=5)

    def usuarios(self):
        print("Usuários foi clicado")

    def cidades(self):
        print("Cidades foi clicado")

    def clientes(self):
        print("Clientes foi clicado")

    def fechar(self):
        root.destroy()


root = Tk()
Principal(root)
root.title("Principal")
root.mainloop()
