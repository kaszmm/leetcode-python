
import math
from msilib import MSIDBOPEN_CREATEDIRECT
from typing import List

#1 Binary Search
#Basic Binary Search Funda where we take left adn right and on each iteration we calculate mid, if mid is equal to target we return mid, else we check if cur mid value is less than target we push our left to mid+1
# else we push our right to mid-1 if our mid value is larger than target
def search(self, nums: List[int], target: int) -> int:
    left=0
    right=len(nums)-1
    while(left<=right):   # here we loop until left and right doesnt cross each other 
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1   #return -1 if we never found vlaue in array



#2 Search a 2D Matrix (O(m)+log(n)) <-here m is number rows we have in matrix
#Intuition behind this solution is we have twoc ondition first is all element in row is in ascending order and last element of row is less than first element of next row
# so to find target in sd matrix we first find in whihc row can target exist
#once we located that we then do binary search on that row
#to find in which row target exist we check if last element of current row is less than our target then it means that our target cant exist in this current row because the last element itself is less than our target
#so we increment our row index, now we check again if last element of current row is less than target if not means our tagrte can exist in this row for sure
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    start=0
    end=len(matrix[0])-1
    while(start<len(matrix) and matrix[start][end]<target):
        start+=1
    if(start>=len(matrix)):
        return False
    arr=matrix[start]  #once we get in which row we can find tagret we then do BS in this arr
    start=0
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            start+=1
        else:
            end-=1
    return False      

#(O(log(m)+log(n))) more optimised solution
def OptsearchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    rows,cols=len(matrix),len(matrix[0])
    top,bottom=0,cols-1
    #do binary seacrh for finding in which row our target can exist
    #in order to find in which row our target exist we first check if last element of row is less than target means target is not in range of this row, so shift the top to mid+1
    #if our our target is less than our target row first element still target is not in range of this row so decrease bottom to mid-1
    while(top<=bottom):
        midRow=(top+bottom)//2
        if target>matrix[midRow][-1]:
            top=midRow+1
        elif target<matrix[midRow][0]:
            bottom=midRow-1
        else:
            break
    #we need check first whther we able to find any row in whihc target can exist, if there is no such row in which target can exist our top and bottom will be out of bound. so check for that condition
    if top>bottom:
        return False
    
    #if we had found the target we had break out of loop and we can get that target row by getting m,id of curren top and bottom
    targetRow=(top+bottom)//2
    start=0
    end=cols-1
    while(start<=end):
        mid=(start+end)//2
        if matrix[targetRow][mid]==target:
            return True
        elif matrix[targetRow][mid]<target:
            start=mid+1
        else:
            end=mid-1

    return False


#3 KOKO Eating BANANAS (O(nlog(n)))  n->number of element in piles, logn->binary search
#Intuition behind this is let say the minimum rate for eating the piles of banans in h hours is 1 while maximum amount will be max(arr)
#With knowing that we do binary search from 1...max(arr) and we calculate hours taken for eating piles is more than hours given to us, 
#that tells us that we need to increase our satrt range so that we eat more bananse under given hour
#if opposite was true, and we can eat all bananas under given hours that tells us that there might be possible other k value in whihc we can eat all banans under given hour
#so we decrease our range of end and check again if we still can eat bananas
def minEatingSpeed(piles, h) -> int:
        start=1   #start from min output  k
        end=max(piles)   # end max output k
        res=max(piles)
        while(start<=end):
            k=(start+end)//2      #our current k output
            hoursTaken=0
            for bananas in piles:                    # we check timetaken for current output k 
                hoursTaken+= math.ceil(bananas/k)
            if hoursTaken>h:        #if timetaken is more than it means we need to increase our start to k+1 in order to eat all banans under given hour
                start= k+1
            else:
                res=min(res,k)    #if hourtaken is less than given hour than update our res to min(current_k,res) and decrease our end range in order to get even less k  
                end=k-1
        return res





#4 Time Based Key-Value Store
#Key thing to remember here is when we set values in keys the order at which the inpput set will be given is in strictly increasing order (timestamps) 
#set function is pretty self explanatory
#the get function we get the values under key and we do binary search on that values if curr_timestamp > given_timestamp then we decrease our range from end so that we can get closer to timestamp
#if we get current_timestamp< given_timestamp then we update our result to that current_timestamp
def __init__(self):
    self.dictionary={} #key: list of [value,timestamp]

def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self.dictionary:
        self.dictionary[key]=[]
    self.dictionary[key].append((value,timestamp))
        
def get(self, key: str, timestamp: int) -> str:
    tuples=self.dictionary.get(key,[])
    start=0
    end=len(tuples)-1
    res=""
    while start<=end:
        mid=(start+end)//2
        if tuples[mid][1]==timestamp:
            return tuples[mid][0]
        elif tuples[mid][1]>timestamp:
            end=mid-1
        else:
            res=tuples[mid][0]
            start=mid+1
    return res




#5 Median of two sorted array
#Brute Force O((m+n)Log(m+n))
#we just merged both array , sort them and return the mid value
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    mergedList=nums1+nums2
    mergedList=sorted(mergedList)
    if len(mergedList)%2==0:
        mid=(len(mergedList)-1)//2
        median=(mergedList[mid]+mergedList[mid+1])
        return median
    else:
        mid=(len(mergedList)-1)//2
        return mergedList[mid]


#Sub Optimised Solution wiht O(m+n) time and O(1) Space complexity
#The approach is simple if we think, so we have two sorted arrays so we can leverage that ans we use thwo pointer one for qrr1 and second for arr2
#now we iterate over two pointer and increment our pointers when we encounter thta our pointer 1 value is less than pointer 2 or vise versa, why?
#COntratry to this solution you can achive this same solution if you use an array and store all the element you encounter in sorted manner and at end
#just return the mid vlaue of resultant array, but that approahc can cost us O(n) space compelxity
#On this SOlution we can achive wiht O(1) space if we iterat over two sorted array using our pointer and storing the value we encounetr in our two variables prev and cur
#why two variables? cause in case of even array leneght we need two values to retunr average median
#now while storing the values in our prev and cur we also keep track of counter ,why? cause we ietarteover two array until we stumble upoin our mid llength cause afterall we just need our mid
#so when our counter gets equal to mid we break from loop and based on length of array we return boht values
def subOptFindMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    p1,p2=0,0
    counter=0
    cur=0
    prev=0
    total=len(nums1)+len(nums2)
    #here we loop till we reach half the elements of array length
    while counter<=(total//2):
        val1=nums1[p1] if p1<len(nums1) else float("infinity")  #here we store values at p1 pointer ,if p1 is out of boudn we store infinity, 
                                                                #because when this infinity is compared wiht element in p2 pointer then p2<p1 is alwasy satisfied and we only store p2 value
        val2=nums2[p2] if p2<len(nums2) else float("infinity")  #same for p2 as well
        if val1<=val2:                          
            prev=cur         #store the curr in prev
            cur=nums1[p1]    #update cur, also notice that we never gonna come in this if stateemnt if p1 is out of bound cause at this pointer p1 is infinite so this if never executes if p1 is out of bound
            counter+=1       #increment counter
            p1+=1            #increment p1
        else:
            prev=cur           
            cur=nums2[p2]
            counter+=1
            p2+=1

    if total%2==0: #if even length array
        return (prev+cur)/2
    else:   #if odd length array
        return cur
        

#Optimal Approach O(log(min(m,n))) Space O(1)
#Just Watch Neetocde and Raj Vikramditya Video on this to even get more understanding of it
def optFindMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    #this awesome recurive code ensures that we get num1.length < num2.length , or basicallly it swaps arrays if array 1 is larger than arraay 2
    if len(nums1)>len(nums2):
        return optFindMedianSortedArrays(nums2,nums1)
    A=nums1   #A will always be samller than B
    B=nums2
    left=0
    right=len(A)-1
    half= (len(A)+len(B))//2
    while True:    #I am unable to know what condition to put in aside from True
        cutA=(left+right)//2
        cutB=(half-1)- (cutA+1)  #half-1 because our half is 1 based index but we need our cutb to 0 indexed based, cutA+1 because our cutA is 0 index based but to know the actual value of cuta so we make cutA 1 index based
        ALeft=nums1[cutA] if cutA>=0 else float("-inf")   #Here Aleft means the after the cut we had two sub arrays one on left and one on right, so this values represents max value( or right most element) from left sub array
        ARight=nums1[cutA+1] if cutA+1<len(A) else float("inf") #Here ARight means min value(or left most element) from right subarray after cutting A
        BLeft=nums2[cutB] if cutB>=0 else float("-inf")      
        BRight=nums2[cutB+1] if cutB+1<len(B) else float("inf")

        #if partition is done on both array is correct 
        if ALeft<=BRight and BLeft <=ARight:
            if (len(A)+len(B))%2==0:
                return (max(ALeft,BLeft)+min(ARight,BRight))/2     #now we return median for even numbers but to get values we get max of left sub arrays from A and B , and we take min of right subarrays of A and B
            else:
                return min(BRight,ARight)             #for odd lenegth we take min of right sub arrays of A and B because when we cut odd length array one extra element goes to right sub array
        elif ALeft > BRight:                     #when right most element in left subarray is larger than left most element in right subarray than it means we need to decrease our ALeft value in order to do that we just shift our right to mid-1
            right=cutA-1
        else:                #when BLeft >ARight is true, when our left most elemnt of right subarray in A is smaller than right most element of left subarray of  then it measn we need to increase our A value so to do that we can shift our left pointer to mid+1
            left=cutA+1
            
optFindMedianSortedArrays([1,3],[2])

