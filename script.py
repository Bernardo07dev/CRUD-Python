acougue = {
 'carne' : ['patinho','colchão','fraldinha','picanha'],
 'preco' : [40.50, 19.20, 60.90, 200.00],
 'estoque' : [100,300,200,220],
 'validade' : ['02/05', '22/09', '12/05', '23/02']
}

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

def acha_i(lista, elem):
  i = 0
  for e in lista:
    if elem == e:
      return i
    else:
      i += 1

def forca(msg, cond):
  escolha = input(msg)
  while escolha not in cond:
    print('Resposta Inválida')
    escolha = input(msg)
  return escolha

def mostra_carne(dic, indice):
  print(f'\n=== CARNE ===')
  for c in dic.keys():
    print(f'{c} - {dic[c][indice]}')
  print('')
  return

def remove_carne(dic, indice):
  for c in dic.keys():
    dic[c].pop(indice)
  return dic

def adiciona_carne(dic):
  for x in dic.keys():
    ad = input(f'Me de a {x} \n ->')
    dic[x].append(ad)
  return dic

def atualiza_carne(dic, indice):
  for x in dic.keys():
    at = input(f'Qual a(o) nova(o) {x} \n ->')
    dic[x][indice] = at
  return dic

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

while True:
  print('=== CLIQUE EM "0" PARA FECHAR O MENU ===')
  menu = forca("O QUE VOCÊ QUER FAZER\n 1 - Mostrar Carne \n 2 - Remover Carne \n 3 - Adicionar Carne \n 4 - Atualizar Carne\n 5 - Mostra Mais Caro \n 6 - Mostrar Mais Barato\n --> ", ['0','1','2','3','4','5','6'])
  if menu == '1':
    carne = forca(f'Qual carne você quer ver:\n {cardapio(acougue['carne'])} \n --> ', acougue['carne'])
    indice_carne = acha_i(acougue['carne'], carne)
    mostra_carne(acougue, indice_carne)
  elif menu == '2':
    carne_rem = forca(f'Qual carne você quer remover\n {cardapio(acougue['carne'])} \n --> ', acougue['carne'])
    i_remove = acha_i(acougue['carne'], carne_rem)
    mostra_dic(remove_carne(acougue, i_remove))
  elif menu == '3':
    add = adiciona_carne(acougue)
    mostra_dic(add)
  elif menu == '4':
    carne_at = forca(f'Qual carne você quer atualizar\n {cardapio(acougue['carne'])} \n --> ', acougue['carne'])
    i_atualiza = acha_i(acougue['carne'], carne_at)
    mostra_dic(atualiza_carne(acougue, i_atualiza))
  elif menu == '5':
    index_caro = i_maior(acougue['preco'])
    mostra_carne(acougue, index_caro)
  elif menu == '6':
    index_barato = i_menor(acougue['preco'])
    mostra_carne(acougue, index_barato)
  elif menu == '0':
    print("\n==0 MENU FECHADO ===\n")
    break
  


  


