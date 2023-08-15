from  convertToInt import *


def sum(n):
    
        newNum = n.split('+')
        listToSum = convertToInt(newNum)
        total=0

        for num in listToSum:
            total += num
        
        return total



def multiply(n):
        
    
        newNum = n.split('*')
        listToMultiply = convertToInt(newNum)
        #The value of total is 1(not 0 as 0 multiplied with anything returns zero).
        total=1

        for num in listToMultiply:
             total = total * num
        
        return total

def subtraction(n):
    
        newNum = n.split('-')
        listToSubtract = convertToInt(newNum)
        print(listToSubtract)
        total=0

        for num in listToSubtract:

            total -= num
        
        return total

def division(n):
    
        newNum = n.split('/')
        listToSubtract = convertToInt(newNum)
        print(listToSubtract)
        total=0

        for num in listToSubtract:

            total = total / num
        
        return total