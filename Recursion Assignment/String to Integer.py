# String to Integer
# Send Feedback
# Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
# Input format :
# Numeric string S (string, Eg. "1234")
# Output format :
# Corresponding integer N (int, Eg. 1234)
# Constraints :
# 0 < |S| <= 9
# where |S| represents length of string S.
# Sample Input 1 :
# 00001231
# Sample Output 1 :
# 1231
# Sample Input 2 :
# 12567
# Sample Output 2 :
# 12567


def convert(str):
    n=len(str)
    if n==0:
        return 0
    if n==1:
        return ord(str[0])-ord('0')
    y=convert(str[1:])
    x=ord(str[0])-ord('0')
    x = x * (10**(len(str)-1))+y
    return int(x)
str=input('')
print(convert(str))