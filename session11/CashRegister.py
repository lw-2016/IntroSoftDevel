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
     
         return 0
      if payment > self._totalPrice:

         return payment - self._totalPrice
      if payment < self._totalPrice:
  
         return  payment - self._totalPrice  
