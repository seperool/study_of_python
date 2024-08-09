#importando funções
from random import seed
from random import randint

#função do menu principal
def menu():
	#inicialização de variaveis
	inscricao = "" #inicialização variavel string vazia
	
	while True: #executar o programa enquanto o usuario não escolhe encerrar
		#opçoes do menu
		print("\n**************Menu**************")
		print("escolha a opção desejada:")
		print("1 para nova inscrição")
		print("2 para visualizar inscrição")
		print("3 para encerrar")
		
		#escolha da opção desejada
		opcao = input("digite a opção desejada:")
		
		#opção 1 - inserir nova inscrição
		if opcao == "1":
			inscricao = cadastro()
		
		#opção 2 - visualizar inscrição realizada ou mensagem de erro
		elif opcao == "2":
			
			#mostrar cadastro
			if inscricao != "": #opção se o cadastro não for uma string vazia
				for key, value in inscricao.items():
					print (key+": "+value)
			
			else: #erro se não tiver cadastro
				print("Nenhuma inscrição cadastrada\n")
		
		#opção 3 - encerrar o programa
		elif opcao == "3":
			break
		
		#opção extra - erro na escolha, nenhuma opção valida
		else:
			print("Erro: digite uma opção válida.")
	
#função que faz o cadastro do usuario
def cadastro():
	print("Preenchimento do cadastro:")
	nome =input("digite o nome:")
	email = input("digite o email:")
	tel = input("digite o telefone:")
	curso = input("digite o curso pretendido:")
	voucher = str(nvoucher())
	
	#inseri os dados cadastrados no dicionario inscrição
	inscricao = {'Nome': nome, 'E-mail': email, 'Telefone': tel, 'Curso': curso, 'Voucher': voucher}
	return inscricao

#função que gera o voucher um numero aleatorio entre 100 e 400	
def nvoucher():
	#seed(100)
	numero = randint(100,400)
	return numero

#chama o programa principal
menu()
