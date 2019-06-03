a=int(input())

b=0

m=a

while (a>0):

	d=a%10

	b=b+(d**3)

	a=a//10

if (b==m):

	print ("yes")

else:

	print ("no")
