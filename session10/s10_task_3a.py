class CashRegister :
                     #method_1 -- special method __init__, used to initialize objects(its variables) later in the program,
                     #(or instantiate, because objects are called by some programmers instances) .
                     #When the objects are created this method is called (triggered)
                     #first parameter is self by convention. Equivalent in Java and C++ == this.
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      
   #method_2  does count how many items/products were scanned/inputed
   #and also adds price of particular item to TOTAL price.
   def addItem(self, price) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
   #method_3  in contrast with method_2 which only keep track of total price,
   #method_3 RETURNS total price 
   def getTotal(self) :
      return self._totalPrice
      
   #method_4  returns how many items/products were processed.
   def getCount(self) :
      return self._itemCount

   #method_5 clears count of items and register back to zero presumably for next customer.
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0



