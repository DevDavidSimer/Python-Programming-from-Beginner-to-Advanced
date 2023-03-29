
'''
How it will work:
This code will use 2 data entered by the user.

What data?
1st Data - Year of Birth
2nd Data - Current Year

Returning:
With these two pieces of information it will make a 
calculation and print on the screen the user's age.
'''

year_birth = int(input('What is your birth year ?'))
current_year = int(input('What year is it?'))
age = current_year - year_birth

print(' You are ' + str(age) + ' years old ')


'''
Explaining the code above:

    "int" was used in front of "input" of the variables so that python will read the data entered 
    by the user as an integer and not as a string. And it was added an internal variable with no 
    interaction with the user that will calculate these two previous variables and then this variable 
    "age" will be used in the print() where it will be changed to a string allowing python to make the 
    concatenation and print the result on the screen.

    Code executed successfully!


'''