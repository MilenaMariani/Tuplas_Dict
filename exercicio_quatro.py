numeros = int (input("Deseja somar quantos numeros? "))
soma_num = 0
for i in range(numeros):
    numero = (int (input("Digite um numero: ")))
    soma_num = soma_num + numero

print(soma_num)