"""
FROM WEEK1 PROBLEM SET 1 PROBLEM 2
"""
"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
"""
HOW TO GET ACCESS TO THE LATTER 2 CHARS AFTER THE SPECIFIC CHAR c ? it's a good idea to create another variable i as a indexer.
"""
"""
BELOW ARE ONE SOLUTION FOR THE PROBLEM
"""
num=0
i=0
for c in s:
    i +=1
    if c=='b' and i<=len(s)-2:
        if s[i]=='o' and s[i+1]=='b':
            num += 1
print('Number of times bob occurs is: '+str(num))

"""
GUESS-AND-CHECK IDEA TI FIND THE SQUARE ROOT OF AN INTEGER
"""
ans=0
neg_flag=False
x=int(input("Enter an interge here: ")) 
if x<0:
    neg_flag = True
while ans ** 2 <x:
    ans += 1
if ans ** 2 = x:
    print("square root of",x,"is",ans)
else:
    print(x,"is not a perfect square")
    if neg_flag:
        print("Just checking...did you mean",-x,"?")
        
 """
 UPGRADE: FIND THE CUBE ROOT OF ANY NUMBER
 """
cube=27
epsilon=0.01
guess=0.0
increment=0.001
num_guesses=0
while abs(guess**3-cube）>=epsilon:
          guess += increment
          num_guesses += 1
 print("Number of guesses:",num_guesses)
 if abs(guess**3-cube）>=epsilon:
        print('failed on cube root of',cube)
 else:
        print(guess,'is close to the cube root of',cube)
        
# BISECTION SEARCH FOR SQUARE ROOT
x=25
epsilon=0.01
numGuesses=0
low=0.0
high=x
ans=(high+low)/2.0

while abs(ans**2-x) >= epsilon:
        print 'low=',low,'high=',high,'ans=',ans
        numGuesses +=1
        if ans**2<x:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0
print 'numGuesses=',numGuesses
print ans,"is close to the square root of",x
       
