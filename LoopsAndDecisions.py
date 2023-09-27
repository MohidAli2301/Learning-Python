#Conditional Statements
#Note: Conditional statements check for boolean values: True and False. Giving statements that would run if true, followed by else do this when false.
if (True):
  print ("This works!")
else:
  print("This doesn't work :(")
  
#Lets make a more advanced one
change = 1 #Change the value to test the cases!
if (change==1):
  print("You should change the value")
elif (change==2):
  print("You Changed the Value!")
else:
  print("Try using 1 or 2")

#Nested If's are also a thing
real=True
notReal=False
if (real): #Change the variable to test the cases!
  print("when first is true say this")
  if (notReal): #Change the variable to test the cases!
    print("when second true say this")
  else:
    print("When second false say this")
else:
  print("say this when first is false")
#-----------------------------------------------------------------------------------------#
#Loops with for and while
for count in range (10,-1,-1): #Start at 10, count till -1, decrease by 1
  print (count)
for x in range (1,6): #Start at 1, until 6, default increment == 1
     print (x)
#Note: works in non-inclusive actions, if you want to count from 1-5 you must use 1,6

#While loops are very simple, as they only run if a condition is true
yes = True
while(yes):
  for x in range (1,6): #Start at 1, until 6, default increment == 1
    print ("Hehe", x)
  yes = False #-- comment this line to test infinite loop!
#-----------------------------------------------------------------------------------------#
#With both conditional statements and looping operators, we can implement and, or, as well as not
yes = True
no = False
if not(no):
  print("If invert no is equal True then this will work")
  while (yes and yes):
    print ("If BOTH are True this will work")
    if yes or no == False:
      print ("If EITHER is FALSE, then this will work")
      yes = False
      no = True

