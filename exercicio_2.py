def criar_organismo (id, nome, tamanho_do_genoma):
       return {
        "id": id,
        "nome": nome,
        "tamanho_do_genoma": tamanho_do_genoma
    }

id = input ("Qual é o id do organismo? ")
nome = input ("Qual o nome do organismo? ")
tamanho_do_genoma = input ("Qual o tamanho do genoma? ")

organismo = criar_organismo (id, nome, tamanho_do_genoma)

print(f"id: {organismo['id']}, nome: {organismo['nome']}, tamanho do genoma: {organismo['tamanho_do_genoma']}")
