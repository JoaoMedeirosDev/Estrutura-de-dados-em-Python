meu_conjunto = set()

meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

print(meu_conjunto)

elemento = 20
if elemento in meu_conjunto:
    print(f'{elemento} está presente no conjunto')
else:
    print(f'{elemento} não está no conjunto.')

meu_conjunto.remove(20)

print("Conjunto após remover o 20:", meu_conjunto)