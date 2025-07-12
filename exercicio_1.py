def verificar_nota (nota):
    if nota > 5:
        return ("Aprovado")
    elif nota < 3:
        return ("Reprovado")
    else:
        return ("Recuperação")

