import sqlite3

conn = sqlite3.connect('src/db/banco_apostas.db')  # Altere para o caminho correto do seu banco
cursor = conn.cursor()

# Exclui a tabela existente, se necessário
cursor.execute("DROP TABLE IF EXISTS odds;")

# Cria a tabela com a estrutura correta
cursor.execute('''
    CREATE TABLE IF NOT EXISTS odds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site TEXT NOT NULL,
        time_home TEXT NOT NULL,
        time_away TEXT NOT NULL,
        odd_home REAL NOT NULL,
        odd_away REAL NOT NULL,
        odd_draw REAL,
        cartao_home INTEGER,
        cartao_away INTEGER,
        media_gols_home REAL,
        media_gols_away REAL,
        data_partida TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Tabela 'odds' criada com sucesso!")
