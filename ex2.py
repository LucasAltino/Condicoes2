valor = float(input("Digite o valor das prestações: "))
quant = int(input("Digite a quantidade de prestações: "))
total = valor / quant

if total > 500:
    print("Você não conseguirá pagar")
else:
    print("Você consegue pagar")