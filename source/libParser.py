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
		print("Expressao invalida!")
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
