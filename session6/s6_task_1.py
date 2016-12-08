#initial list
a = [ 66.25, 333, 333, 1, 1234.5 ]
print("Initial list is: \t\t\t\t" , a)

#list  after insert(2,-1) and append (333)
a = [ 66.25, 333, 333, 1, 1234.5 ]
a.insert(2, -1)
a =[66.25, 333, -1, 333, 1, 1234.5]
a.append(333)
print("List after inserting -1 and appending 333 is:\t" ,a)

#index 333 displays 1 because 333 is in index position 1 ,66.25 is 0
a= [66.25, 333, -1, 333, 1, 1234.5, 333]
indexing=a.index(333)
indexing1=a.index(1234.5)
print("List indexing(333) : \t\t\t\t" ,indexing)
print("List indexing(1234.5) : \t\t\t" ,indexing1)
#list after a.remove(333), removes first 333 in list
r=[66.25, 333, -1, 333, 1, 1234.5, 333]
r.remove(333)
print("List after removing: \t\t\t\t", r)

#reverse order of items in the list
re =[66.25, -1, 333, 1, 1234.5, 333]
re.reverse()
print("List after reversing operation: \t\t\t", re)

#sort from smallest to highest int
s=[333, 1234.5, 1, 333, -1, 66.25]
s.sort()
print("List after sorting: \t\t\t\t",s)




