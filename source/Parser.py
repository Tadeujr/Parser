
#digit ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
def digito(valor):
	dig = ['0','1','2','3','4','5','6','7','8','9']
	
	return (valor in dig)
	

def verificaDigito(expre):
	
	for n in expre:
		if(not digito(n)):
			return False
		
	return True


#Number	
def numero(valor):
	num = ['.','E','e','+','-']
	
	return (valor in num)
	

def verificaNumero(expre):
	
	for n in expre:
		if((not digito(n)) and (not numero(n))):
			return False
	return True

#base::=('+'|'-')base| number | '('expre')'			
def base(valor):
	
	sinal = ['(',')']
	
	if( not (valor in sinal )):
		return False
	
	return True	

def verificaBase(expre):
	
	for n in expre:
		if(not base(n) and not verificaNumero(n)):
			return False
	return True	

#factor ::= base ('^' factor)?
def fator(expre):
	
	for n in expre:
		if(not verificaBase(n) and n != '^'):
			return False
	
	return True	
		
#term ::= factor (('*' | '/' | '//' | '%') factor)*
def termo(valor): # busca verifica os termo da expressao
	
	term = ['*' , '/' , '//' , '%'];
	
	return (valor in term)

#expr ::= term (('+' | '-') term)*

def verificaTermo(expre):
	
	for n in expre:
		if(not(termo(n)) and not (fator(n))):
			return False
	return True	
	
def expressao(expre):	

	for n in expre:
		if(not verificaTermo(n)):
			return False
	
	return True		
	

		
		
		
