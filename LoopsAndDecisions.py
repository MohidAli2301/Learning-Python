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

