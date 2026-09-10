#Transpose Matrix
r,c=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(r)]
for j in range(c):
   for i in range(r):
       print(a[i][j],end=" ")
   print()
5. Stack Using List
stack=[]
stack.append(10)
stack.append(20)
print(stack)
print("Pop:",stack.pop())
print(stack)
Linked List Insertion
class Node:
   def __init__(self,data):
       self.data=data
       self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
temp=head
while temp:
   print(temp.data,end=" ")
   temp=temp.next