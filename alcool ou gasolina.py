etanol = input('Escreva o preço do etanol: ')
gasolina = input('Escreva o preço da gasolina: ')
divisao = float(etanol) / float(gasolina)
if divisao <= 0.7:
    print('É melhor abastecer com etanol!')
else:
    print('É melhor abastecer com gasolina!')
