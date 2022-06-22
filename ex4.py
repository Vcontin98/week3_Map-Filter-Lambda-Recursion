def fibonacci(n):
  if n<2:
    return n
  else:
    return (fibonacci(n-1)+fibonacci(n-2)) #this is recursive because the function is calling it self!

#catching exception that are not int
try:
  size = int(input('please input a positive integer: '))
except ValueError:
  print ('Invalid Input')

# check if the number of terms is valid

if size <= 0:
  print("Plese enter a positive integer")
else:
  print("Fibonacci sequence:")
  for i in range(size): #telling the computer to do a certain action X amount of time according to the value store in size AKA Iteration
    print(fibonacci(i))