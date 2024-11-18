from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def fetch_bet365_data():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://www.bet365.com")  # URL de exemplo, substitua conforme necessário
        print("Página Bet365 carregada com sucesso")

        # Exemplo de scraping (ajuste conforme necessário)
        # element = driver.find_element_by_css_selector('seu-seletor-aqui')
        # print(element.text)

        driver.quit()
    except Exception as e:
        print(f"Erro ao obter dados: {e}")
