# Check Palindrome (recursive)
# Send Feedback
# Check whether a given String S is a palindrome using recursion. Return true or false.
# Input Format :
# String S
# Output Format :
# 'true' or 'false'
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# racecar
# Sample Output 1:
# true
# Sample Input 2 :
# ninja
# Sample Output 2:
# false

## Read input as specified in the question.
## Print output as specified in the question.
def is_palindrome(s):
    if len(s) <= 1:
        return "true"
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return "false"
a=input().strip()
print(is_palindrome(a))


