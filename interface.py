# importar bibliotecas
import tkinter as tk
import quiz

# criar a janela principal
root = tk.Tk()
root.title("App de Quiz")
root.geometry("400x400")

# criar label para exibir a pergunta
question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack()

# criar label para exibir as opçoes
options_label = tk.Label(root, text="", font=("Arial", 12))
options_label.pack()

# criar label para exibir a pontuação
score_label = tk.Label(root, text="", font=("Arial", 12))
score_label.pack()

root.mainloop()