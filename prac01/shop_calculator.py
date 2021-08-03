number_of_items=int(input("Enter number of item:"))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items=int(input("Enter number of item:"))
#end of while loop
total_price1=0
for i in range(number_of_items):
    price_of_item = float(input("Enter price of item:$"))
    total_price1 +=price_of_item
#end of for loop
if total_price1 > 100:
    total_price=total_price1-(total_price1*0.1)
    print(f"Total price for {number_of_items} is ${total_price:.2f}")
else:
    print(f"Total price for {number_of_items} is ${total_price1:.2f}")


