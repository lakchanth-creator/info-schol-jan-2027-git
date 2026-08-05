num = 1

while (num<=10):
    print(num)
    num+=1

print("Loop finished")


for i  in range(1,5):
    print("*" * i)

for i in range(4,0,-1):
    print("*" * i)

    i = 4
while i>0:
    print("*" * i)
    i -= 1

end = 100
for num in range(1, end+1):
    print(num)

name = "john doe"

for char in name:
    print(char)

    stars = 1

while stars <= 7:
    print("*" * stars)
    stars += 2

height = 8

print(" " * (height - 1) + "*")

for i in range(1, height):
 spaces = " " * (height - i - 1)
 foliage = "*" * (2 * i + 1)
 print(spaces + foliage)

for _ in range(2):
 print(" " * (height - 1)+ "^")