#loops are used to repeat a block of code
#for loops
kilifi = ('magarini','shakahola','madunguni','mlunguni')

for constituencies in kilifi:
    print('no power for: ',constituencies)
   # print(constituencies)


   #for loops using range
    welcome_message = "welcome to plp"
for i in range(6):
    print(welcome_message)


    #The break statement
    #With the break statement we can stop the loop before it has looped through all the items
    fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  #Exit the loop when x is "banana"

 # Exit the loop when x is "banana"but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


  #THE WHILE LOOP
  #With the WHILE loop we can execute a set of statements as long as a condition is true.
  i = 1
while i < 5:
  print(i)
  i += 1

  #THE BREAK STATEMENT
 # With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3: #Exit the loop when i is 3:
    break
  i += 1

 # The continue Statement
#With the continue statement we can stop the current iteration, and continue with the next
#Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 4:
    continue
  print(i)
