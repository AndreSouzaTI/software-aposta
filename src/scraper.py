from data.flashscore import fetch_flashscore_data
from data.dicasbet import fetch_dicasbet_data
from data.academias import fetch_academias_data
from data.bet365 import fetch_bet365_data
from data.bettingexpert import fetch_bettingexpert_data
from data.oddsportal import fetch_oddsportal_data

def scraper():
    print("Iniciando a coleta de dados...")

    # Chama as funções de scraping de cada site
    fetch_flashscore_data()
    #fetch_dicasbet_data()
    fetch_academias_data()
    fetch_bet365_data()
    fetch_bettingexpert_data()
    fetch_oddsportal_data()

