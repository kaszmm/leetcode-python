from ast import List


#2457. Minimum Addition to Make Integer Beautiful
#Intuition:
#So in order to make the n beautiful the intuition is try to make from right side of digits like
#until you get sum of digits less than or equal to target
#
#for example n=12345 target=2
#if     n=12345->12350->12400->13000->20000 
#sumN= 15           11          7            4            2  (<- here we get sumN which is <= target)
#temp=   0              5          65        655        7655 (<-this is our ans)
#
#So Algo intuition is take count=10 and temp=0
#now count is what gonna help us make zeros from right side of n
#We do while loop until our n+temp becomes sumN whose sum is <=target
#so intitially our temp is 0 so we just check if sum of n is less than target isf it is we just return temp whihc is 0
#If that is not the case we take the mod of n with count so intitally our mod of 12345%10 will be 5 so by adding remaining value( count-mod=remaining) we can make our right digit zero , so we update our temp=5 and multiple our count wiht 10, 
#chekc again if n+temp is less than target if it is not we take mod whihc is 45 this time casue 12345%100 is 45 and we update our temp wiht 100-45=65 and we check that again wiht n+temp and so on.. at end we get our temp 
#
#for example n=12345 target=1
#if     n=12345->12350->12400->13000->20000->100000
#sumN= 15           11          7            4            2           1
#temp=   0              5          65        655        7655       87655

def makeIntegerBeautiful(self, n: int, target: int) -> int:
    count=10
    temp=0
     
    while(self.getSum(n+temp)>target):
        mod=n%count
        temp= count-mod
        count*=10
    return temp
    
def getSum(self,num):
    total=0
    for i in str(num):
        total+=int(i)
    return total


#2456. Most Popular Video Creator
#Brute Force Approach
#Things to remember
#1)First Find creatir wiht greater orequal sum and add it to temp list
#2)Find  Creator video wiht highest Value if highest value is same for same creator then get min Id from vids
def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

    #this hashmap is for creator->sum of views
    hashMap1={}
    #this hashmap is for creator->[id,view]
    hashMap2={}
    #initialize hashmap 1 wiht zero on start
    for i in range(len(creators)):
        hashMap1[creators[i]]=0

    #Get sum of views for all creators
    for i in range(len(creators)):
        hashMap1[creators[i]] += views[i]
    
    #In this we set highest view for particular creator, and if that highest view is same as current view we take the least id from both
    for i in range(len(creators)):
        #is no id or view added in hashmap for creator just simply add it
        if creators[i] not in hashMap2:
            hashMap2[creators[i]] = (ids[i],views[i])
        else:     #if id and view already exist in hashmap[creator] then take max view from current view and prev view , and if both view are same get min id of vid from both
            prevId,prevView=hashMap2[creators[i]]
            if prevView<views[i]:
                hashMap2[creators[i]] = (ids[i],views[i])
            elif prevView==views[i]:
                if prevId>ids[i]:
                    hashMap2[creators[i]] = (ids[i],views[i])
                
    #this temp will have all the creators in it which have equal max value 
    temp=[]
    #we get key from hashmap1 whihc have sum of view as max
    maxkey=max(hashMap1,key=hashMap1.get)
    for key in hashMap1:
        if hashMap1[key]==hashMap1[maxkey]:
            temp.append(key)    
    res=[]
    #at last we have creators with max views (temp) and we also have creators wiht min id and max view (hashmap2), just append this result in to res and return it 
    for i in temp:
        curId,curView=hashMap2[i]
        arr=[i,curId]
        res.append(arr)
    return res
            

#2455. Average Value of Even Numbers That Are Divisible by Three
def averageValue(self, nums: List[int]) -> int:
    sumVal=0
    count=0
    for i in nums:
        if i%3==0 and i%2==0:
            sumVal+=i
            count+=1
    if count==0:
        count=1
    return sumVal//count