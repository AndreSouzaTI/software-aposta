import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('src/db/banco_apostas.db')
cursor = conn.cursor()

# Adicionando novas colunas na tabela 'odds'
cursor.execute('''
    ALTER TABLE odds
    ADD COLUMN odd_draw REAL;
''')

cursor.execute('''
    ALTER TABLE odds
    ADD COLUMN cartao_home INTEGER;
''')

cursor.execute('''
    ALTER TABLE odds
    ADD COLUMN cartao_away INTEGER;
''')

cursor.execute('''
    ALTER TABLE odds
    ADD COLUMN media_gols_home REAL;
''')

cursor.execute('''
    ALTER TABLE odds
    ADD COLUMN media_gols_away REAL;
''')

# Salvando as mudanças e fechando a conexão
conn.commit()
conn.close()