number_list=[]
for i in range(5):
    numbers=int(input("Enter numbers:"))
    number_list.append(numbers)
print(f"The first number is {number_list[0]}")
print(f"The last number is {number_list[-1]}")
print(f"The smallest number is {min(number_list)}")
print(f"The largest number is {max(number_list)}")
print(f"The average of the numbers is {sum(number_list)/len(number_list)}")
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username=input("Enter your username:")
if username in usernames:
    print("Access accepted")
else:
    print("Access denied")
