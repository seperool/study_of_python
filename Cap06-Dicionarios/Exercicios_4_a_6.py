#4)
glossario = {'print':"Imprime na tela uma mensagem.",
             'dicionários':"Os Dicionários permitem conectar informações relacionadas.",
             'lista':"Uma lista é uma coleção de itens em uma ordem em particular.",
             'del':"Quando não houver mais necessidade de uma informação armazenada em um dicionário, podemos usar a instrução del para remover totalmente um par chave-valor.",
             'tuplas':"Tuplas são listas em que os itens não são criadas para mudar (listas imutáveis)."}

for key, value in glossario.items():
    print("\n" + key)
    print(value)

#5)
rios = {
        'nilo':'egito',
        'amazonas':'brasil',
        'tigris':'syria',
        'euphrates':'iran'
        }
for rio, pais in rios.items():
    print("O " + rio.title() + 
          " corre pelo(a) " + 
          pais.title() + ".")

print("\nOs rios são:")
for rio in rios.keys():
    print(rio.title())

print("\nOs paises são:")
for estado in rios.values():
    print(estado.title())

#6)
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'}

pesquisa = ['jen','marcelo','sarah','melissa','jonathan','edward','phil']

for nome in pesquisa:
    if nome in favorite_languages.keys():
        print("Olá " + nome.title() + 
              "! Obrigado por participar da pesquisa.")
    else:
        print("Olá " + nome.title() + 
              "! Gostaria de participar da pesquisa?")