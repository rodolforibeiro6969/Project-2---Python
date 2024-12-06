import sqlite3
import pandas as pd

# def criar_tabelas():
#     # Conecta ao banco de dados ou cria-o se não existir
#     conn = sqlite3.connect("quiz.db")
#     cursor = conn.cursor()
#
#     # Criação da tabela de usuários
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE NOT NULL,
#         password TEXT NOT NULL,
#         score INTEGER DEFAULT 0
#     )
#     ''')
#
#     # Criação da tabela de perguntas
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS questions (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         question TEXT NOT NULL,
#         option1 TEXT NOT NULL,
#         option2 TEXT NOT NULL,
#         option3 TEXT NOT NULL,
#         option4 TEXT NOT NULL,
#         correct INTEGER NOT NULL
#     )
#     ''')
#
#     # Criação da tabela de resultados
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS results (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         score INTEGER NOT NULL,
#         date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         FOREIGN KEY (user_id) REFERENCES users (id)
#     )
#     ''')
#
#     # Confirma as alterações e fecha a conexão
#     conn.commit()
#     conn.close()
#     print("Tabelas criadas com sucesso!")
#
# # Executa a criação das tabelas
# if __name__ == "__main__":
#     criar_tabelas()
#

# def importar_perguntas_do_csv(nome_arquivo):
#     try:
#         # Ler o arquivo CSV
#         perguntas_df = pd.read_csv(nome_arquivo)
#
#         # Validar colunas esperadas
#         colunas_esperadas = ['question', 'option1', 'option2', 'option3', 'option4', 'correct']
#         if not all(coluna in perguntas_df.columns for coluna in colunas_esperadas):
#             print("Erro: O arquivo CSV não contém todas as colunas necessárias!")
#             return
#
#         # Conectar ao banco de dados
#         conn = sqlite3.connect("quiz.db")
#         cursor = conn.cursor()
#
#         # Inserir perguntas no banco de dados
#         for _, linha in perguntas_df.iterrows():
#             cursor.execute('''
#                 INSERT INTO questions (question, option1, option2, option3, option4, correct)
#                 VALUES (?, ?, ?, ?, ?, ?)
#             ''', (linha['question'], linha['option1'], linha['option2'], linha['option3'], linha['option4'], linha['correct']))
#
#         conn.commit()
#         conn.close()
#
#         print("Perguntas importadas com sucesso!")
#     except Exception as e:
#         print(f"Erro ao importar perguntas: {e}")
#
# # Executar a função
# importar_perguntas_do_csv(r"C:\Users\Pedro\Desktop\projeto2 Nelson\quiz-questions.csv")


def corrigir_respostas():
    # Conectar ao banco de dados
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Dicionário com perguntas e os índices corretos (substitua os valores pelos corretos)
    data = [
        ["Qual é o país mais populoso do mundo?", "China", "Índia", "EUA", "Indonésia", 1],
        ["Qual é o elemento químico mais abundante no universo?", "Hidrogénio", "Hélio", "Oxigénio", "Carbono", 1],
        ["Qual é o rio mais extenso de Portugal?", "Tejo", "Douro", "Guadiana", "Mondego", 1],
        ["Em que ano foi fundada a União Europeia?", "1993", "1957", "1989", "1995", 2],
        ['Quem escreveu "Os Lusíadas"?', "Luís de Camões", "Fernando Pessoa", "Eça de Queirós", "Gil Vicente", 1],
        ["Qual é a moeda oficial do Japão?", "Iene", "Yuan", "Won", "Ringgit", 1],
        ["Qual é o osso mais longo do corpo humano?", "Fémur", "Tíbia", "Úmero", "Rádio", 1],
        ["Em que ano começou a Primeira Guerra Mundial?", "1914", "1916", "1918", "1912", 1],
        ["Qual é a capital da Austrália?", "Camberra", "Sydney", "Melbourne", "Brisbane", 1],
        ["Quem inventou o telefone?", "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "James Watt", 1],
        ["Qual é o metal mais precioso?", "Ródio", "Ouro", "Platina", "Paládio", 2],
        ["Em que ano foi descoberto o Brasil?", "1500", "1492", "1498", "1502", 1],
        ["Qual é o maior mamífero terrestre?", "Elefante africano", "Rinoceronte", "Hipopótamo", "Girafa", 1],
        ['Quem pintou "A Última Ceia"?', "Leonardo da Vinci", "Michelangelo", "Rafael", "Botticelli", 1],
        ["Qual é a velocidade da luz?", "299.792 km/s", "199.792 km/s", "399.792 km/s", "249.792 km/s", 1],
        ["Em que ano terminou a Segunda Guerra Mundial?", "1945", "1944", "1946", "1943", 1],
        ["Qual é o planeta mais quente do sistema solar?", "Vénus", "Mercúrio", "Marte", "Júpiter", 1],
        ["Quem descobriu a penicilina?", "Alexander Fleming", "Louis Pasteur", "Marie Curie", "Robert Koch", 1],
        ["Qual é a capital do Canadá?", "Otava", "Toronto", "Vancouver", "Montreal", 1],
        ["Qual é o maior deserto do mundo?", "Antártida", "Saara", "Ártico", "Gobi", 1],
        ["Qual é o símbolo químico do ouro?", "Au", "Ag", "Fe", "Cu", 1],
        ["Em que ano foi fundada a ONU?", "1945", "1944", "1946", "1947", 1],
        ["Qual é o maior órgão do corpo humano?", "Pele", "Fígado", "Intestino", "Pulmões", 1],
        ['Quem escreveu "Dom Quixote"?', "Miguel de Cervantes", "William Shakespeare", "Dante Alighieri", "Victor Hugo",
         1],
        ["Qual é a montanha mais alta de Portugal Continental?", "Serra da Estrela", "Serra do Gerês", "Serra do Marão",
         "Serra da Lousã", 1],
        ["Em que ano foi implementado o Euro?", "1999", "1998", "2000", "2001", 1],
        ["Qual é o maior oceano do mundo?", "Pacífico", "Atlântico", "Índico", "Ártico", 1],
        ["Quem foi o primeiro presidente dos EUA?", "George Washington", "Thomas Jefferson", "John Adams",
         "Benjamin Franklin", 1],
        ["Qual é o metal mais abundante na crosta terrestre?", "Alumínio", "Ferro", "Cobre", "Zinco", 1],
        ["Em que ano foi abolida a monarquia em Portugal?", "1910", "1908", "1912", "1914", 1],
        ["Qual é a capital da Nova Zelândia?", "Wellington", "Auckland", "Christchurch", "Hamilton", 1],
        ["Quem desenvolveu a teoria da relatividade?", "Albert Einstein", "Isaac Newton", "Stephen Hawking",
         "Niels Bohr", 1],
        ["Qual é o maior animal do mundo?", "Baleia-azul", "Elefante africano", "Tubarão-baleia", "Cachalote", 1],
        ["Em que ano foi fundada a NATO?", "1949", "1947", "1951", "1953", 1],
        ["Qual é o elemento mais pesado da tabela periódica?", "Oganésson", "Urânio", "Plutónio", "Férmio", 1],
        ['Quem pintou "O Grito"?', "Edvard Munch", "Vincent van Gogh", "Pablo Picasso", "Claude Monet", 1],
        ["Qual é a capital da Dinamarca?", "Copenhaga", "Oslo", "Estocolmo", "Helsínquia", 1],
        ["Em que ano começou a Revolução Industrial?", "1760", "1750", "1770", "1780", 1],
        ["Qual é o maior lago de água doce do mundo?", "Lago Superior", "Lago Vitória", "Lago Huron", "Lago Michigan", 1],
        ['Quem escreveu "O Principezinho"?', "Antoine de Saint-Exupéry", "Jules Verne", "Victor Hugo", "Albert Camus", 1],
        ["Qual é o país mais extenso da América do Sul?", "Brasil", "Argentina", "Peru", "Colômbia", 1],
        ["Em que ano foi descoberta a América?", "1492", "1489", "1495", "1498", 1],
        ["Qual é o menor planeta do sistema solar?", "Mercúrio", "Marte", "Vénus", "Plutão", 1],
        ["Quem foi o primeiro homem a circum-navegar o globo?", "Fernão de Magalhães", "Vasco da Gama", "Cristóvão Colombo", "Pedro Álvares Cabral", 1],
        ["Qual é a língua mais falada no mundo?", "Mandarim", "Inglês", "Hindi", "Espanhol", 1],
        ["Em que ano foi construído o Muro de Berlim?", "1961", "1959", "1963", "1965", 1],
        ["Qual é o maior arquipélago do mundo?", "Indonésia", "Filipinas", "Japão", "Maldivas", 1],
        ["Quem descobriu a radioatividade?", "Marie Curie", "Albert Einstein", "Isaac Newton", "Niels Bohr", 1],
        ["Qual é a capital da Suíça?", "Berna", "Zurique", "Genebra", "Basileia", 1],
        ["Em que ano foi assinada a Declaração Universal dos Direitos Humanos?", "1948", "1946", "1950", "1952", 1],
        ["Qual é o maior felino do mundo?", "Tigre-siberiano", "Leão", "Jaguar", "Leopardo", 1],
        ['Quem compôs a "Nona Sinfonia"?', "Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Franz Schubert", 1],
        ["Qual é o ponto mais baixo da Terra?", "Mar Morto", "Vale da Morte", "Depressão de Qattara", "Grande Vale do Rift", 1],
        ["Em que ano foi inventada a internet?", "1969", "1971", "1973", "1975", 1],
        ["Qual é a capital da Coreia do Sul?", "Seul", "Busan", "Incheon", "Daegu", 1],
        ['Quem escreveu "1984"?', "George Orwell", "Aldous Huxley", "Ray Bradbury", "H.G. Wells", 1],
        ["Qual é o segundo elemento mais abundante no corpo humano?", "Carbono", "Hidrogénio", "Nitrogénio", "Cálcio", 1],
        ["Em que ano foi fundada a UNESCO?", "1945", "1944", "1946", "1947", 1],
        ["Qual é o maior primata do mundo?", "Gorila-das-montanhas", "Orangotango", "Chimpanzé", "Gibão", 1],
        ["Quem inventou a lâmpada elétrica?", "Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Michael Faraday", 1],
        ["Qual é a capital da Grécia?", "Atenas", "Tessalónica", "Patras", "Heraclião", 1],
        ["Em que ano foi descoberta a Austrália?", "1770", "1768", "1772", "1774", 1],
        ["Qual é o rio mais longo do mundo?", "Nilo", "Amazonas", "Yangtzé", "Mississippi", 1],
        ["Quem foi o primeiro europeu a chegar à Índia por mar?", "Vasco da Gama", "Fernão de Magalhães", "Bartolomeu Dias", "Cristóvão Colombo", 1],
        ["Qual é a maior ilha do mundo?", "Gronelândia", "Nova Guiné", "Bornéu", "Madagascar", 1],
        ["Em que ano foi inventada a televisão?", "1925", "1923", "1927", "1929", 1],
        ["Qual é o elemento químico mais pesado encontrado naturalmente?", "Urânio", "Plutónio", "Tório", "Rádio", 1],
        ['Quem pintou a "Guernica"?', "Pablo Picasso", "Salvador Dalí", "Joan Miró", "Henri Matisse", 1],
        ["Qual é a capital do México?", "Cidade do México", "Guadalajara", "Monterrey", "Puebla", 1],
        ["Em que ano foi fundada a Cruz Vermelha?", "1863", "1861", "1865", "1867", 1],
        ["Qual é o maior réptil do mundo?", "Crocodilo-de-água-salgada", "Anaconda-verde", "Dragão-de-komodo", "Tartaruga-de-couro", 1],
        ["Quem descobriu a estrutura do DNA?", "Watson e Crick", "Franklin e Wilkins", "Mendel e Morgan", "Darwin e Wallace", 1],
        ["Qual é a moeda oficial da Rússia?", "Rublo", "Coroa", "Franco", "Marco", 1],
        ["Em que ano foi abolida a escravatura no Brasil?", "1888", "1886", "1890", "1892", 1],
        ["Qual é o maior vulcão do sistema solar?", "Monte Olimpo", "Monte Everest", "Mauna Kea", "Kilimanjaro", 1],
        ['Quem escreveu "O Pequeno Príncipe"?', "Antoine de Saint-Exupéry", "Jules Verne", "Victor Hugo", "Albert Camus", 1],
        ["Qual é a capital da Índia?", "Nova Deli", "Mumbai", "Calcutá", "Bangalore", 1],
        ["Em que ano foi inventado o primeiro computador eletrônico?", "1946", "1944", "1948", "1950", 1],
        ["Qual é o maior peixe do mundo?", "Tubarão-baleia", "Baleia-azul", "Espadarte", "Marlim-azul", 1],
        ["Quem foi o primeiro homem no espaço?", "Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "Alan Shepard", 1],
        ["Qual é o ponto mais alto da África?", "Kilimanjaro", "Monte Quénia", "Monte Stanley", "Ras Dashen", 1],
        ["Em que ano foi fundada a NASA?", "1958", "1956", "1960", "1962", 1],
        ["Qual é o maior anfíbio do mundo?", "Salamandra-gigante-chinesa", "Sapo-cururu", "Rã-touro", "Axolote", 1],
        ["Quem inventou a vacina?", "Edward Jenner", "Louis Pasteur", "Robert Koch", "Alexander Fleming", 1],
        ["Qual é a capital da Argentina?", "Buenos Aires", "Córdoba", "Rosário", "Mendoza", 1],
        ["Em que ano foi inventado o automóvel?", "1885", "1883", "1887", "1889", 1],
        ["Qual é o maior asteroide do sistema solar?", "Ceres", "Vesta", "Pallas", "Hygiea", 1],
        ['Quem escreveu "Romeu e Julieta"?', "William Shakespeare", "Christopher Marlowe", "Ben Jonson", "John Webster", 1],
        ["Qual é a capital da Holanda?", "Amesterdão", "Roterdão", "Haia", "Utrecht", 1],
        ["Em que ano foi fundado o Banco de Portugal?", "1846", "1844", "1848", "1850", 1],
        ["Qual é o maior carnívoro terrestre?", "Urso-polar", "Tigre-siberiano", "Leão", "Urso-pardo", 1],
        ["Quem descobriu a lei da gravidade?", "Isaac Newton", "Galileu Galilei", "Johannes Kepler", "Albert Einstein", 1],
        ["Qual é o metal mais condutor de eletricidade?", "Prata", "Cobre", "Ouro", "Alumínio", 1],
        ["Em que ano foi inventado o telefone móvel?", "1973", "1971", "1975", "1977", 1],
        ["Qual é o maior satélite natural do sistema solar?", "Ganimedes", "Titã", "Calisto", "Io", 1],
        ['Quem pintou "A Noite Estrelada"?', "Vincent van Gogh", "Claude Monet", "Paul Gauguin", "Edgar Degas", 1],
        ["Qual é a capital da Turquia?", "Ancara", "Istambul", "Esmirna", "Bursa", 1],
        ["Em que ano foi criada a World Wide Web?", "1989", "1987", "1991", "1993", 1],
        ["Qual é o maior cefalópode do mundo?", "Lula-gigante", "Polvo-gigante-do-pacífico", "Nautilus", "Sépia-gigante", 1],
        ["Quem inventou o rádio?", "Guglielmo Marconi", "Nikola Tesla", "Thomas Edison", "Alexander Graham Bell", 1],
        ["Qual é a montanha mais alta da Europa?", "Monte Elbrus", "Monte Branco", "Monte Rosa", "Matterhorn", 1],
        ["Em que ano foi fundada a primeira universidade portuguesa?", "1290", "1288", "1292", "1294", 1],
        ["Qual é o maior aquífero do mundo?", "Sistema Aquífero Guarani", "Grande Bacia Artesiana", "Aquífero Núbio", "Aquífero High Plains", 1],


    ]

    # Atualizar a tabela com os índices corretos
    columns = ["Question", "Option1", "Option2", "Option3", "Option4", "Correct"]
    df = pd.DataFrame(data, columns=columns)

    # Salvar o arquivo corrigido
    output_file = "quiz-questions-corrected.xlsx"
    df.to_excel(output_file, index=False)

    print(f"As perguntas corrigidas foram salvas em: {"quiz-questions.csv"}")

# Chamar a função para corrigir
corrigir_respostas()
