"""Demonstrate the following functions/methods which operates on strings in Python with suitable examples:
   (a) len( ),(b) strip( ),(c) rstrip( ),(d) lstrip( ), (e) find( ),(f) rfind( ),(g) index( ),
   (h) rindex(), (i) count( ),(j) replace( ),(k) split( ),(l) join( ), (m) upper( ),(n) lower( ),
   (o) swapcase( ),(p) title( ), (q) capitalize( ),(r) startswith() and (s) endswith()"""
#len() function
str = " Rafia "
print(f"String: {str}")
print(f"Length of the string: {len(str)}")
#strip() method
print(f"String after strip(): '{str.strip()}'")
#rstrip() method
print(f"String after rstrip(): '{str.rstrip()}'")
#lstrip() method
print(f"String after lstrip(): '{str.lstrip()}'")  
#find() method
print(f"Index of 'a': {str.find('a')}")
#rfind() method
print(f"Index of 'a' from the right: {str.rfind('a')}")
#index() method
print(f"Index of 'a': {str.index('a')}")
#rindex() method
print(f"Index of 'a' from the right: {str.rindex('a')}")
#count() method
print(f"Count of 'a' in the string: {str.count('a')}")
#replace() method
print(f"String after replace(): '{str.replace('R', 'a')}'")
#split() method
str1="Hello, World!"
print(f"String after split(): {str1.split(', ')}")
#join() method
str1 = ["Hello", "World"]
print(f"String after join(): '{', '.join(str1)}'")
#upper() method
print(f"String after upper(): '{str.upper()}'")
#lower() method 
print(f"String after lower(): '{str.lower()}'")
#swapcase() method
print(f"String after swapcase(): '{str.swapcase()}'")
#title() method
print(f"String after title(): '{str.title()}'")
#capitalize() method
str2 = "hello world!"
print(f"String after capitalize(): '{str2.capitalize()}'")
#startswith() method
print(f"Does the string start with 'R'? {str.startswith('R')}")
#endswith() method
print(f"Does the string end with 'a'? {str.endswith('a')}")
