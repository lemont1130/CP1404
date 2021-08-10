import random
constants=[]
picks=int(input("How many quick picks?"))
for line in range (picks):
    for i in range(6):
        print(random.randint(1,46),end=" ")
        constants.append(i)
    print(line,end="\n")


