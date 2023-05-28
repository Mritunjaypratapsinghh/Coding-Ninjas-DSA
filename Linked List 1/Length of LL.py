# Length of LL
# Send Feedback
# Given the head of a singly linked list of integers, find and return its length.
# Input format :
# The first and only line contains elements of the singly linked list separated by a single space. 
#  Remember/Consider :
# While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
# Output format :
# The output contains a single integer denoting the length of the linked list.
#  Constraints :
# 0 <= N <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 3 4 5 2 6 1 9 -1
# Sample Output 1 :
# 7


# Explanation of sample input 1 :
# The number of nodes in the given linked list is 7.
# Hence we return 7.


# Sample Input 2 :
# 10 76 39 -3 2 9 -23 9 -1
# Sample Output 2 :
# 8


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.next=None






def length(head) :
    slow=head
    count=0
    while slow:
        slow=slow.next
        count+=1
    return count











        




#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()



#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    print(length(head))

    t -= 1