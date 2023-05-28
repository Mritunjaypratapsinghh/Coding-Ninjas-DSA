# Pair sum in array
# Send Feedback
# You have been given an integer array/list(ARR) and a number 'num'. Find and return the total number of pairs in the array/list which sum to 'num'.
# Note:
# Given array/list can contain duplicate elements. 
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the first array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.

# Third line contains an integer 'num'.
# Output format :
# For each test case, print the total number of pairs present in the array/list.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^4
# 0 <= num <= 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 9
# 1 3 6 2 5 4 3 2 4
# 7
# Sample Output 1:
# 7
# Sample Input 2:
# 2
# 9
# 1 3 6 2 5 4 3 2 4
# 12
# 6
# 2 8 10 5 -2 5
# 10
# Sample Output 2:
# 0
# 2


#  Explanation for Input 2:
# Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.

# For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).






from sys import stdin
def getPairsCount(arr, n, sum):
 
    m = [0] * 100000
 
    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
 
    twice_count = 0
 
    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):
 
        twice_count += m[sum - arr[i]]
 
        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1
 
    # return the half of twice_count
    return int(twice_count / 2)
 





















#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(getPairsCount(arr, n, num))

    t -= 1
