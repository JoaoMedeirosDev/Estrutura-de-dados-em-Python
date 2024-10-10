precos_em_dolares = [100, 250, 400, 500]
taxa_de_cambio = 6

precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))

print(precos_em_reais)