while True:
	
	    n = int (input("\nDigite o termo que queira descobrir na sequência Fibonacci: "))
	
	    i = 0
	    a = 0
	    b = 1
	
	
	    if n > 0:
	
	        print ("\n%dº termo: %d"%(b,b))
	        i += 1
	        a = b
	
	        while i < n:
	
	            
	            print ("\n%dº termo: %d"%(i+1,b))
	            b = a + b
	            i+=1
	            a = b - a
	
	        quest = str(input('\nDeseja continuar? Digite Y p/ sim e N p/ não >>>>   '))
	
	        if quest == 'Y':
	
	            print ("\nVamos começar de novo")
	
	        else:
	
	            break
	
	    else:
	        print ("\nVocẽ não pode digitar zero ou numero negativo")
	        quest = int(input ("\nDigite 0 para sair e 1 para continuar ... "))
	
	        if quest == 1:
	
	            print ("\nVamos começar de novo")
	
	        else:    
	            break

print(i)