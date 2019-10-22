mytup = ("Ferrari", "Lamborghini", "Alfa Romeo")
print(mytup)
for x in mytup: #iterating using for loops 
    print(x)

myit = iter(mytup) #iterating using the iter() function 

print(next(myit))
print(next(myit))
print(next(myit))

mylist = ["BMW", "Mercedes", "Audi"]
print(mylist)
mylist[1] = "Volkswagen"
print(mylist)

for x in mylist:
    print(x)
if "Audi" in mylist:
    print("you have bad taste in cars")
else:
    print("why not try something Swedish")
print(len(mylist))

mylist.append("Mercedes")
print(mylist)

print(mylist[0:2])
