from CashRegister import *
  
t1=CashRegister()
t1.addItem(2.99)
t1.addItem(4.99)
t1.addItem(7.99)
t1.addItem(5.99)
t1.addItem(3.99)
t1.addItem(1.99)
t1.addItem(15.99)
t1.addItem(5.99)
t1.addItem(17.99)


#test getTotal()
print("Total Spent:  %0.2f" % t1.getTotal())

#test getCount()
print("Number Of Products Bought: " , t1.getCount())

#test giveChange()
#assuming customer handed £100
print("Give Change: %0.2f  " % t1.giveChange(100))





