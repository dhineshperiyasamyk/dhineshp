j = int(input())

count = 0



for i in range(2, (j//2 + 1)):

    if(j % i == 0):

        count = count + 1

        break



if (count == 0 and j != 1):

    print("yes")

else:

    print("no")
