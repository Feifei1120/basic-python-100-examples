list = []

a = int(input("Please put in an integer: "))
try:
    a == int
except:
    raise ValueError
    
for i in a:
    if i =="2":
        list.append(i)
print(len(list))
