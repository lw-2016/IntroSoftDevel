'''
What are the values of register1._itemCount,
register1._totalPrice,
register2._itemCount
register2._totalPrice after these statements?
'''
register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(0.95)
register2 = CashRegister()
register2.addItem(1.90)




class CashRegister :
# Comment 1
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      
   # Comment 2
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
   # Comment 3
   def getTotal(self) :
      return self._totalPrice
      
   # Comment 4
   def getCount(self) :
      return self._itemCount

   # Comment 5
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

