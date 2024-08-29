#Exemplo de uso "not in"
#not in = Retorna True se não esta na lista
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
  print(user.title() + ", you can post a response if you wish.")
