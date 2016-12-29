#   +   Addition            5+2=7 
#   -   Subtraction         5-2=3
#   *   Multiplication      5*2=10
#   /   Division            5/2=2.5
#   **  Exponent            5**2=25
#   %   Modulo              5%2=1

#print("I have %d cats" %6)
#print("I have %3d cats" %6)
#print("I have %03d cats" %6)
#print("I have %f cats" %6)
#print("I have %0.2f cats" %6)

#print("I have {0:d} cats".format(6))
#print("I have {0:3d} cats".format(6))
#print("I have {0:03d} cats".format(6))
#print("I have {0:f} cats".format(6))
#print("I have {0:.2f} cats".format(6))


area = 0
height = 10
width = 20

#Calculate the area of a triangule
area = width * height / 2
#print(area)
print("The area of the triangule would be %d" %area)
#Printing formatted float value with 2 decimal places
print("The area of the triangule would be %0.2f " %area)

#Printing the formatted decimal number with right justified to take up 6 spaces
print("My favorite number is %6d !" % 42)
#Printing the formatted decimal number with right justified to take up 6 spaces
#with leading zeros
print("My favorite number is %06d !" % 42)


#Do the same thing with the .format syntax to include numbers our output
print("the area of the triangle would be {0:f} ".format(area))
print("my favorite number is {0:d} ".format(42))



#This is an example with multiple numbers
#I have used the \ to indicate command continues on next line
print("Here are three numbers! " + \
        "The first is {0:d} The second is {1:d} and {2:d}".format(7,8,9))