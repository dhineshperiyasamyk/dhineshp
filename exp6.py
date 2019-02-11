yr=int(input())
if (yr % 4) == 0:
   if (yr % 100) == 0:
       if (yr % 400) == 0:
           print("yes".format(yr))
       else:
           print("no".format(yr))
   else:
       print("yes".format(yr))
else:
   print("no".format(yr))
