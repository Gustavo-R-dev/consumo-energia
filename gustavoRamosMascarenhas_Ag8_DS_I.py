#Pesquisa de Opinião TudoWeb
exce = 0
ruim = 0
print("Pesquisa de Opinião TudoWeb")

for i in range(1, 51):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    print("Opinião: 1-EXCELENTE | 2-BOM | 3-RUIM")
    opiniao = int(input("Digite sua opinião sobre o atendimento: "))
    if opiniao == 1:
        exce = exce + 1
    elif opiniao == 3:
        ruim = ruim + 1
print("\nResultado da Pesquisa")
print(f"Quantidade de notas excelentes: {exce}")
print(f"Quantidade de notas ruins: {ruim}")