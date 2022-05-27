#add 
def add(n1, n2): 
  return n1 + n2 

#substract 
def substract(n1, n2): 
  return n1 - n2 

#multiply 
def multiply(n1, n2): 
  return n1*n2

#divide 
def divide(n1,n2): 
  return n1/n2 

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide,
}

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for symbol in operations: 
  print(symbol)

choice = input("Please choose a symbol from the above: ")
calc = operations[choice]

answer = calc(num1, num2)
  


print(f"{num1} {choice} {num2} = {answer}")
