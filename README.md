# What is Python?
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

# Variables in Python
* Variable doesn't start with numeric value
* id(a) will give the memory location of variable a
* if value of variable are same then id will be also same

# String in Python
* In string + work as concatination
* during concationation both side will be string


# Operators in Python
1. Arithmnetic Operator
   
   Operator        Name        Example
   +              Addition       x+y
   -              Substraction   x-y
   *            Multiplication   X*Y
   /            Division         x/y
   %            Modulus          x%y
   **           Exponents        x**y
   //           Floor division   x//y



2. Assignment Operator
   Operator      Example        Same AS
   =              x=5            x=5
   +=             x+=3          x=x+3
   -=            x-=3           x=x-3

3. Comparision Operators
   Operators     Name            Example
   ==           Equal            x==y
   !=           Not Equal        x!=y
   >           Greater Than      x>y
   <           Less than         x<y
   >=       Greater than or equal to  x>=y
   <=       Less than or equal to  x<=y

4. Logical Operators
    Operator      Description                           Example
    and  return true if both statements are true   x<5 and x<10
    or  returns true if one of the statements is true  x<5 or x<10
    not reverse the result, returns false if the result is true     not(x<5 and x<10)

5. Identity Operators
   Operators         Description                    Example
   is           Returns True if both variables are
                the same object                     x is y
   is not       Returns True if both variables
                are not the same objects     x is not y        

6. Membership Operators
   Operators        Description                   Example
   in           Returns True is a sequence       x in y
                with the specified value is
                present in the object
   not in       Returns true if a sequence       x not in y
                with the specified value is
                not present in the object    

7. Bitwise Operators
   Operators         Name                 Description
   &                  AND                 x & y
   |                  OR                  x | y
   ^                  XOR                 x ^ y


* print(bin(10)) :- it gives the binary value of 10   


# Data Types in Python
* Data Type list
   1. Numeric 
      (a) Integer
      (b) Float
      (c) Complex Number
   2. Sequence Type
      (a) String
      (b) List
      (c) Tuple  
   3. Dictionary
   4. Set

* Mutable and Immutable Data types
=> Mutable object can change its state or contents and immutable objects cannot.

1. Mutable Data Types:
    . List
    . Dictionary
    . byte array
2. Immutable Data Types:
    . Int
    . Float
    . Complex
    . String
    . tuple
    . Set

# String:- 
* A string is a collection of one or more characters put in a single quote, double-quote or triple quote.
* Multi-line strings can be denoted using triple quotes, '''or'''.
# type(a)   :- its gives the data types of a

# List:-
 * List is an ordered sequence of items.
 * it is one of the most used datatypes in python is very flexible
 * it is mutable(means changeable)

# List Comprehension Elegant way to create Lists
-> List comprehension is ann elegant way to define and create lists based on existing lists.
-> List comprehension is generally more compact and faster than normal functions and loops for creating list.

* Syntax of List Comprehension
[expression for item in list]
# tuple
 * Tuple is an ordered sequence of items same as a list.
 * it is defined within parentheses() where items are seperated by commas.

# Dictionary'
 * Dictionary is an unordered collection of key-value pairs.
 * In  python, dictionaries are defined within braces {} with each item being a pair in the form key: value

# Set
 * A set is an unordered collection of items.
 * Every set element is unique (no duplicates) and must be immutable( cannot be chnaged)
 * {}


# Python Conditional Statement
1. If Statement
   if[conditional expression]:
        [statement(s) to execute]
   * Example
   a=10
   if a%2==0:
     print(a,"is even number")

2. if else Statement
   if[conditional expression]:
        [statement(s) to execute]
   else:
        [alternate statement to execute]     
   * Example
   a=int(input("Enter the number:- "))
   if a%2==0:
      print(a,"is even number")
   else:
      print(a,"is odd number") 

2. if elif else Statement
   if[conditional expression]:
        [statement(s) to execute]
   elif[condition #2]:
      [statement #2]
   else:
        [alternate statement to execute]     
   * Example
   a=int(input("Enter the percentage:- "))
   if a>=60:
      print("1st division")
   elif a>=48:
      print("2nd Division)   
   else:
      print("Fail") 

# For Loop in python
 * Range
 1. range(5):- start=0;condition<5;increment=1
 2. range(1,5):- start=1;condition<5;increment=1
 3. range(1,5,2):- start=1;condition<5;increment=2


# String 
 * A string is a sequence of characters.
 * Strings can be created by enclosing characters inside a single quotes or double quotes
 * Triple quotes can be used represent multiline string

* String indexing start from 0 when we go from left to right where as string indexing start from -1 when we go from right to left
* len(w) = length of w
* text.strip()= remove the space of before  of after the string

# Python String Function
 1. lower():- convert all letter in lowercase
 2. upper():- convert all letters in uppercase 
 3. title():- convert first letter of all word in upercase
 4. capitalize():- convert first letter in uppercase
 5. find():- find the index of element(if element is not in variable it will give -1)
 6. index:- return index of element
 7. isaplha():- return true if string has only alphabets
 8. isdigits():- return true if string has only numeric
 9. isalnum():- return true if string has alphabets or number
 10. chr():- return aplabhets according to ASCII value of that element
 11. ord():- return numbers according to ASCII value of element

# Python String Format() method
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The Placeholder is defined using curly brackets:{} .
Read more about the placeholders in the Placeholder section below.

# List Fuction

* Function for Delete Elements from the List-
 1. del
 2. pop()
 3. remove()
 4. clear()

 * Function for Update Elements in the List
 5. insert()-> insert a element in list
 6. append() -> append a new element or list to the end
 7. extends() -> extends a new element at the end of list
 8. count() -> count the number of occurence of the element in the list
 9. max() -> return the maximum element of the list
 10. min() -> return the minimum element of the list
 11. sort() -> sort the list
 12. reverse() -> reverse the list
 13. index() -> return the index of the element
