from doctest import master
from msilib.schema import SelfReg
import tkinter as tk
from tkinter import messagebox
from typing import Self
from main import jogo 

class JogoMatematicaGUI:
    def __init__(self, master):
    Self.master = master
    Self.master.title("Jogo de Matemática")

    Self.label = tk.Label(master, text="Bem-vindo ao Jogo de Matemática!")
    Self.label.pack()

    Self.iniciar_button = tk.Button(master, text="Iniciar Jogo", command=SelfReg.iniciar_jogo)
    Self.iniciar_button.pack()

    def iniciar_jogo(self):
        pontuacao = jogo()
        messagebox.showinfo(title="Fim do Jogo", message=f"Sua pontuação final é: {pontuacao}")

        if __name__ == "__main__":
            root = tk.Tk()
            app = JogoMatematicaGUI(root)
            root.mainloop()

