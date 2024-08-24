#Tupla com 5 pratos de restaurante
buffet = ("macarronada","feijoada","lazanha","bife com batata frita","carré")
print("Pratos oferecidos pelo restaurante:")
for prato in buffet:
    print(prato.title())

#Erro
#buffet[2]="omelete"

#Modificando 2 pratos subescrevendo a tupla
buffet=("macarronada","sopa","purê","bife com batata frita","carré")
print("\nNovos pratos oferecidos pelo restaurante:")
for prato in buffet:
    print(prato.title())