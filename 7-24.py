# CONVERT DECIMAL INTEGER TO BINARY
if num <0:
  isNeg = True
  num = abs(num)
else:
  isNeg = False
result = ' '
if num == 0:
  result = '0'
while num > 0:
  result = str(num%2) + result
  num=num//2
if isNeg:
  result = '-'+result
  
# CONVERT DECIMAL FRACTION TO BINARY
x=float(input("Enter a decimal number between 0 and 1: "))
p=0
#FIRST, I NEED TO COVERT THE FRACTION INTO A WHOLE NUMBER BY MULTIPLY THE POWERS OF 2

while((2**p)*x)%1 !=0:
  print('Remainder= '+str((2**p)*x-int((2**p)*x)))
  p +=1
num = int((2**p)*x)
# SO THE FRACTION CONVERTED TO AN INT NOW
"""
NOTE THAT YOU CANNOT ALWAYS FIND A PERFECT CORRESPOND P FOR ANY FRACTION TO MAKE (2**p)*x AN INTEGER, SO IN THESE CASES YOU NEED TO MAKE APPROXIMATION
"""

result=''
if num ==0:
  result = '0'
while num >0:
  result = str(num%2)+result
  num = num//2
# NOW CONVERT THE INTERGE INTO BINARY
  
for i in range(p-len(result)):
  result='0'+result
result = result[0:-p]+'.'+result[-p:]
# DEVIDED P POWERS OF 2 BY MOVING THE POINT IN BINARY FORM

print('The bonary presentation of the demical '+str(x)+' is: '+str(result))
