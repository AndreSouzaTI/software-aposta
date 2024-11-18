import schedule
import time
from src.main import main

def job():
    print("Executando o job de coleta de dados...")
    main()

# Agendar o job para rodar a cada 10 minutos
schedule.every(10).minutes.do(job)

# Loop para verificar e rodar o job
while True:
    schedule.run_pending()
    time.sleep(1)
