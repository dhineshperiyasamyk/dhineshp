y = int(input())

b = y

c = 0

 

while b != 0:

	c = (c * 10) + (b % 10)

	b = b // 10

 

if y == c:

	print("yes")

else:

	print("no")
