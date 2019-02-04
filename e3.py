b=['a','e','i','o','u']
a=raw_input()
if a in b:
    print ("Vowel")
elif(a.isalpha()):
    print("Consonant")
else:
        print("Invalid")
