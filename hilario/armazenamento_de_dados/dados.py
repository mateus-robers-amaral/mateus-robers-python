import csv

with open('dados_estacao.csv', 'w', newline='') as arquivo:
    final = csv.writer(arquivo, delimiter=';')

    final.writerow(['Pressao', 'Temperatura', 'Umidade'])

with open('dados_estacao.csv') as csv_file:
    arquivo = csv.reader(csv_file, delimiter=';')

    for i in arquivo:
        print(i[0])