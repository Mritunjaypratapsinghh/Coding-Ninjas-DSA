# Pair Star
# Send Feedback
# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
# Input format :
# String S
# Output format :
# Modified string
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a



def pairstar(s):
    if len(s)<=1:
        return s
    
    if s[0]==s[1]:
        return s[0]+"*"+pairstar(s[1:])
    else:
        return s[0] + pairstar(s[1:])
    
    #return pairstar(s[1:])


    # if n==1:
    #     return s
    
    # if s[0]==s[1]:
    #     smalloutput= s[0]+"*" 
    # str=pairstar(s[1:])
    # return str+smalloutput
    # return smalloutput+ pairstar(s[1:])
s=input().strip()
n=len(s)
print(pairstar(s))