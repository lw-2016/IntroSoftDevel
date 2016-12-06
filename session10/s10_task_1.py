#class named Person
class Person():
        #constructor
	def __init__(self, firstName) :
	        self._name = firstName

#create object of class Person with value: Harry
# using function print(harry)directly would cause to display
#memory address instead of value Harry
#<__main__.Person object at 0x02C81330>	        


#create another 3 example variables person1,2,3
#and assign class name Person with value Tom, Joe and Stephan.
harry = Person("Harry")
person1 =Person("Tom")
person2 =Person("Joe")
person3 =Person("Stephan")

#print our example values
print (harry._name)
print (person1._name)
print (person2._name)
print (person3._name)
