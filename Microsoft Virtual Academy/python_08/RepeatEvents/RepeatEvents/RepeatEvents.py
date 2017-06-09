import turtle

nbrsides = 20
for weirdname in range(nbrsides):
    turtle.forward(30)
    turtle.right(175 / nbrsides)
    for steps in range(nbrsides):
        turtle.color('red')
        turtle.forward(15)
        turtle.right(360 / nbrsides)

# for steps in range(1,18) :
#     print(steps)

# for steps in range(1,20,2) :
#    print(steps)

# for steps in [1,5,7,8,9,11,45,47,45] :
#    print(steps)

# for colour in ['red','green','blue','black'] :
#    turtle.color(colour)
#    turtle.forward(100)
#    turtle.left(90)

# for index in range(2):
#    print("Hello")
# print("World")
