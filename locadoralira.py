import os

carros = [
    ("Chevrolet Tracker", 120),
    ("Chervrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Pulse", 130)
]
alugados = []



print("===========")
print("###### Bem vindo à Lira veiculos  #######")
print("===========")

def monstrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros): 
        print("[{}] - {} - R$ {} / dia".format(i, car[0], car[1]))


                    
monstrar_lista_de_carros(carros)


while True:
    os.system("clear")
    print("===========")
    print("###### Bem vindo à Lira veiculos  #######")
    print("===========")
    print("O que deseja fazer?")
    print("0- Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    op = int(input())


    os.system("clear")
    if op == 0:
        monstrar_lista_de_carros(carros)

    elif op == 0:
        pass
    elif op == 1:
        monstrar_lista_de_carros(carros)
        print("============")
        print("Escolha o código do carro:")
        cod_car = int(input())
        print("============")
        print("Por quantos dias você deseja alugar o carro?")
        cod_dias = float(input())
        print("============")
        print("O aluguel totalizaria R$ {}.Deseja alugar?".format(cod_dias * carros[cod_car][1]))
        print("0 - SIM | 1 - NÃO")
        print("============")
        conf = int(input())
        if conf == 0:
            print("Parabéns você alugou o {} por {} dias.".format(carros[cod_car][0], cod_dias))
            alugados.append(carros.pop(cod_car))
        print("=======================================================")
            
    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros alugados")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            monstrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if conf == 0:
                print("Obrigado(a) por devolver o carro {}".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))
    print("")
    print("===========")
    print("Digite 0 para continuar | 1 para Sair")
    if float(input()) == 1:
        break

