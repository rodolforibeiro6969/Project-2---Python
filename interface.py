import sqlite3
from tkinter import *
from tkinter import messagebox
import random

from login import login_window

# Variáveis globais
user = None
score = 0

# Função para carregar as perguntas
def carregar_perguntas():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Buscar 10 perguntas aleatórias
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 10")
    perguntas = cursor.fetchall()
    conn.close()
    return perguntas

# Função para verificar a resposta do usuário
def verificar_resposta(selected, pergunta_atual, restantes):
    global score

    if selected == pergunta_atual[6]:  # Índice 6 contém o número da resposta correta
        score += 1
        messagebox.showinfo("Correto!", "Resposta correta!")
    else:
        messagebox.showerror("Errado!", "Resposta incorreta.")

    if restantes:
        mostrar_pergunta(restantes[0], restantes[1:])
    else:
        finalizar_quiz()

# Função para exibir perguntas
def mostrar_pergunta(pergunta_atual, restantes):
    pergunta, opcao1, opcao2, opcao3, opcao4, correta = pergunta_atual[1:7]

    question_label.config(text=pergunta)
    btn_opcao1.config(text=opcao1, command=lambda: verificar_resposta(1, pergunta_atual, restantes))
    btn_opcao2.config(text=opcao2, command=lambda: verificar_resposta(2, pergunta_atual, restantes))
    btn_opcao3.config(text=opcao3, command=lambda: verificar_resposta(3, pergunta_atual, restantes))
    btn_opcao4.config(text=opcao4, command=lambda: verificar_resposta(4, pergunta_atual, restantes))

# Função para finalizar o quiz
def finalizar_quiz():
    global user, score

    # Salvar o resultado no banco de dados
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (user_id, score) VALUES ((SELECT id FROM users WHERE username = ?), ?)", (user, score))
    conn.commit()
    conn.close()

    messagebox.showinfo("Fim do Quiz", f"Você acertou {score} perguntas!")
    quiz_window.destroy()

# Função para abrir a interface do quiz
def iniciar_quiz():
    global quiz_window, question_label, btn_opcao1, btn_opcao2, btn_opcao3, btn_opcao4, timer_label

    # Configuração da janela do quiz
    quiz_window = Toplevel(quiz_window)
    quiz_window.title("Quiz Interativo")
    quiz_window.geometry("600x400")
    quiz_window.configure(bg="#ADD8E6")  # Azul claro

    # Label do temporizador
    timer_label = Label(quiz_window, text="", font=("Arial", 14), bg="#ADD8E6")
    timer_label.pack(pady=10)

    # Widgets do quiz
    question_label = Label(quiz_window, text="", font=("Arial", 14), wraplength=500, justify="center", bg="#ADD8E6")
    question_label.pack(pady=20)

    btn_opcao1 = Button(quiz_window, text="", font=("Arial", 12), width=30, bg="#D9A96A")  # Contraste dourado
    btn_opcao1.pack(pady=5)
    btn_opcao2 = Button(quiz_window, text="", font=("Arial", 12), width=30, bg="#D9A96A")
    btn_opcao2.pack(pady=5)
    btn_opcao3 = Button(quiz_window, text="", font=("Arial", 12), width=30, bg="#D9A96A")
    btn_opcao3.pack(pady=5)
    btn_opcao4 = Button(quiz_window, text="", font=("Arial", 12), width=30, bg="#D9A96A")
    btn_opcao4.pack(pady=5)

    # Carregar perguntas
    perguntas = carregar_perguntas()
    if perguntas:
        mostrar_pergunta(perguntas[0], perguntas[1:])
    else:
        messagebox.showerror("Erro", "Nenhuma pergunta disponível!")
        quiz_window.destroy()
