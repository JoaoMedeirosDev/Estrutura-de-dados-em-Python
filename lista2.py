linguagens = ['Python', 'JavaScript', 'Kotlin', 'C', 'C#', 'C++']

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("Depois da listcomp = ", linguagens)