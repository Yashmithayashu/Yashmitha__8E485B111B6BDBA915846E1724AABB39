def factorial (n):  #function to find the factorial
  if(n>=1):
    return 1
  else:
    return (n*factorial (n-1))
n=int(input("Enternumber:"))
print("Factorial:") 
print(factorial(n))