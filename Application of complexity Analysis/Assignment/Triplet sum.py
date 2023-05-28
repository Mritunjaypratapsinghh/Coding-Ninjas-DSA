# Triplet sum
# Send Feedback
# You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.
# Note :
# Given array/list can contain duplicate elements.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the first array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.

# Third line contains an integer 'X'.
# Output format :
# For each test case, print the total number of triplets present in the array/list.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^3
# 0 <= X <= 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7 
# 12
# Sample Output 1:
# 5
# Sample Input 2:
# 2
# 7
# 1 2 3 4 5 6 7 
# 19
# 9
# 2 -5 8 -6 0 5 10 11 -3
# 10
# Sample Output 2:
# 0
# 5


#  Explanation for Input 2:
# Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.

# For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)


from sys import stdin
def tripletSum(arr,n, X):
    count = 0
    n = len(arr)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == X:
                    count += 1
    return count


# Function to find the number of triplets in the array whose sum is equal to 'num'
def tripletSum(arr,n,sum):
    arr.sort() # Sorting the array in non-decreasing order
    trip_count=0 # Initializing the count of triplets to zero
    for i in range(n):
        pair_sum=sum-arr[i] # Finding the sum of pairs required to form the triplet
        pair_count=pairSum(arr,i+1,n-1,pair_sum) # Finding the number of pairs whose sum is equal to 'pair_sum'
        trip_count+=pair_count # Adding the count of pairs to the count of triplets
       
    return trip_count # Returning the count of triplets


# Function to find the number of pairs in the array whose sum is equal to 'pair_sum'
def pairSum(arr,s,e,pair_sum):
    pair_count=0 # Initializing the count of pairs to zero
    while s<e:
        if(arr[s]+arr[e]<pair_sum): # If the sum of pair is less than the required sum, then we need to increase the sum
            s=s+1
        elif(arr[s]+arr[e]>pair_sum): # If the sum of pair is greater than the required sum, then we need to decrease the sum
            e=e-1
        else: # If the sum of pair is equal to the required sum, then we need to count the number of such pairs
            if(arr[s]==arr[e]): # If the elements at both the ends are equal, then we need to calculate the total number of pairs possible
                total_ele=(e-s)+1
                pair_count=pair_count+(total_ele*(total_ele-1)//2)
               
                return pair_count # Returning the count of pairs
           
            temp_s=s+1
            temp_e=e-1
            while((temp_s<=temp_e) and (arr[temp_s] == arr[s])): # Skipping the duplicates from the left
                temp_s+=1
               
            while((temp_e>=temp_s) and (arr[temp_e] == arr[e])): # Skipping the duplicates from the right
                temp_e-=1
               
            total_start=temp_s-s # Counting the number of elements between 's' and 'temp_s'
            total_end=e-temp_e # Counting the number of elements between 'e' and 'temp_e'
            pair_count=pair_count+(total_start*total_end) # Counting the number of pairs possible with the current values of 's' and 'e'
            s=temp_s # Updating the value of 's'
            e=temp_e # Updating the value of 'e'
           
    return pair_count # Returning the count of pairs


























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
    print(tripletSum(arr, n, num))

    t -= 1
