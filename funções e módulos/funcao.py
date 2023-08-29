def canetas (a,p):
    return a*2 + p*2.5

cazul = int(input("Digite a quantidade de canetas azuis: "))
cpretas = int(input("Digite a quantidade de canetas pretas: "))

print(f'O total a pagar é {canetas(cazul,cpretas)} R$')
