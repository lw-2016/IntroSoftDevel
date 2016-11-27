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
