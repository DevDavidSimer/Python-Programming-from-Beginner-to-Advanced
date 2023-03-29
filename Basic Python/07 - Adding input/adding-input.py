
# Now I will use input.

# I'm going to ask the user to enter data and after he enters this data 
# I'm going to use print() to display this information on the screen.


name = input("What's your name ?")
age = input(str('How old are you ?'))
city = input('where do you live?')


print(name + ' is ' + age + ' years old and lives in ' + city)


'''
When I add the input the user tells me this data, and in order not to have an execution 
failure when printing on the screen I needed to tell python that the data informed for the 
variable age needs to be read as a string.

The code was executed successfully!
'''