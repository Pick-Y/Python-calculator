from assignOperation import *




def identifyOperation(n):
    numToSum = n
    result = 0

#first loop to loop what is contained in the number array.
#as the input is stored as a string array, it will contain a characters such, for example "3+4"
    for i in numToSum:
#second loop to check each single character and check wich opearation sign is present in the array, for example "+"

        for l in range(0,len(i)):
#Based on wich operation sign we find, we assign the result variable the result of the relevant operation
            if i[l] == "+":
                result = sum(i)
                break
            elif i[l] == "*":
                result = multiply(i)
                break
            elif i[l] == "-":
                result = subtraction(i)
         
                break
            elif i[l] == "/":
                print("ciaone")
                result = division(i)
                
                break
# we return the result to the main fucnction
    
    return result
        
         


  
   

                
           


    