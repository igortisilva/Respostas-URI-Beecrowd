from num2words import num2words as n
num = int(input("Digite"))
saida = n(num, lang = 'pt-br')
print(saida)
