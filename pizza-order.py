price = 0
avgprice = 83
import time

name = input("What is your name: ")
print("We offer 3 different sizes of pizza, 6 ince ,9 ince or 12 inch")

choice1 = input("Pizza size(inch): ")
if choice1 == "6":
    price += 20
elif choice1 == "9":
    price += 30
elif choice1 == "12":
    price += 40
else:
    price += 20

time.sleep(0.5)
print()
choice2 = input("Do you want a thicker crust? That will be charged $5 extra!\n If yes,please input yes: ")
if choice2 == "yes":
    choice2b = "thick"
    price += 5
else:
    choice2b = "thin"
    price += 0

print()
m,p,c,t = 0,0,0,0

time.sleep(0.5)

print("What ingredients do you want? Ingredients available: mushroom $15, peproni $20, chicken $25, tomato $8")
choice3 = input("Input format: 'm' for mushroom , 'p' for peproni, 'c' for chicken, 't' for tomato: ")

active = True
while True:
    c3 = input(choice3)
    if c3 == "m":
        price += 15
        print("Mushroom added! Anything more?")
    elif c3 == "p":
        price += 20
        print("Peproni added! Anything more?")
    elif c3 == "c":
        price += 25
        print("Chicken added! Anything more?")
    elif c3 == "t":
        price += 8
        print("Tomato added! Anything more?")
        break
    active = False   

print(f"The total cost is: {price}")
print("Order received! Your pizza is being prepared!")
