import sqlite3

from scraper.flashscore import scrape_flashscore
from scraper.dicasbet import scrape_dicasbet
from scraper.bet365 import scrape_bet365
from scraper.bettingexpert import scrape_bettingexpert
from scraper.oddsportal import scrape_oddsportal

# Conectar ao banco de dados
conn = sqlite3.connect('banco_apostas.db')
cursor = conn.cursor()

# Coletar dados de todos os scrapers
todos_dados = []
todos_dados.extend(scrape_flashscore())
todos_dados.extend(scrape_dicasbet())
todos_dados.extend(scrape_bet365())
todos_dados.extend(scrape_bettingexpert())
todos_dados.extend(scrape_oddsportal())

# Inserir dados no banco
for registro in todos_dados:
    cursor.execute('''
        INSERT INTO odds (site, time_home, time_away, odd_home, odd_away, odd_draw, cartao_home, cartao_away, media_gols_home, media_gols_away, data_partida)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', registro)

# Salvar mudanças e fechar conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso!")
