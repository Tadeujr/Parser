###vai receber dois numero para operar vou fazer um funcao so para enviar para aqui

import Parser

def removeBranco(expre):
	vet = []
	
	if(" " not in expre and '' not in expre):
		return expre
		
	for i in expre:
		if(i != " " and i !=''):
			vet.append(i)
	
	return vet
			

def separaExpre(expre): 
	vet = []
	vet = removeBranco(expre)
	if(not Parser.expressao(vet)):
		return False
	else:
		numA = ""
		numB = None
		vetM = []
		vetSaida = []
		
		for i in vet:
			
			if(i=='(' or i in ['*' , '/' , '//' , '%','^','+','-'] ):
				
				if(i == '(' ):
					vetM.append(i)
				else:
					vetM.append(numA)
					vetM.append(i)
					
				numA = ''				
			elif(Parser.digito(i) or i == '.'):
				numA+=i
			elif(Parser.verificaTermo(i)):
				
				vetM.append(numA)
				vetM.append(i)
				numA = ''
			
		if(numA != ''):
			vetM.append(numA)	
		
		vetSaida = removeBranco(vetM)
		
		return vetSaida

def convertNumero(expre):
	nA = ""
	total = None
	
	for n in  expre: # so numeros
		if(digito(n) or '.'):
			nA += n
	
	total =  float(nA)
	
	print(total)

	
def precedencia(expre):#calculo da base
	caracter = []
	separador = []
	
	for i in range(len(expre)-1,-1,-1):#tam, parada, decremento ou incremento
		if(expre[i]!=')' and expre[i]!='('):
			
			caracter.append(expre[i])
				
		elif(expre[i] == '('):
			separador.append(caracter)
		
		else:
			print("Erro: esta faltando parentese ")	
						
		#elif(expre[i] == '^'):
		#	caracter.append(expre[i-1])
		#	caracter.append(expre[i+1])

	return caracter


def separaSinal(expre):#mudardenome
	
	if(not verificaExpressao(expre)):
		return False
	
	else:
		#busca parenteses
		print(precedencia(expre))
			
	
def transformaExpressao(expre):
	saida = None
	aux = ''
	vetAux = separaExpre(expre)
	vetSaida = []
	numA = None
	numB = None
	if(not separaExpre(expre)):
	
		return False
	else:
		for i in vetAux:
			
			if(i == '(' or i == ')'):
				vetSaida.append(i)	
			
			elif(Parser.verificaDigito(i) or '.' in i):
				numA = float(i)
				vetSaida.append(numA)
			else:
				vetSaida.append(i)	
			
	return vetSaida

def calculaExpre(numA, numB, oper):
	cashe = 0.0 
		
	if(oper == '+'):
		cashe = numA+numB
		
	elif(oper == '-'):
		cashe = numA-numB			
	
	elif(oper == '^'):

		cashe = numA**numB		

	elif(oper == '%'):

		cashe = numA % numB

	elif(oper == '/'):

		cashe = numA/numB

	elif(oper == '//'):

		cashe = numA // numB
			
	elif(oper == '*'):

		cashe = numA*numB
		

														
	return cashe
	

def final(expre):
	vet = transformaExpressao(expre)
	numA = 0.0
	numB = 0.0
	sinal = ''
	resultado = 0.0
	cont = 0
	total = 0.0
	
	if(not transformaExpressao(expre)):
		return False
	
	for i in vet:
		
		if(type(i) == float):
			
			if(sinal == ''):
				numA = i
			
			elif(sinal!='' and cont == 0 ):
				numB = i
				resultado = calculaExpre(numA, numB, sinal)
				
				numA = 0.0
				numB = 0.0
				cont+=1
			
			elif(cont > 0 ):
				
				resultado = calculaExpre(resultado, i, sinal)
				
				sinal =''
				cont = 0
			
			
				
		elif(Parser.termo(i) or i in ['^','+','-','/','//']):
			sinal = i
			

	print(resultado)
														
	#return total 
