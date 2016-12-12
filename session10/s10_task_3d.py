class CashRegister :
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price   
   def getTotal(self) :
      return self._totalPrice    
   def getCount(self) :
      return self._itemCount
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

#method implementation giveChange(self, payment)
   def giveChange(self, payment):
      if  payment == self._totalPrice:
         print("Thank You For Shopping: ")
         return 0
      if payment > self._totalPrice:
         print("Give change: ")
         return payment - self._totalPrice
      if payment < self._totalPrice:
         print("Please , you need to pay extra £: ")
         return  payment - self._totalPrice     
#customer 1
register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)
# customer 2
register2 = CashRegister()
register2.addItem(1.90)

print("Customer has to pay:  £",register1.getTotal())
print("Customer has bought : ",register1.getCount() , "products")
#test1 customer hands more than total, requires change 
print(register1.giveChange(20))#assuming that customer handed £20
print()
print("Customer has to pay:  £",register2.getTotal())
print("Customer has bought :",register2.getCount() , "product")
print(register1.giveChange(50))#assuming that customer handed £50


#test2 customer hands less than total needs to be aksed for more money
#print("%.2f" % register1.giveChange(1.5))#assuming that customer handed £1.5
#test3 customer gives exactly total amount , no further action required.
#print(register1.giveChange(1.85))#assuming that customer handed exactly £1.85



