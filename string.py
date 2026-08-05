name="Manujana"
print(name)
#man print
print(name[0:2])

#Need to print "Jana"
print(name)
#Jana print
print(name[:4])

#Need to print "Mnjn"
print(name[0:8:2])

#Need to print "Mun"
print(name[0:8:3])

fruit="Orange"
#I need to print first 3 characters( Ora )
#I need to print last  3 charcters( nge )
print(fruit[0:3])
print(fruit[3:6])

print(fruit[:-3])
print(fruit[-3:-1])

fruits=["Orange","Apple","Banana",1,2,3,True]
print(fruits)

print(fruits[1])
print(fruits[:3])
print(fruits[4:7])
print(fruits[3:6])

fruits[1]="Banana"
print(fruits)

fruits.insert(0,"Apple")
print(fruits)

fruits.insert(8,1000)
print(fruits)

#Append
fruits.append(False)
#print(fruits)

#Remove
#fruits.remove("Orange")
#print(fruits)

#fruits.remove("Apple")
#print(fruits)

#fruits.pop(2)
#print(fruits)

#del fruits[4]
print(fruits)

#fruits.clear()
print(fruits)

for x in fruits:
    print(x)

for x in fruits:
    print(x, end=",")

Name = "Rukman"
print(Name)

Name = Name.upper()
print(Name)


Name = Name.lower()
print(Name)


    