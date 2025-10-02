acougue = {
    'carne': ['patinho', 'colchão', 'fraldinha', 'picanha'],
    'preco': [40.50, 19.20, 60.90, 200.00],
    'estoque': [100, 300, 200, 220],
    'validade': ['02/05', '22/09', '12/05', '23/02']
}

def cria_i():
    global indices
    indices = {}
    for i in range(len(acougue['carne'])):
        indices[acougue['carne'][i]] = i
    return indices

cria_i()

def i_maior(lista):
    maior = 0
    for m in range(len(lista)):
        if lista[m] > lista[maior]:
            maior = m
    return maior

def i_menor(lista):
    menor = 0
    for m in range(len(lista)):
        if lista[m] < lista[menor]:
            menor = m
    return menor

def forca(msg, cond):
    print(f"OPÇÕES VÁLIDAS - {cond}")
    escolha = input(f"{msg} \n-->")
    while escolha not in cond:
        print('Resposta Inválida')
        print(f"OPÇÕES VÁLIDAS - {cond}")
        escolha = input(f"{msg} \n-->")
    return escolha


def mostra_carne():
    carne = forca("Qual carne você quer ver", acougue['carne'])
    i = indices[carne]
    print(f'\n=== CARNE ===')
    for c in acougue.keys():
        print(f'{c} - {acougue[c][i]}')
    print('')
    return

def remove_carne():
    carne = forca("Qual carne você quer remover ", acougue['carne'])
    i = indices[carne]
    for c in acougue.keys():
        acougue[c].pop(i)
    cria_i()
    return acougue

def adiciona_carne():
    for x in acougue.keys():
        ad = input(f'Me de a(o) {x} \n ->')
        if ad.isnumeric():
            ad = int(ad)
        acougue[x].append(ad)
    cria_i()
    return acougue

def atualiza_carne():
    carne = forca("Qual carne você quer atualizar", acougue['carne'])
    i = indices[carne]
    for x in acougue.keys():
        s_n = forca(f"Você quer atualizar o(a) {x}".lower(), ["s", "n"])
        if s_n == "s":
            escolha = input(f'Qual a(o) nova(o) {x} \n ->')
            if escolha.isnumeric():
                escolha = int(escolha)
            acougue[x][i] = escolha
    cria_i()
    return acougue

def mostra_dic(dic):
    print(f'\n=== LISTA DE CARNES ===')
    for k, v in dic.items():
        print(f'{k} : {v}')
    return

def cardapio(lista):
    print(f"\n=== CARDAPIO DE CARNES ===")
    for c in range(len(lista)):
        print(f'{lista[c]}')
    print('')

funcs = {
    "mostrar":mostra_carne,
    "remover":remove_carne,
    "adicionar":adiciona_carne,
    "atualizar":atualiza_carne,
}

l_funcs = list(funcs.keys())
l_funcs.append("sair")

while True:
    print("--- MENU ---")
    mostra_dic(acougue)
    print("")
    escolha = forca("O que você quer fazer", l_funcs)
    if escolha == "sair":
        break
    funcs[escolha]()



