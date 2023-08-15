from assignOperation import *



#sum

def identifyOperation(n):
    numToSum = n
    result = 0

    for i in numToSum:
        for l in range(0,len(i)):
            if i[l] == "+":
                result = sum(i)
                break
            elif i[l] == "*":
                result = multiply(i)
                break
            elif i[l] == "-":
                result = subtraction(i)
                print("ciaone")
                break
            #elif i[l] == "*":
             #   operationSign = i[l]
                
           # else:
              #  print("ciaone")
    return result
        
         


  
   

                
           


    