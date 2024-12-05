import pandas as pd
import sqlite3


# Carregar arquivo csv em um dataframe pandas
df = pd.read_csv('quiz-questions.csv')

# Ligação à base de dados
conn = sqlite3.connect('quiz.db')
c = conn.cursor()


# Criação da tabela na base de dados
c.execute('''
    CREATE TABLE IF NOT EXISTS quiz (
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        correct integer
    )
''')

# Insert dos dados na tabela
for index, row in df.iterrows():
    c.execute('INSERT INTO quiz (question, option1, option2, option3, option4, correct) VALUES (?, ?, ?, ?, ?, ?)', (row['question'], row['option1'], row['option2'], row['option3'], row['option4'], row['correct']))

df.to_sql('quiz', conn, if_exists='replace', index = False)

pd.read_sql('SELECT * FROM quiz', conn)


# Criação das tabelas registo e resultados na base de dados
c.execute('''
    CREATE TABLE registo (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE resultados (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES registo(id)
    )
''')

# Commit das alterações e fecha a conexão
conn.commit()
conn.close()