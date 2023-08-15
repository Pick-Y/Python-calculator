# Python-calculator

#Description

This is a simple calculator in python
It include the ability to add,subtract, divide and multiply numbers

At moment the program as the ability to only process two number


#Run
From the main file, on vscode, click the run button

#Challenges
- sorting the array
While considering how to approach this task, I was faced with the problem of how to identify the operation sign in the array input received from the user and 
how to split the content so that I would gengerate an array con only the numbers.

To solve the problem, I created a double loop to check every single character in the array. Then I used the split("+") - for example - function to return an array that contained
only the individual numbers. However, the numbers were of the string type. So, I used the Int() method to convert those values into int values.

- subtracting numbers
Abother challenge that I face was that in the subtraction function, while going thorough the loop and subtracting the numbers, the program was printing negative numbers. The solution that I found was to create to variables, num1 and num2, and, in the first loop assigning the value to num1 if it was empty or assignining the value to num2 if itwas not empty. Then i subtracted the numbers from each other.

