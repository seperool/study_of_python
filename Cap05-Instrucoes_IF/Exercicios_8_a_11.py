#8)
users = ('admin','mario','camila','sergio','gabriela','alexandre')

for user in users:
    if user == 'admin':
        print("Olá " + user + ", gostaria de ver um relatório de status?")
    else:
        print("Olá " + user.title() + ", obrigado por fazer login novamente.")

#9)
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Olá " + user + ", gostaria de ver um relatório de status?")
        else:
            print("Olá " + user.title() + ", obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")

#10)
current_users = ['admin','mario','camila','sergio','gabriela','alexandre']
new_users = ['julio','marcelo','camila','deotan','iasmin']

for user in new_users:
    if user in current_users:
        print("Nome " + user.title() + " já existe. Tente outro nome!")
    else:
        print("Nome de usuário " + user.title() +" disponível!")
#11)
nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    if num == 1:
        print(str(num)+"st")
    elif num == 2:
        print("\n"+str(num)+"nd")
    elif num == 3:
        print("\n"+str(num)+"rd")
    else:
        print("\n"+str(num)+"th")