from functions import telefone, certidao, conta
import csv

ficha_cadastral = []
inp = int(input("""Olá, como vai? Poderia inserir os valores solicitados?
                \n[1] Sim\n[2] Não\n---> """))
if inp == 1:
    telefone()
    certidao()
else:
    print("Obrigado!")

with open('catalogplay.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"]) # título
    for pessoa in ficha_cadastral:
        writer.writerow(pessoa)