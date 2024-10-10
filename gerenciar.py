convidados = ['Adrielle', 'Matteo', 'Heitor', 'Hector', 'Jefferson']

confirmaram = ['Adrielle', 'Matteo', 'Hector']

nao_confirmaram = [convidados for convidados in convidados if convidados not in confirmaram]
print("Convidados que ainda não confirmaram:")
for pessoa in nao_confirmaram:
    print(pessoa)

print("Enviando lembrente aos que não confirmaram a presença na festa!")

