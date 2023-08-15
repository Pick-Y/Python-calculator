from calculations import *

#Using the input method, the program asks the user to insert the operation he wants to calculate. The input then is stored
#as a string into an array. The array will include the operation sign, example "+", that will later be used to identify the
#type of operation
number = [input("Insert the operation you wish to calculate: ")]

#number is then passed to identifyOperation() to execute the calculation
# and the result will be printed.
result = identifyOperation(number)
print(result)
