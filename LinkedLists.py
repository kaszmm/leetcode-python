
from ast import Delete, List
from collections import deque
from dbm import ndbm
from functools import cache
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


#1  Copy List with Random Pointer
# O(n) : Time ans Space COmplexity : O(n)
# Approach is we store our original node in dictionary as key, and corresponding to that lkey we store our new generated node as values  in one loop
#after that we loop again in original link list and get fetch out the stored nodes from dcitionary, if the key doesnt exist we defautl get NONE(null)
#we just return our new list at end
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    #Do app all nodes in hashmap first then loop again head again and this time fetch nodes from hashmaps
    if head==None:
        return None
    nodeMap={}
    cur=head
    while cur!=None:
        newNode=Node(cur.val)
        nodeMap[cur]=newNode
        cur=cur.next
            
    dummy=Node(0)
    tail=dummy
    cur=head
    while cur!=None:
        deepNode=nodeMap.get(cur,None)
        deepNode.next=nodeMap.get(cur.next,None)
        deepNode.random=nodeMap.get(cur.random,None)
        tail.next=deepNode
        tail=tail.next
        cur=cur.next
    return dummy.next

#Minor Optimisation using single O(n) loop instead of two wiht O(n) Space Complexity
def OthcopyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        nodeMap={}
        dummy=Node(0)
        tail=dummy
        cur=head
        while cur!=None:
            deepNode = nodeMap.get(cur,Node(cur.val))
            nodeMap[cur]=deepNode
            if cur.next!=None:
                deepNode.next= nodeMap.get(cur.next,Node(cur.next.val))
                nodeMap[cur.next]=deepNode.next
            if cur.random!=None:
                deepNode.random = nodeMap.get(cur.random,Node(cur.random.val))
                nodeMap[cur.random]=deepNode.random
            tail.next=deepNode
            tail=tail.next
            cur=cur.next
        return dummy.next

#Most Optimisation using O(n) time and O(1) space if dont consider the head link list space itself
#the code runs for three loops, in first loop we add our new nodes in between existing nodes in head like A->A'->B->B'
#In second loop we register all the random pointer for our new nodes 
#In third loop we connect all the newNode and return head.next cause our new linked list starts from head.next
def OptcopyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        temp=head

        while temp!=None:
            cur=temp.next
            newNode=Node(temp.val)
            temp.next=newNode
            newNode.next=cur
            temp=cur
          
        cur=head
        copy=cur.next
        while cur!=None and cur.next!=None:
            if cur.random!=None:
                copy.random=cur.random.next
            cur=cur.next.next
            if cur !=None:
                copy=copy.next.next
                
        cur=head.next.next
        copy=head.next
        while cur!=None and cur.next!=None:
            copy.next=cur.next
            cur=cur.next.next
            copy=copy.next
        return head.next




#2 Add two numbers
#Key thing to rememebr is both lkist are in reverse order , so just start adding both digits from l1 and l2 and keep track of carry
#after exiting while loop check if carry is 1 if it is add that also in our result and retunr result list
def addTwoNumbers(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
        dummy = Node(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = Node(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


#3  Find Duplicate NUmber  (this question is hard cause you cant MODIFY array(cant use sorting) and you need to come up wiht O(1) space complexity(cant use set or dict))
#Approach: Used Floyd's Tortoise and hare algo
#Time Complexity: O(n)
#Space Complexity: O(1)
#Intuition:
#Yes this question is linkned list question why? cause first using array in form of linked list we first find cycle in this list 
# and once we find cycle we then use floyd tortoise and hare algorithm to find the repeated item that starts the cycle in list
#Things to know: the repeated element in list will be entry point of our cycle
#Our node 0 will be never be included in cycle,cause our input will consist of element range [1..n] so no node will point to 0 at all so 0 will never be in cycle
#USe fast and slow pointer method we first find node at which our fast and slow intersected
#Once thye intersected we take new slow pointer that starts from start and we then move slow and slow2 siultaneously once they noth intersect 
#we know that the node at whihc both intersected is node that is entry point of our cycle , whihc is also repeated element in our array
def findDuplicate(nums) -> int:
        slow=nums[0]
        fast=nums[nums[0]]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]
        
        slow2=0
        while fast!=slow:
            slow2=nums[slow2]
            slow=nums[slow]
        return slow

#Approach : Using Binary Search
#Time Complexity: O(n log(n))
#Space Complexity: O(1)
#Intuition:
#In order to understand how this solution work there feew things to observe
#1)In list of [1..n] distinct numbers the count of each number which are less than or equal to current number will be equal to number itself,like [1,2,3,4,5]
#in this array the count for 1 is 1 ,2 is 2(1,2), 3 is 3(1,2,3)...  count[1:1,2:2,3:3,4:4,5:5]
#2)COnsidering point 1) if there are any duplicate numbers present in our array the count of dupkicate number will be greater than the number itself ie
#so let's take another example like [3,4,2,5,2,1] for understanding this example we will sort and then observe some thing in it
#so our example afetr sort is [1,2,2,3,4,5] now when we take the count of this array where the numbers are less than or equal to number itself we found
#count [1:1,2:3,3:4,4:5,5:6], you can see than from number 2 inwards all the numbers after it satrted having count greater to number themself so in
#order to found out which number is duplicate we juts need to find minimum number that have count greater than number itself and that number will be our duplicate

#Algorithm:
#Things to keep note of
#1) We take left and right pointer not as index but as values itself, so left start wiht 1 and not wiht 0 and our right will be len(arr) not len(arr)-1
#2)We dont need to sort array in order to find count for current value, we just get mid and then we iterate over arr and check how many number is less than or equal to mid val
#3)When we encounter that count is greater than midVal measn that we may or may not found the duplicate so update our duplicate val for that cur val
#and narrrow our range from 1..n to 1..mid-1 , why? cause our aim is find min val that have cout=nt greaer than or equal to itself
#4)If our mid count is not greater than mid itself than we need to increment our values in range so we shift l=mid+1 .. right=n
def OthfindDuplicate(nums) -> int:
        left=1
        right=len(nums)
        duplicate=0
        while(left<=right):
            midVal= (left+right)//2
            count=0
            for num in nums:
                if midVal>=num:
                    count+=1
            
            if count>midVal:
                duplicate=midVal
                right=midVal-1
            else:
                left=midVal+1
        return duplicate


#Approach : Negative Marking [But this solution modifies our array so it can tbe used]
#Time Complexity: O(n)
#Space Complexity: O(1)
#Intuition:
#Things to Remember
#1) our input array will have element from [1..n] so we nevert encounter 0 value in it
#2)Our length of arr is n+1 so we never get out of bound errors in it
#3)here we get value from array and we treat that values as index and use that index to make the value at that index negative
#ie if arr=[3,2,2,4] then first we take 3 as index and make nums[3] negative arr=[3,2,2,-4] now make nums[2] -ve arr[3,2,-2,4] , noe again 2 came so make 2 index -ve 
#but here we see that number at index 2 is already negative so our duplicate is index=2 so return index
#So basically what we ieterate over array and what ever value we have in array we make that vlaue'index negative
#Doing that when making any value's index negative we check if that value is already negative, if it is means the current vlaue is duplicate and we return that
def findDuplicate(nums) -> int:
    for i in nums:
        idx=abs(i)
        if nums[idx]<0:
            return idx
        else:
            nums[idx]=nums[idx]*-1
    return 0


#["LRUCache","get","put","get","put","put","get","get"]
#[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
#[null,-1,null,-1,null,null,2,6]

#4 LRU Cache
#Approach: Brute Force
#Time Complexity :O(n)
#Space Complexity: O(n)
#Intuition:
#So I have just used deque which is double link list collection
#Things to remember:
#1)In this solution the most recenlty used nodes are on right side
#2)When we add new node we add in it in right most side
#3) LRU node is on left side
#When we insert new node we check first is our capacity is full or not
#If it is full then we chekc if this new key already exist in out hashmap , if it does we remove the key from our deque and re enter it at right side of deque and we update our ahshmap
#same thing when our capacity is not full
class LRUCache:

    def __init__(self,capacity: int):
        self.CAPACITY=capacity
        self.hashMap={}
        self.nodes=deque()

    def get(self,key: int) -> int:
        if not (key in self.hashMap):
            return -1
        else:
            self.nodes.remove(key)
            self.nodes.append(key)
            return self.hashMap[key]

    def put(self,key,value) -> None:
        if len(self.nodes)<self.CAPACITY:
            if key not in self.hashMap:
                self.nodes.append(key)
            else:
                self.nodes.remove(key)
                self.nodes.append(key)
            self.hashMap[key]=value
        else:
            if key not in self.hashMap:
                leastUsedkey=self.nodes.popleft()
                self.hashMap.pop(leastUsedkey)
                self.nodes.append(key)
            else:
                self.nodes.remove(key)
                self.nodes.append(key)
            self.hashMap[key]=value
    
class LruNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next=None

class OptLRUCache:

    def __init__(self,capacity: int):
        self.CAPACITY=capacity
        self.cache={}
        self.head= LruNode(0,0)
        self.tail=LruNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def Insert(self,node:LruNode):
        temp=self.head.next
        self.head.next=node
        node.prev=self.head.next
        node.next=temp
        temp.prev=node
        self.cache[node.key]=node

    def Delete(self,node:LruNode):
        node.prev.next=node.next
        node.next.prev=node.prev
        if node.key in self.cache:
            del self.cache[node.key]

    def get(self,key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node:LruNode=self.cache[key]
            self.Delete(node)
            self.Insert(node)
            return node.val

    def put(self,key,value) -> None:
        if key in self.cache:
            self.Delete(self.cache[key])
        if len(self.cache) >= self.CAPACITY:
            self.Delete(self.tail.prev) 
        newNode=LruNode(key,value)
        self.Insert(newNode)



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#5Reverse K Group Node
#Approach: Brute Force
#TIme COmplexity : DOnt know what it is
#Space COmplexity: O(k) 
#Things to rememeber
#1)Our prev node will be pointer to node just before we start "k" gorup so in start prev points to -1 node in dummy while we reverse the first k nodes in our hread list
#2)End will point to one node after kth node
#3) Doing ths setup we can easily connect out new dummy reversed list of nodes using prev.next->dummy_list.next->end
#Intuition is we make dummy node and add element to that dummy node while out k and count is not equal once that we check if count is equal to k if not we just retunr our new list cause no element to reverse
#else we reverse list of this new dummy list and we get its staRt and end point returned from our method
#Else all stuff is basic linked list stuff need to make your own code in order to understand
def reverseKGroup(head, k) -> Optional[ListNode]:
        end=head
        newHead=ListNode(-1)
        prev=newHead
        while end:
            count=0
            dummy=ListNode(-1)
            tail=dummy
            while count<k and end:
                tail.next=ListNode(end.val)
                end=end.next
                tail=tail.next
                count+=1
            if count<k:
                return newHead.next
            newStart,newEnd =reverseList(dummy.next)
            prev.next=newStart
            newEnd.next=end
            prev=newEnd
        return newHead.next
    
    
def reverseList(head):
        s=None
        prev=head
        nodeEnd=prev
        cur=head.next
        while prev:
            prev.next=s
            s=prev
            prev=cur
            if cur:
                cur=cur.next
        return s,nodeEnd



#Approach: In Place Reverseing Nodes
#Time Complexity :N/A
#Space COmplexity: O(1)
#Intuition :
#Here we are not using additional dummy list so in order to to reverse our k list group
#we do two things, first we check if there are k element present in our list
#If present we reverse the list
#here we great one extra node (-1) and after that node we point to our original head
#Else is in comments
def OthreverseKGroup(head, k) -> Optional[ListNode]:
        end=head
        newHead=ListNode(-1)
        newHead.next=head
        prev=newHead
        while end:
            count=0
            while count<k and end:
                end=end.next
                count+=1
            if count<k:
                break
            prev=OthreverseList(prev,end,prev.next,k)  #we set our new prev to the kth reverse list node now
        return newHead.next
    
def OthreverseList(start,end,head,k):
        s=None
        prev=head
        nodeEnd=prev   #this nodeEnd is to keep track of when we reverse list when do our next prev starts from which is when we reverse k list the first element in list i now last elment and that will be our nodeEnd
        cur=head.next
        while prev and k>0:   #along wiht prev we also check till k >0 cause we dont need extra elments to be reverses other than k size
            prev.next=s
            s=prev
            prev=cur
            if cur:
                cur=cur.next
            k-=1
        start.next=s           #now our start which is pointing just before the nodes we reverses yet 
        nodeEnd.next=end       #end is pointing to nodes after the kth element
        return nodeEnd



testNode=ListNode(1,next=ListNode(2,next=ListNode(3,next=ListNode(4,next=ListNode(5)))))
OthreverseKGroup(testNode,2)