"""lab2"""
myList = ["Argentina", "Portugal", "England", "Kazakhstan", "France", "Russia", "China"]
print(myList[0])
print(myList[6])
myList.clear()
print(myList)
print(len(myList))
print("Hello World !")
myList.insert(0, "Poland")
print(myList)
myList.append("Brazil")
print(myList)
myList.reverse()
print(myList)
print(myList.pop(0))
print(myList)
i = 0
for i in range(len(myList)):
    if myList[0] == "Poland":
        myList.append("Germany")
        myList.append("Norway")
        myList.append("America")
        print(myList)
myTuple = ("Circle","Circle", "Square", "Rectangle", "Sphere", "Pyramid", "Cylinder")
print(myTuple.count("Circle"))
print(myTuple)
print(type(myTuple))
print(myTuple[5])
print(myTuple[2:7])
print(myTuple[:4])
y = list(myTuple)
y.append("Shape")
print(y)
y.remove("Pyramid")
print(y)
x = ("Red", "green", "yellow")
k = ("purple", "dark", "blue")
g = x + k
print(g)
for i in range(len(g)):
    print(g[i])
    i = i + 1
mySet = {1, 2, 7, 89, 45, 6}
mySet.remove(89)
print(mySet)
mySet.pop()
print(mySet)
mySet1 = {}
print(mySet1)
mySet1 = mySet.copy()
print(mySet1)
mySet1.add(23)
print(mySet1)
thisD = {"car" : "dodge challenger", "nation" : "Kazakh", "University" : "KBTU"}
print(thisD)
print(thisD["car"])
print(thisD.pop("car"))
print(thisD)
print(thisD.update({"car" : "mustang"}))
print(thisD)

print(123)
if "car" in thisD:
    thisD.update({"car" : "BMW"})
    print(thisD)
print(len(thisD))
print(type(thisD))
y = thisD.get("University")
print("I study in - " + y)
print(y)
x = thisD.values()
print(x)
k = thisD.items()
print(k)
keys = thisD.keys()
print(keys)
thisD.update({"hobby" : "volleyball"})
print(thisD)
thisD["hobby"] = "video games"
print(thisD)

for i in thisD:
    print(i + "-" + thisD[i])
lisT = thisD.copy()
print(lisT)
print(thisD.setdefault("car"))
print(thisD["car"])
import random
number = random.randint(1,100)
if number in range(1,60):
    print("This number is between 1 and 100")
else:
    print("This is not between 1 and 100")
import math
if math.sqrt(4512) > 45:
    print("It works")
else:
    print("This is otherwise case")

if 9 > 9: print("Yes")
elif 9 == 9: print("elif")
else: print("error")

print("Hello") if math.sqrt(1024) == 32 else print("Bye!")

newList = []
j = 0
while j < 5:
    y = float(input("Insert number:"))
    j += 1
    newList.append(y)
print(newList)
i = 0
for i in range(len(newList)):
    print(newList[i])