import sys

def example():
  print('def example')
example()

def simple_addition(num1,num2):
  answer = num1 + num2
  print('num1=',num1)
  print('answer=',answer)
simple_addition(1,2)

print('sys.version=',sys.version)

print("hi\ndog")
print("hi" + \
      "\n" + 
      "cat")

x = 12
if x == 1:
  print('x is 1')
else:
  print('x ???')

if x == 1:
  print('* x is 1')
elif x == 12:
  print('* x is 12') 
else:
 print('* x is ???')

el = [1,2,3,4,5]
for n in el:
 print(n)
  
 print('each n')

for x in range(1,11):
  print(x)

