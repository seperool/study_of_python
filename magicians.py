magicians = ['alice','david','caroline']
for magician in magicians: #estrutura do for > for variavel in lista :
	print (magician.title()+ ", that was a great trick!")  #linha indentada, dentro do laço for
	print ("I can't wait to see your next trick, " + magician.title()+'\n')
print ('Thank you, everyone. That was a great magic show!') # linha não indentada, fora do laço for
