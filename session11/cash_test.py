from cash import Cashregister
  
t1=Cashregister() #default , set to 0 , 0.0
t1.addItem(2.99)
t1.addItem(4.99)
t1.addItem(7.99)

#FIRST TEST

#test getTotal()
print("Total Spent:  %0.2f" % t1.getTotal())

#test getCount()
print("Number Of Products Bought: " , t1.getCount())

#test giveChange()
#assuming customer handed £20
print("Give Change: %0.2f  " % t1.giveChange(20))
print()

#SECOND TEST
t2=Cashregister() 
t2.addItem(15.99)
t2.addItem(5.99)
t2.addItem(17.99)

#test getTotal()
print("Total Spent:  %0.2f" % t2.getTotal())
#test getCount()
print("Number Of Products Bought: " , t2.getCount())
#test giveChange()
#assuming customer handed £100
print("Give Change: %0.2f  " % t2.giveChange(50))


