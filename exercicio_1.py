def verificar_nota (nota):
    if nota > 5:
        return ("Aprovado")
    elif nota < 3:
        return ("Reprovado")
    else:
        return ("Recuperação")

nota = int (input ("Qual a nota? "))

nota_final = verificar_nota (nota)
print (verificar_nota(nota))
