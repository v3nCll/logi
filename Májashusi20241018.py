bool
str
int
float
dictionary
list
tuple

myStr = "hello World"
for i in myStr:
    print(i, end=" ")
print("\n")

myList = [("apple", "orange", "pear", "kiwi")]
for i in myList:
    print(i, end=" ")
print("\n")

myMatrix = [[2, 5, 9], []]
for i in myMatrix:
    for j in i:
        print(j, end=" ")
    print("\n", end=" ")
print("\n", end=" ")

for i in myTuple:
    print(i, end=" ")
print("\n")

for i in myDict.keys():
    print(i, ": ", myDict[i], sep=" ")




List = [3, 9]
List = str(List)
print(List)
print(type(List))
for i in List:
    print(i)


#First task
x = input("adj meg egy számot: \n")
x = float(x)
print(type(x))
y = str(-2* x**4+3* x**3+2* x**2-7* x+4)
print(y)


#Second task
sec = input("sec: ")
