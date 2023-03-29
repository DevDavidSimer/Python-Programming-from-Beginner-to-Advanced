
# All variables are integers
x = 3
y = 4
z = 5

print(x)
print(y)
print(z)

#When we change the type of the variable 

x = str(3)
y = int(4)
z = float(5)

#x1 becomes a string 
#y1 remains an integer
#z1 becomes a float type number

print(x)
print(y)
print(z)

#Look how interesting it is when we sum these variables:

#x + x turns to 33 and this happens because it concatenates the string. Text (3) + text (3) = 33
#y + y is still an integer, so the sum is done normally.
#z + z is also treated as a number, but in this case it knows that it is working with fractional numbers, so the result has an extra 0.

print(x + x)
print(y + y)
print(z + z)
