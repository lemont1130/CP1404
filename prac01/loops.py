for i in range(1,21,2):
    print(i,end=" ")
for i in range(0,101,10):
    print(i,end=" ")
for i in range(20,0,-1):
    print(i,end=" ")
number_of_stars = int(input("Number of stars:"))
for i in range(number_of_stars):
    print("*",end="")
number_of_line = int(input("Number of line:"))
for i in range(number_of_line):
    print("*"*(i+1))
