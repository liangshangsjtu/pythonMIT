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
