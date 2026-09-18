"""Write Python program to perform followingoperations on Lists:
(a) list( ), (b) len( ), (c) count( ), (d) index ( ), (e) append( ),(f) insert( ), (g) extend(),
(h) remove( ), (i) pop( ), (j) reverse( ), (k) sort( ), (l) copy( ) and (m) clear( )"""
#list() function  
list1 = list("Hello")
print(f"List created from string: {list1}")
#len() function
list2 = [1, 2, 3, 4, 5]
print(f"Length of the list: {len(list2)}")
#count() function
print(f"Count of 3 in the list: {list2.count(3)}")
#index() function
print(f"Index of 2 in the list: {list2.index(2)}")  
#append() method
list2.append(4)
print(f"List after append(): {list2}")  
#insert() method
list2.insert(1, 10)
print(f"List after insert(): {list2}")  
#extend() method
list2.extend([4, 5])
print(f"List after extend(): {list2}") 
#remove() method
list2.remove(3)
print(f"List after remove(): {list2}")  
#pop() method
list2.pop()
print(f"List after pop(): {list2}")  
#reverse() method
list2.reverse()
print(f"List after reverse(): {list2}")  
#sort() method
list2.sort()
print(f"List after sort(): {list2}")  
#copy() method
list3 = list2.copy()
print(f"Original list: {list2}")
print(f"Copied list: {list3}")
#clear() method
list2.clear()
print(f"List after clear(): {list2}")
