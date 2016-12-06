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

     #method implementation getPounds()
   def getPounds(self):
      return self._totalPrice
   
#customer 1
register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)

# customer 2
register2 = CashRegister()
register2.addItem(1.90)

print("Customer has to pay:  £",register1.getTotal())
print("Customer has bought : ",register1.getCount() , "product")
print("Let's forget about pennies, only whole pounds matter:  £%0.d" % register1.getPounds())
print()
print("Customer has to pay:  £",register2.getTotal())
print("Customer has bought :",register2.getCount() , "products")
print("Let's forget about pennies, only whole pounds matter:  £ %0.d" % register2.getPounds())
