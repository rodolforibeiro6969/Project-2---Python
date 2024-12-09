import sqlite3
import tkinter as tk
from tkinter import messagebox
import random
from tkinter import *

# Variáveis globais
user = None
score = 0
correct_index = None
count = 10  # Tempo inicial do temporizador
timer_running = False
timer_id = None

# Função para carregar as perguntas
def carregar_perguntas():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Buscar 10 perguntas aleatórias
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 10")
    perguntas = cursor.fetchall()
    conn.close()
    return perguntas

# Função para mostrar uma pergunta
def mostrar_pergunta(pergunta_atual, restantes):
    global correct_index

    # Reiniciar o temporizador
    reset_timer(count, lambda: mostrar_proxima_pergunta(restantes))

    # Descompactar dados da pergunta
    pergunta, opcao1, opcao2, opcao3, opcao4, correta = pergunta_atual[1:7]

    # Criar uma lista das opções e embaralhar
    opcoes = [(1, opcao1), (2, opcao2), (3, opcao3), (4, opcao4)]
    random.shuffle(opcoes)

    # Identificar o índice da opção correta após o embaralhamento
    for i, opcao in enumerate(opcoes):
        if opcao[0] == correta:
            correct_index = i + 1  # Ajusta para valores 1-4

    # Atualizar a interface gráfica com as opções embaralhadas
    question_label.config(text=pergunta)
    btn_opcao1.config(text=opcoes[0][1], command=lambda: verificar_resposta(1, correct_index, restantes))
    btn_opcao2.config(text=opcoes[1][1], command=lambda: verificar_resposta(2, correct_index, restantes))
    btn_opcao3.config(text=opcoes[2][1], command=lambda: verificar_resposta(3, correct_index, restantes))
    btn_opcao4.config(text=opcoes[3][1], command=lambda: verificar_resposta(4, correct_index, restantes))

# Função para verificar a resposta
def verificar_resposta(selected, correct_index, restantes):
    global score

    # Interrompe o temporizador
    stop_timer()

    if selected == correct_index:
        score += 1
        messagebox.showinfo("Correto!", "Resposta correta!")
    else:
        mensagem = f"Resposta incorreta. A resposta certa era a opção {correct_index}."
        messagebox.showerror("Errado!", mensagem)

    mostrar_proxima_pergunta(restantes)

# Função para mostrar a próxima pergunta ou finalizar o quiz
def mostrar_proxima_pergunta(restantes):
    if restantes:
        mostrar_pergunta(restantes[0], restantes[1:])
    else:
        finalizar_quiz()

# Função para finalizar o quiz
def finalizar_quiz():
    global user, score

    # Interrompe o temporizador
    stop_timer()

    # Guardar pontuação na bd
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (user_id, score) VALUES ((SELECT id FROM users WHERE username = ?), ?)", (user, score))
    conn.commit()
    conn.close()

    # Esconder o temporizador
    timer_label.pack_forget()

    # Finalizar o quiz e desativar os botões
    question_label.config(text=f"Fim do Quiz! Você acertou {score} perguntas.")
    btn_opcao1.config(state="disabled")
    btn_opcao2.config(state="disabled")
    btn_opcao3.config(state="disabled")
    btn_opcao4.config(state="disabled")

# Função para iniciar o quiz
def iniciar_quiz():
    global quiz_window, question_label, btn_opcao1, btn_opcao2, btn_opcao3, btn_opcao4, timer_label

    # Fecha a janela de login e cria a nova janela do quiz
    login_window.destroy()
    quiz_window = Tk()  # A nova janela principal
    quiz_window.title("Quiz Interativo")
    quiz_window.geometry("600x400")
    quiz_window.configure(bg="#ADD8E6")

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

# Função do temporizador
def countdown(count, on_timeout):
    global timer_running, timer_id

    if count > 0:
        timer_label.config(text=f"Tempo restante: {count}s")
        timer_id = quiz_window.after(1000, countdown, count - 1, on_timeout)
    else:
        stop_timer()
        messagebox.showinfo("Tempo esgotado", "O tempo acabou!")
        on_timeout()

# Função para reiniciar o temporizador
def reset_timer(count, on_timeout):
    stop_timer()
    countdown(count, on_timeout)

# Função para interromper o temporizador
def stop_timer():
    global timer_id

    if timer_id:
        quiz_window.after_cancel(timer_id)
        timer_id = None

# Função de login
def login_utilizador():
    global user

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Verificar credenciais
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        user = username
        messagebox.showinfo("Sucesso", f"Bem-vindo, {username}!")
        iniciar_quiz()
    else:
        messagebox.showerror("Erro", "Utilizador ou palavra-passe inválidas!")

# Função para registar um utilizador
def registar_utilizador():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Registo concluído! Agora faça login.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Utilizador já existe!")

# Interface de login/registo
login_window = Tk()
login_window.title("Login/Registo")
login_window.geometry("400x300")
login_window.configure(bg="#001F54")

Label(login_window, text="Nome de utilizador:", font=("Arial", 12), bg="#001F54", fg="white").pack(pady=10)
username_entry = Entry(login_window, font=("Arial", 12))
username_entry.pack()

Label(login_window, text="Palavra-Passe:", font=("Arial", 12), bg="#001F54", fg="white").pack(pady=10)
password_entry = Entry(login_window, show="*", font=("Arial", 12))
password_entry.pack()

Button(login_window, text="Login", font=("Arial", 12), command=login_utilizador, bg="#D9A96A").pack(pady=10)
Button(login_window, text="Registar", font=("Arial", 12), command=registar_utilizador, bg="#D9A96A").pack()

login_window.mainloop()
