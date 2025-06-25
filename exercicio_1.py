def verificar_nota (nota):
    if nota > 5:
        return ("Aprovado")
    elif nota < 3:
        return ("Reprovado")
    elif 3 > nota < 5:
        return ("Recuperação")
    

print (verificar_nota)
