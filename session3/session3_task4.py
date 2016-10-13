#task 4 session 3

'''
there is 17 terms to test suitability for variable.
each term was assigned value=1.
cycle through utlil IDLE returns error. Then proceed until end of list.
'''

apple = 1
APPLE = 1
Apple2 = 1  
#1Apple = 1                        <---first error var name can not start with a number
#account number = 1  <---second error no spaces allowed
account_number  = 1
#account.number = 1  <--- third error 
accountNumber = 1 
fred = 1 
Fred = 1
Return = 1
return_value = 1 
#5Return = 1  <---forth error again no numbers as first characker.
GreatBigVariable = 1 
greatBigVariable = 1 
great_big_variable = 1 
#great.big.variable = 1   <---fifth error



#here are included variables accepted by Idle  
print (apple+APPLE+Apple2+account_number +accountNumber+ fred +Fred + Return + return_value +GreatBigVariable +greatBigVariable + great_big_variable  )



"""
#out of  17 terms to test following 5 terms were found illegal:

1Apple                      <---first error: variable names can not start with a number
account number  <---second error: no spaces allowed
account.number <--- third error: no dots allowed 
5Return <---fourth error: again no numbers as first character.
great.big.variable =   <---fifth error : no dots between strings only underscore is allowed

program returns 12 (_17 terms -5 illegals commented)

"""
