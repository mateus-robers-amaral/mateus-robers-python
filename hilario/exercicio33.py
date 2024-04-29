while True:
    num1 = int(input("Digite o primeiro número:\n-> "))
    num2 = int(input("Digite o segundo número:\n-> "))
    total = 0
    if num1 < num2:
        for i in range(num1, num2 + 1):
            total += i
        print(total)
        break
    elif num1 > num2:
        quest = int(input("O primeiro número deve ser menor que o segundo. Deseja tentar novamente?\n[1] Sim\n[2] Não\n-> "))
        if quest == 1:
            continue
        elif quest == 2:
            exit()