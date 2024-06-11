resp = 'V'
while resp.upper() == 'V':
    print("\nInforme o intervalo para fazer a sona")
    ini = int(input("Início: "))
    fim = int(input("Final: "))
    if fim<ini:
        x=ini
        ini=fim
        fim=x
    i=ini
    soma=0
    while i<=fim:
        soma+=ini
        i+=1
    print("\nA soma entre {} e {} é {}".format(ini,fim,soma))
    resp=input("Digite V para realizar novamente: ")