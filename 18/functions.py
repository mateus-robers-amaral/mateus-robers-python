from cadastro import ficha_cadastral
def telefone():
    while True:
        tel = input("Digite seu número de telefone: \n--->")
        if len(tel) != 11:
            print("Digite o DDD, por favor. O número de telefone deve conter 9 números.")
            continue
        else:
            print("Telefone armazenado com sucesso!")
            tel.append(ficha_cadastral)
            break
    
def certidao():
    while True:
        cpf = input("Digite o número de seu CPF: \n--->")
        if len(cpf) != 11:
            print("O número de CPF deve conter 11 digitos.")
            continue
        else:
            print("Número de CPF arquivado com sucesso!")
            cpf.append(ficha_cadastral)
            break

def conta():
    while True:
        while True:
            agencia = input("Qual o número da sua agência bancária? \n--->")
            if len(agencia) != 4:
                print("O número da agência deve conter apenas 4 números.") 
                continue
            else:
                print("Agência encontrada!")
                agencia.append(ficha_cadastral)
                break
        
        while True:
            tipo_de_conta = input("Qual o tipo da sua conta?\n[1] Poupança\n[2] Conta corrente")
            if tipo_de_conta == "1":
                print("Conta poupança selecionada.") 
                tipo_de_conta.append(ficha_cadastral)
                break
            elif tipo_de_conta == "2":
                print("Conta corrente selecionada.") 
                tipo_de_conta.append(ficha_cadastral)
                break
            else:
                print("Selecione apenas uma das opções.")
                continue
        
        num = input("Digite o número da sua conta: \n--->")
        if len(num) != 10:
            print("O número da conta deve conter 10 digitos. (Tente incluir o dígito / Tente excluir os '0' iniciais)")
            continue
        else:
            print("Número de CPF arquivado com sucesso!")
            break
        