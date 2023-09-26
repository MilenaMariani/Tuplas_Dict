nome_notas = {"milena" : 9, "jose": 5, "renan": 4}
soma = 0
quant_chaves = 0
for chave, valor in nome_notas.items():
    quant_chaves +=1
    soma = soma + valor

media = soma / quant_chaves
print (media)