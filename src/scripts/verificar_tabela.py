import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('src/db/banco_apostas.db')  # Altere para o caminho correto do seu banco de dados
cursor = conn.cursor()

# Verificar a estrutura da tabela
cursor.execute("PRAGMA table_info(odds);")
columns = cursor.fetchall()

# Imprimir as colunas da tabela
for column in columns:
    print(column)

# Fechar a conexão
conn.close()
