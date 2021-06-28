list = []

a = int(input("Please put in an integer: "))
try:
    a == int
except:
    raise ValueError

    
for i in a:
    if i =="2": #if we wanna count how many two's there are in an integer
        list.append(i)
print(len(list))
