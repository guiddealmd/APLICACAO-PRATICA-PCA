import tkinter as tk
from tkinter import messagebox
from main import jogo

class JogoMatematicaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Matemática")

        self.label = tk.Label(master, text="Bem-vindo ao Jogo de Matemática!")
        self.label.pack()

        self.iniciar_button = tk.Button(master, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.iniciar_button.pack()

    def iniciar_jogo(self):
        pontuacao = jogo()
        messagebox.showinfo(title="Fim do Jogo", message=f"Sua pontuação final é: {pontuacao}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoMatematicaGUI(root)
    root.mainloop()