import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('banco_apostas.db')
cursor = conn.cursor()

# Consultar todos os registros
cursor.execute('SELECT * FROM odds')
dados = cursor.fetchall()

# Exibir resultados
for linha in dados:
    print(f"Site: {linha[1]} | Jogo: {linha[2]} vs {linha[3]} | Odds: Home {linha[4]} | Away {linha[5]} | Draw {linha[6]} | Cartões: Home {linha[7]}, Away {linha[8]} | Média Gols: Home {linha[9]}, Away {linha[10]} | Data: {linha[11]}")

# Fechar conexão
conn.close()
