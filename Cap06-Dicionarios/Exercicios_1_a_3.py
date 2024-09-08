#1)
pessoa = {'fist_name':'josé',
          'last_name':'souza',
          'age':42,
          'city':'nova iguaçu'
          }
print(pessoa)

#2)
number_faverite = {'mario':42,
                   'ricardo':54,
                   'sergio':29,
                   'marcela':96,
                   'rafaela':12}
print("O número favorito do Mario é "+
      str(number_faverite['mario'])+
      ".")
print("O número favorito do Ricardo é "+
      str(number_faverite['ricardo'])+
      ".")
print("O número favorito do Sergio é "+
      str(number_faverite['sergio'])+
      ".")
print("O número favorito da Marcela é "+
      str(number_faverite['marcela'])+
      ".")
print("O número favorito da rafaela é "+
      str(number_faverite['rafaela'])+
      ".")

#3)
glossario = {'print':"Imprime na tela uma mensagem.",
             'dicionários':"Os Dicionários permitem conectar informações relacionadas.",
             'lista':"Uma lista é uma coleção de itens em uma ordem em particular.",
             'del':"Quando não houver mais necessidade de uma informação armazenada em um dicionário, podemos usar a instrução del para remover totalmente um par chave-valor.",
             'tuplas':"Tuplas são listas em que os itens não são criadas para mudar (listas imutáveis)."}

print('print: '+
      glossario['print'])
print('\nDicionários: '+
      glossario['dicionários'])
print('\nlista: '+
      glossario['lista'])
print('\ndel: '+
      glossario['del'])
print('\nTuplas: '+
      glossario['tuplas'])
