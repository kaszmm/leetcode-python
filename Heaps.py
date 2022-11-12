from ast import List
from collections import defaultdict, deque
import heapq
import math
import copy

#1 Kth Largest Element in a Stream
#Approach: Binary Search
#TIme Complexity: nlog(n) for constructor and k*n*log(n) for add method because for each insert in array it takes O(n)and log(n) for Binary Search and k time si add method called
#Space Complexity: O(n)
#Intuition:
#Intitlaly when we ahve array we sort it in ascending order
#Now rememeber we need largest numebr not smallest number
#Intuition is we have sorted array so when new values is added we check on which index that value can be inserted and we just insert that vlaue in array and'
#return the kth largest element from last cause our array is in ascending order
class KthLargest:

    def __init__(self, k, nums):
        self.arrList=sorted(nums)
        self.largest=k
    def add(self, val: int) -> int:

        #If Intially our array is null, or last value of array is smaller or equal to current val, in this case we can just appedn that val in out array at last
        if not len(self.arrList) or self.arrList[-1]<=val:
            self.arrList.append(val)
        elif self.arrList[0]>=val:               #if first element of array is larger than current val than we can insert that val on 0th index of array 
            self.arrList.insert(0,val)
        else:                                  #else we find at which index our val can be inserted in array
            start=0
            end=len(self.arrList)-1
            while start<end:
                mid=(start+end)//2
                if self.arrList[mid]>val:              #if mid value is larger than current val we decrement our raneg from end so we can get our current val in tighter range
                    end=mid-1
                else:
                    start=mid+1                      #if mid val is less than or equal to current val we juts increment our start range so we can find mid even in tighter range 

            #at this point our start and end are equal that is why we exited loop 
            if  self.arrList[start]<=val:                     #if start or end value is less than or equal to current val we insert to next index of start cause current val is largeer than start idx
                self.arrList.insert(start+1,val)
            else:                                         #else if val is smaller than start idx we can insert at start index
                self.arrList.insert(start,val)
        return self.arrList[len(self.arrList)-self.largest]


#Approach: Min Heap
#Time Complexity: nLog(n) <-to generate heap in constructor and mlog(n)<- for add function here m is number of times add will be called
#Space Complexity:O(k) cause we make our heap and reduce it down till our heap length is k
#Intuition:
#here we use the min heap instead of max heap, because if we take max heap we cant traserve to kth element in heaps, so instead we use min heap
#now what advantage min heap provides is if I have element like [3,4,1,2] and k=2 then our top two element will be [3,4] 
#so we only keep 3,4 in ourmin heap , now remember that 1,2 is never gonna be 2nd largest element in array cause let say if we add 1 in to our array thne [3,4,1,2,1] 
#here also our 2nd largest will be 3 and not 1,2 so we keep track of number of k largest elements in our heap

#now why use min heap? cause if we have min heap of k size element in it, then top of elemnt in min heap will alsways be kth largest element in our array.
class OptKthLargest:

    def __init__(self, k, nums):
        self.minHeap=nums
        self.k=k
        heapq.heapify(self.minHeap)             
        while len(self.minHeap)>k:                #remove unnessary elmenets from heap and keep only k elements in heap
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)              #add new element in our heap
        if len(self.minHeap)>self.k:                  #if our have elements less than k then dont pop from it , cause heap can be initialised as [] , and due to that we will not pop form heap until our heap size become equal to k
            heapq.heappop(self.minHeap)                     
        return self.minHeap[0]                     #return top of heap element




#2 Last Stone Weight
#Time Complexity: nlog(n)  -> heapify takes O(n) time to make heap from array, and push and pop feature of heap takes log(n) but we are gonna call push and pop probably n times so it becomes n(log(n)
#Space Complexity: O(n)
#Intuition: we make a max heap , we take two stones from amx heap we take diff of both stones, and if diff is greater than 0 we push that new diff as new stone in max heap
#at end we might have 1 stone left in heap or no stone based on that we return result
#To implement max heap we have to substract our stones values to -1 , casue python only provide min heap

def lastStoneWeight(stones) -> int:
    if len(stones)==1:
        return stones[0]
    newStones=[i*-1 for i in stones]
    heapq.heapify(newStones)
    
    while len(newStones)>1:
        stone1=-1*heapq.heappop(newStones)
        stone2=-1*heapq.heappop(newStones)
        newStone=stone1-stone2
        if newStone:
            heapq.heappush(newStones,-1*newStone)
    return -1*newStones[0] if len(newStones)>0 else 0    # or do something like , what it does is if our heap is empty it append 0 to it and retunr 0 but if not empty it just retunr max stone in heap
                                                         #heapq.heappush(newStones,0)   
                                                         #return abs(newStones[0])


#3 K Closest Points to Origin
#Approach: Naive Approach using Max Heap
#Time Complexity: nlog(k)  -> heapify takes O(n) time to make heap from array, and push and pop feature of heap takes log(k) but we are gonna call push and pop probably n times so it becomes n(log(k)) logk becuas elour heap is of size k not n
#Space Complexity: O(n)
#Intuition: 
#What we do is make a max heap based on distacnes and upon iterating over points we push the distances and if our heap length becomes greater than k we pop from heap
def kClosest(points, k: int):
    priorityQueue=[]
    for x,y in points:
        distance=math.sqrt(x**2+y**2)
        heapq.heappush(priorityQueue,[-1*distance,x,y])
        if len(priorityQueue)>k:
            heapq.heappop(priorityQueue)
    res=[]
    for distance,x,y in priorityQueue:
        res.append([x,y])
    return res

#Approach: Sorting
#Time Complexity: nlog(n)  ->sorting takes nlog(n) time
#Space Complexity: O(n)
#Intuition:
#we sort Array based on distances and after that we get first k element and return
def kClosest(points, k: int):
    points.sort(key=lambda dist:dist[0]**2+dist[1]**2)
    res=[]
    for i in range(k):
        x,y=points[i]
        res.append([x,y])
    return res


#Approach: Using Kd Tree using Externla scipy library
#This approch can be answered in floow up question like what if our data is for 1 million or so then use kd tree
# def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
#         tree = spatial.KDTree(points)
# 		# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
#         distance, idx = tree.query(x=[0,0], k=K, p=2) 
#         return [points[i] for i in idx] if K > 1 else [points[idx]]


#Approach: Optimised Approach using Min Heap
#Time Complexity: klog(n)  -> here we iterate only k times and in minheap and pop elements(log(n) which counts to klog(n)
#Space Complexity: O(n)
#Things to Remember:
#1)We done need to take sqrt for ecludian distances, cause if x^2+y^2 itself if is greater than a^2+b^2 then the sqrt itself will also be larger for that points, so no need to take sqrt for min distance find
#2) We used Min heap
#3) When using PriorityQueue in python , python takes first argument to do heap sort on list, ie if I have tuples in list like [[x1,y1],[x2,y2]], 
    #then heapifying it python will take x1 and x2 to do heap sort
#Intuition:
#At first we just append all the distances in our array list
#We than simpley heapify it , and as this is gonna be min heap we then pop first k element from heap cause they are gonna be k smallest distacnes in heap 
def kClosest(points, k: int):
    priorityQueue=[]
    for x,y in points:
        distance=x**2+y**2
        priorityQueue.append([distance,x,y])
    heapq.heapify(priorityQueue)
    res=[]
    while k>0:
        dist,x,y=heapq.heappop(priorityQueue)
        res.append([x,y])
        k-=1
    return res




#4  Kth Largest Element in an Array
#Approach: Naive Approach
#TIme Complexity:nlog(n)  ->Sorting takes nlog(n) which is merge sort
#Space Complexity:O(1)
#Intuition: We just sort the array in ascending order and return the kth largest element from last
def findKthLargest(nums, k: int) -> int:
    nums.sort()
    return nums[len(nums)-k]


#Approach: Max Heap Approach
#TIme Complexity:klog(n)   -> pop takes log(n) time and we need to pop from max heap till our count reach k so klog(n)
#Space Complexity:O(1)
#Intuition: We make a max heap for given nums array and after that we pop from top till our count reach k, to get the kth largest number in array
  
def findKthLargest(nums, k: int) -> int:
    newList=[-1*num for num in nums]
    heapq.heapify(newList)
    for i in range(k-1):
        heapq.heappop(newList)
    return -1*newList[0]


#Appraoch: Quick Select
#TIme Complexity:O(n)   -> This O(n) is average time complexity and this is most optimal one
#Space Complexity: O(1)
#Intuition: We use Quick select Algo, in which we take last element in our array as pivot everytime, this taking last element for pivot is lomuto's partiotioning scheme
#after that from pivot each element should be less than pivot and on right greater than pivot
#Once that is done we check if our k is less than p then it emasn our exist in left side of pivot else our k exist in right side of pivot
#Also we check if our k==p it means we already found our kth largest numebr in array, why? cause remember pivot is the only element that is sorted 
#Due to this if k==p then our kth largest will be num[p] itself
def findKthLargest(nums, k: int) -> int:
    kFromLast=len(nums)-k              #this variable we are gonna use instead of k, becuase rememebr we are sorting array in ascending order but we need largest element , so in order for that we need to know the index from last and not first so length-k=kth from last in array
    left=0
    right=len(nums)-1
    def QuickSelect(l,r):
        pivot=nums[r]
        p=l
        for i in range(l,r):
            if nums[i]<=pivot:
                nums[p],nums[i]=nums[i],nums[p]
                p+=1
        nums[p],nums[r]=pivot,nums[p]
        if kFromLast>p:                      #our kth lies in right side of partition
            return QuickSelect(p+1,r)
        elif kFromLast<p:                     #our kth lies in left side of partition
            return QuickSelect(l,p-1)
        else:
            return nums[p]                     #our kth is at p index so we found our kth largest
    return QuickSelect(left,right)





#621. Task Scheduler   watch: https://www.youtube.com/watch?v=ySTQCRya6B0&t=282s
#TIme Complexity:O(n*m) ~ O(n) cause here n->tasks and m->idle time but here idle time is only 100 so it can be ignored
#Space Complexity: O(n)
#Intuition:
#We first get all the different charcters freq in dictionary
#and we also make max heap based on freq, why tasks with max freq first? cause we need to use the taks wiht most freq more in order for that when ever there is idle time
#we will try to use the most frequenet tasks
#now we dont actually care about what task it is what we need to look for is the diff freq we have
#so we use queue and in queue we add the freq of task and time it can be poped from queue and add to heap for task processing

def leastInterval(tasks, n: int) -> int:
    if n==0 :
        return len(tasks)
    taskDict={}
    for i in tasks:                          #smart way of adding the freq in dictionary
        taskDict[i]=taskDict.get(i,0)+1
    maxHeap=[]
    for key,value in taskDict.items():
        maxHeap.append(-1*value)
    heapq.heapify(maxHeap)   #max heap for tasks based on freq
    queue=deque()
    time=0              
    while maxHeap or queue:           #while we either have tasks in heap or queue
        time+=1                       #we increment time cause our CPU will now process one task
        if maxHeap:                    #if we have task in heap then we pop from it and we decrement the freq for that task and add it to queue to be used when its time is equals to current time
            currentCount=1+heapq.heappop(maxHeap)
            queue.append([currentCount,time+n])
        if queue and queue[0][1]==time:                       #if we have tasks in queue and time in those task is equal to current time then they are allowed to be processed again so add them into heap for processing
            heapq.heappush(maxHeap,queue.popleft()[0])
    return time
        
#Tip: watch knowledge gate or kevin naught vid
#TIme Complexity:O(n*m) ~ O(n) cause here n->tasks and m->idle time but here idle time is only 100 so it can be ignored
#Space Complexity: O(n)
#Intuition:
#We first get all the different charcters freq in dictionary
#and we also make max heap based on freq, why tasks with max freq first? cause we need to use the taks wiht most freq more in order for that when ever there is idle time
#we will try to use the most frequenet tasks
#now we dont actually care about what task it is what we need to look for is the diff freq we have
#so we use queue and in queue we add the freq of task and time it can be poped from queue and add to heap for task processing
def leastInterval(tasks, n: int) -> int:
    taskDict={}
    for i in tasks:                          #smart way of adding the freq in dictionary
        taskDict[i]=taskDict.get(i,0)+1
    maxHeap=[-value for value in taskDict.values()]
    heapq.heapify(maxHeap)   #max heap for tasks based on freq
    res=0
    while maxHeap:
        taskQueue=[]                                                                                                                                   
        for i in range(0,n+1):                    #why we run from [0..n+1] because let say we have AABB and n=2 running for 0..n will result in having A->B->exit loop, 
                                                #but we want to be A->B->idle->exit loop so due to that we run for n+1 cause we also have to inclue=de the current task 
                                                # we are processing which is A and then we need to wait for n=2 times so in total we will run for 2(cooldown time)+1(currentTask)=3
            curTask=abs(heapq.heappop(maxHeap))
            taskQueue.append(curTask-1)                  
        
        for task in taskQueue:                     #what ever tasks wiht >0 freq remaining add them again in heap
            if task:
                heapq.heappush(maxHeap,-task)
        res+= len(taskQueue) if not len(maxHeap) else n+1                    #add the time taken for processing task to n+1 (currentTask+cooldown time) if we still got some tasks in maxheap, else just add the len(taskQueue) whihc are finished 
                                                                        #why we do it? cause if we still have some task left in our heap it means we must have run n+1 times to process task or sitting idle
                                                                        #but if there is not tasks left in maxheap then it means that we might have completed all tasks before n+1 and we just need to account for the task we completed whihc is in our taskQueue
    return res


#Tip: watch nick white or ask someone
#TIme Complexity: O(n)
#Space Complexity: O(26) ~ O(1)
#Intuition: I dont quite understand, but can explain what the code is       
def leastInterval(tasks, n: int) -> int:
    task_freq=[0]*26
    for task in tasks:                         #get freq of chracters ini arr
        task_freq[ord(task)-ord('A')]+=1
    task_freq.sort()                            #sort array 
    maxTaskFreq=task_freq[-1]-1                 #get max freq and remove -1 cause we do not need to wait for task that is last done
    idleSlots=maxTaskFreq *n                    #get empty idle slots by multiple our max freq and cooldown time
    
    for idx in range(24,-1,-1):                         #start traversing in revserse cause we can start from max frquencies 
        idleSlots -= min(task_freq[idx],maxTaskFreq)     #this we do cause there might be possible bility that other taks also have same freq as current max freq 
                                                        #and we did -1 in max freq cuase we dont need to wait for alst task, 
                                                        # so taking min will ensure that even if current task freq is same as max Freq we take max Freq-1 
        
    return len(tasks) if idleSlots<0 else idleSlots+len(tasks)    #is there are still idle slots remainign then return remaining idle slot+ lenght of total tasks, 
                                                                #if all our idle slots used means idle slots<=0 then just return lenght of total tasks






#Approach naive not very well thought!
#TIme Complexity: O(k*n)    log(n) for postTweet cause we heappush every tweet for user, 
# follow will take O(k) time cause on each follow and unfollow we iterate over k followers list to append/remove  this new/old follower ,
# getNewsFeed will take O(n*k) cause firts we append all the list of n tweets of k followers in one list and then we apply heapify on it!
#Space Complexity:  O(n*k)
#Intuition we use Linkedlist for tracking the user<->List<followers> and use simple hashmap for user<->List<Tweets>
#follow and unfollow we need to ietrate over k nodes to either find last node to append new follower(follow) or to find kth node to remove it from linkedlist(unfollow)
#For Post tweets we heappush tweet based on if user already have tweets else we just append this new tweets in user tweet list
#get news feed we take new list and we append all the list of tweets of all the followers user have including user's tweets and then we heapify it and get most top 10 tweets doing while loop 10 times
#or till we empty our heap
class FollowNode:
    def __init__(self, x: int, next: 'FollowNode' = None):
        self.val=int(x),
        self.next=None
        
class Twitter:

    def __init__(self):
        self.userTweets={}
        self.userFollowing={}
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        if userId in self.userTweets:
            heapq.heappush(self.userTweets[userId],[-self.count,tweetId])
        else:
            self.userTweets[userId]=[]
            self.userTweets[userId].append([-self.count,tweetId])
            if userId not in self.userFollowing:
                self.userFollowing[userId]=FollowNode(userId)
        
    def getNewsFeed(self, userId: int):
        if userId not in self.userFollowing:
            return []
        tweets=[]
        res=[]
        cur=self.userFollowing[userId]
        while cur:
            tweets += self.userTweets[cur.val[0]] if cur.val[0] in self.userTweets else []
            cur=cur.next
        heapq.heapify(tweets)
        while tweets and len(res)<10:
            res.append(heapq.heappop(tweets)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowing:
            self.userFollowing[followerId]=FollowNode(followerId)
        
        followNodes=self.userFollowing[followerId]
        cur=followNodes
        while cur.next:
            if cur.next.val[0]==followeeId:
                return
            cur=cur.next
        cur.next=FollowNode(followeeId)
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowing:
            return
        followNodes=self.userFollowing[followerId]
        prev=followNodes
        cur=followNodes.next
        while cur:
            if prev.next.val[0] != followeeId:
                prev=prev.next
            else:
                break
            cur=cur.next
        prev.next=cur.next if cur else None


#Tip: Watch Neetcode Explaination
#Appproach: Used HashSet for follow/unfollow whihc gives O(1) , used hashMap for posttweet which gives O(1),
    # used minHeap in getNewsFeed which gives O(k) cause we heapify and here k is number of followers and appending 10 latest tweets will take 10*log(k)
#TIme Complexity: O(k)
#Space Complexity: O(k*n) k -> number of users and n->is tweets per user
#Intuition:
#we we use two hashmaps one for tracking user<->List<tweets> and another for user<->List<followers>  ,and why we use it is given in "Appproach:" above
#So for following and unfollowing we can easily add and remove follower for spcific user easily
#for posting tweets we just append the tweet along wiht timestamp which will get decremented each time , 
# cause remember that python sont have maxHEap implementation so gonna use negative number for latest tweets, 
#and why simple append in list? because that indicates that our latest tweets for that user will always start from last to first

#now main logic is in getNewsTweet,
#so remember? that we know that most latest tweets for all user is at end of list?
#we leverage that so first what we do is just append the latest tweets from all user's follower along wiht user itself
#now we heapify that so that we get most frequent tweet on top
#now while our minheap is not empty and also our len <10 we pop most frequent tweet from minheap and ppend it to our result, but also we push the latest tweet from list of user whose tweet we just poped from minheap
#what that ensures thta we will always get latest tweets from all the users
class OptTwitter:

    def __init__(self):
        self.userTweetMap=defaultdict(list)
        self.userFollowingMap=defaultdict(set)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweetMap[userId].append([self.count,tweetId])
        self.count-=1


    def getNewsFeed(self, userId: int):
        latestTweets=[]
        minHeap=[]
        self.userFollowingMap[userId].add(userId)
        for followee in self.userFollowingMap[userId]:
            if followee in self.userTweetMap:
                lastTweetIdx= len(self.userTweetMap[followee])-1
                timeStamp,tweet=self.userTweetMap[followee][lastTweetIdx]
                minHeap.append([timeStamp,tweet,followee,lastTweetIdx-1])
        
        heapq.heapify(minHeap)
        while minHeap and len(latestTweets)<10:
            timeStamp,tweet,followee,tweetIdx=heapq.heappop(minHeap)
            latestTweets.append(tweet)
            if tweetIdx>=0:
                newTimeStamp,newTweet=self.userTweetMap[followee][tweetIdx]
                heapq.heappush(minHeap,[newTimeStamp,newTweet,followee,tweetIdx-1])
        return latestTweets 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowingMap[followerId].add(followeeId)     
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowingMap[followerId]:
            self.userFollowingMap[followerId].remove(followeeId)


#Tip: Read this -> https://leetcode.com/problems/design-twitter/discuss/82825/Java-OO-Design-with-most-efficient-function-getNewsFeed
#Appproach: All stuff is same as above solution, but this solution is implemented wiht proper OOD 
#TIme Complexity: O(k)
#Space Complexity: O(k*n) k -> number of users and n->is tweets per user
#Intuition wise there is not diff than above solution , just instead of using list we used linked list to track latest tweets by reversing each nodes when new tweet is added in it
#this way our head will always point to most recent to least recent
#We created Tweet and User Object and used that in our solution for implementation of diff methods
class Tweet:
    def __init__(self,tweetId:int,timeStamp:int,next:'Tweet'=None):
        self.TweetId=tweetId
        self.TweetedTime=timeStamp
        self.NextTweet=next
class User:
    def __init__(self,userId:int=0,tweet:'Tweet'=None,twitterObj:'OODTwitter'=None):
        self.UserID=userId
        self.Following=set([])
        self.TweetHead=tweet
        self.tweetObj=twitterObj

    def Follow(self,id:int):
        self.Following.add(id)

    def Unfollow(self,id:int):
        self.Following.remove(id)

    def Post(self,tweetId:int):
        tweet=Tweet(tweetId,self.tweetObj.timeStamp)
        tweet.NextTweet=self.TweetHead
        self.TweetHead=tweet
        
class OODTwitter:

    def __init__(self):
        self.timeStamp=0
        self.userMap= defaultdict(User)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userMap:
            newUser=User(userId,None,self)
            newUser.Follow(userId)
            self.userMap[userId]=newUser
        self.userMap[userId].Post(tweetId)
        self.timeStamp-=1

    def getNewsFeed(self, userId: int):
        latestTweets=[]
        minHeap=[]
        for following in self.userMap[userId].Following:
            if self.userMap[following].TweetHead:
                timestamp=self.userMap[following].TweetHead.TweetedTime
                curTweet=self.userMap[following].TweetHead
                minHeap.append([timestamp,curTweet])
        heapq.heapify(minHeap)
        while minHeap and len(latestTweets)<10:
            timeStamp,curtweet=heapq.heappop(minHeap)
            latestTweets.append(curtweet.TweetId)
            if curtweet.NextTweet:
                timestamp=curtweet.NextTweet.TweetedTime
                nextTweet=curtweet.NextTweet
                heapq.heappush(minHeap,[timestamp,nextTweet])
        return latestTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userMap:
            newUser=User(followerId,None,self)
            newUser.Follow(followerId)
            self.userMap[followerId]=newUser
        if followeeId not in self.userMap:
            newUser=User(followeeId,None,self)
            newUser.Follow(followeeId)
            self.userMap[followeeId]=newUser   
        self.userMap[followerId].Follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId!=followerId and followeeId in self.userMap[followerId].Following:
            self.userMap[followerId].Unfollow(followeeId)   







