def remover(lista):
    nova = []
    for obj in lista:
        novo_obj = {}
        for chave, valor in obj.items():
            if chave == "nome":
                novo_obj[''] = valor
            else:
                novo_obj[chave] = valor
        nova.append(novo_obj)
    return nova
champ = [
    {"nome": "Ahri", "Mid": "Mago"},
    {"nome": "Pyke", "Suporte": "Assasino"},
    {"nome": "illaoi", "Top": "Lutador"}
]
campeão = remover(champ)
print(campeão)