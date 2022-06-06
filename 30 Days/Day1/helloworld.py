# Exercise: Level 1

# Open the python interactive shell and do the following operations. The operands are 3 and 4.
print (3+4)         #addition
print (3-4)         #subtraction
print (3*4)         #multiplication
print (3%4)          #mudulus
print (3/4)         #division
print (3**4)        #exponential
print (3//4)        #floor divison operation


# Write strings on the python interactive shell. The strings are the following:
print ("Your name")
print ("Your family name")
print ("Your country")
print ("I am enjoying 30 days of python")


#Check the data types of the following data:
print (type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print (type(['Asabeneh', 'Python', 'Finland']))
print(type("your name"))
print(type("your family name"))


#Write an example for different Python data types such as Number
#(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

#numbers
print (5)           #integer
print (22.1)        #float
print (2j)          #complex number

#string
print ("i like python")

#boolean
print (4>6)
print (1<4)

#list
print (["banana", 10, 6j, 3.142])

#dictionary
info = {
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
print (info)