idade = int(input("Digite sua idade: "))

if idade <= 7:
    print("Categoria: Infantil A ")
elif idade <= 11:
    print("Categoria: Infantil B ")
elif idade <= 13:
    print("Categoria: Juvenil A ")
elif idade <= 18:
    print("Categoria: Juvenil B ")
else:
    print("Categoria: Adulto ")