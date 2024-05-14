import time
import schedule

def executar():
    print("Executou!")

i = 1
schedule.every().day.at('17:36').do(executar)

while True:
    print("Ciclo:", i)
    i += 1
    schedule.run_pending()
    time.sleep(1)