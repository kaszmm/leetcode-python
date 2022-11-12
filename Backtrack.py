from ast import List

#BIG TIPPPP use list[:] instead of list.copy()   ,[:] is much faster than copy()


#1 Subsets
#Appproach: Dfs Traversal Backtracking
#TIme Complexity: O(n(2^n))
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list to add subsets in it
#Intuition:
#so for each index it does dfs traversla and add all the subset it encounters when our index gets out of bound we return
def subsets(nums):
    res=[[]]
    def dfs(list:list,curIdx):
        if curIdx>=len(nums):   #if curIdx out of bound then return
            return
        list.append(nums[curIdx])          #add the curIdx element into out list
        res.append(list.copy())              #add that list into our res arr
        for i in range(curIdx+1,len(nums)):       #we loop for eacg element starts from curIdx+1 to n , because we alrewady traversed curIdx but we need to traverse other elements in array
            dfs(list,i)                 #we recrusively traverse for next element
            list.pop()                    #on each recursion we add enw element in our list after we have returned from that recursive call we pop that element and then we add next element in our arr into our list
        return
    for i in range(0,len(nums)):                #since we are doing recursion dfs on each element individually , we have travser for each index using loop and call dfs for each idx
        dfs([],i)
    return res

#Appproach: Dfs Traversal Backtracking
#TIme Complexity: O(n(2^n))
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list to add subsets in it
#Intuiton:
#With slight change in code we can eliminate the for loop we use to call dfs , and that is instead of appending element in to our list on each recursive call we can just add
#that element when in our loop which loops from 0..n wiht that we will add all the possible element and its subsets in our result
def subsets2(nums):
    res=[]
    def dfs(list:list,curIdx):
        res.append(list.copy())
        for i in range(curIdx,len(nums)):
            list.append(nums[i])
            dfs(list,i+1)
            list.pop()
        return
    dfs([],0)
    return res

#Tip: Watch Neetcode vid for it! https://www.youtube.com/watch?v=REOH22Xwdkk&t=278s
#Appproach: Dfs Traversal Backtracking
#TIme Complexity: O(n(2^n))
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list to add subsets in it
#Intuiton:
#This logic is quite diffferent the above one's, this logic uses idea of two choices we make, one choice is to add element i our list and another choice is not to add in list
#so what we do is we just traverse dfs for boht choices one we add and do dfs traversal and for another we pop the element we added in list and again do dfs traversal
def subsets3(nums):
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):              
            res.append(subset.copy())
            return
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res

#Tip: Watch this article: https://leetcode.com/problems/subsets/discuss/27278/C%2B%2B-RecursiveIterativeBit-Manipulation
#Appproach: Iterative version
#TIme Complexity: O(n(2^n))
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list to add subsets in it
#Explaination:
# Using [1, 2, 3] as an example, the iterative process is like:
# Initially, one empty subset [[]]
# Adding 1 to []: [[], [1]];
# Adding 2 to [] and [1]: [[], [1], [2], [1, 2]];
# Adding 3 to [], [1], [2] and [1, 2]: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].
def subsets4(nums):
    res = [[]]
    for num in nums:
        res += [item+[num] for item in res]
    return res

#Same as Above just in detail of what the code is doing
#so we loop for each nums in outer loop
#and inner loop we loop till our sixe of res arr and and on each arr in our res's array of array we append the current num we iterating and appedn that new array ito our result
def subset4(nums):
    res=[[]]
    for num in nums:
        resSize=len(res)       #take size and use inner loop till the size of res each time
        for i in range(0,resSize):
            arr=res[i].copy()          #get array in res
            arr.append(num)             #append new num elemement in this array
            res.append(arr.copy())           #re append this new array in our res array
    return res












#2 Permutations
#Appproach: Recursive version
#TIme Complexity: O(n!)
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list
#Intuition:
#We use set in problem to track which element we already added in our permutation, and we onlly need to use one for loop and that for loop will iterate over all the numbers
#each time and to prevent it to add the same number again we use set ,once we are done ad return from our call we will remove the element we just added from list and set,
#and we do the same recursion for next element in our loop
def permute(nums):
    res=[]
    values=[]
    visited=set([])
    def dfs(visited,list):
        if len(list)==len(nums):
            res.append(list[:])
            return
        for i in range(0,len(nums)):       #iterate over all the element
            if nums[i] in visited:                 #if num is already visited then skip it
                continue
            list.append(nums[i])            #add not visited num to list and set
            visited.add(nums[i])
            dfs(visited,list)                #do recusive call for this now
            visited.remove(nums[i])          #once done and get retunred from recusive call remove the added element from list and set
            list.pop()
        return
    dfs(visited,values)
    return res

#Tip: What Neetcode Video for it
#Appproach: Recursive version
#TIme Complexity: O(n!)
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list
#Intuition:
#On each recurive call we pop first elemnt and find possible permutations for remaining array and we do it till we get len==1 cause permuattion of len==1 is number itself,
#after that we return that and we append the popped elmeent from array into this new res and add this into our main res array
def permute2(nums):
    res=[]
    if len(nums)==1:
        return [[nums[0]]]
    for i in range(len(nums)):
        num=nums.pop(0)
        newarr=permute2(nums)
        for ar in newarr:
            ar.append(num)
        res.extend(newarr)
        nums.append(num)
    return res





#3 Subset II
#Appproach: Recursive version   (We branch and decide to choose or not to choose)
#TIme Complexity: O(n*2^n)
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list
#Things to Rememebr:
#1) We sort our array in order to keep track of duplicates in array
#2) Order of subset doesnt matter so a subset let say 441 and 414 is considered same and if our sol have any one of it then its considered correct 
#but if our sol have both of this subsets than it is considered incorrect cause 441 and 414 is duplicates subsets
#Intuition:
def subsetsWithDup(nums):
    res=[]
    nums.sort()
    def dfs(list,curIdx):
        if curIdx>=len(nums):       #also handles our of bound indexes
            res.append(list[:])
            return
        list.append(nums[curIdx])
        dfs(list,curIdx+1)
        list.pop()
       
        #logic is same as subset I provided by neetcode except we put a little logic here, and that is so in this we sort our array first and now
        #we should know one thing is when we make decision of include element and not include elemnt in not include element we need to also not include the duplicate vlaues of that element
        #in order for that in our sorted array we will skip all the duplicate elements and then make decision of not include element, this ensures that our res will not ahve duplicates
        while curIdx+1<len(nums) and nums[curIdx]==nums[curIdx+1]:  
            curIdx+=1
        dfs(list,curIdx+1)             #this case will at end add [] in our subset whihc is also valid subset of any array
        return
    dfs([],0)
    return res

#Appproach: Recursive version   (we scan throught entire array and add unique subsets on the way)
#TIme Complexity: O(n*2^n)
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list
#Things to Rememebr: Same as Above
#Intuition: Intution is same as Subset I problem wiht just a little code
def subsetsWithDup2(nums):
    res=[]
    nums.sort()             #sorted array
    def dfs(list,curIdx):
        res.append(list.copy())
        for i in range(curIdx,len(nums)):
            if i==curIdx or nums[i]!=nums[i-1]:   #<---- we do recurison if our i is our curIdx or our cur ith num is not same as i-1th num, this prevent duplicates, also why previledge for i==curIDx?
                list.append(nums[i])                       #cause see if let say our array is 112 then not considering the first 1 and considering the second 1 will be mistake
                dfs(list,i+1)                               #becuase the 1st 1 can have more subsets then the 2nd 1 so if our start of loop is same as our curIdx we take it and we avoid dfs for 2nd 1 afterwards
                list.pop()
        return
    dfs([],0)
    return res

#Appproach: Iterative Version
#TIme Complexity: O(n*2^n)
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list
#Intuiion:
#we sort array so we caN group all duplicates together
#we keep track fo variable begin which tell us to whther start adding new element in array from 0 or to skip certain element in array
#so when we encounter duplicate our begin will be size of res but this is not the updated size but prevoius size of result like if I have [1,2,2] and when we encounter second 2 our begin will 
#have valus of len when we added 1 into our result
def subsetsWithDup3(nums):
    res=[[]]
    nums.sort()
    begin=None   
    for i in range(len(nums)):
        if i==0 or nums[i]!=nums[i-1]:          #we track of begin 
            begin=0
        resSize=len(res)       #take size and use inner loop till the size of res each time
        for j in range(begin,resSize):
            arr=res[j].copy()          #get array in res
            arr.append(nums[i])             #append new num elemement in this array
            res.append(arr.copy())
        begin=resSize                #update begin with previous size of res, cause if we encounter duplicate in next loop iteration we will skip res size and then add another elements
    return res  

#Appproach: Iterative Version
#TIme Complexity: O(n*2^n)
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list
#Intuiion: Same as Above just little diff
def subsetsWithDup3(nums):
    res, cur_char, frm, nums = [[]], None, 0,  sorted(nums)
    for n in nums:
        frm, ln = frm if n==cur_char else 0, len(res)
        for ls in res[frm:]:
            res.append(ls + [n])
        cur_char = n
        frm = ln
    
    return res














#4 COmbination Sum 2
#Code that doesnt work and why is explained for branch out each time and make decision for choosing an element or not choosing an element on each recursion
# def combinationSum2(candidates, target):
#     res=[]
#     candidates.sort()   
#     def dfs(list,curIdx,cursum):
#         if cursum>target or curIdx>=len(candidates):    #<- why this doesnt work cause this sort of appraoch we g=et our result when we get out of bound index, 
#                                                         #but you can see thta we are not appending any result when we get out of bound index
#             return
#         if cursum==target:                             #instead we are adding in our result every time when our cursum equals target, but this will make duplicate, 
#                                                         #cause this approach of choosing or not choosing an elemeent provide us wiht result at out of bound index or at very end, 
#                                                         # so we should try checking whther our curSum equal tagrter whnwe become out of bound and then add the list into our result array
#             res.append(list[:])
#         list.append(candidates[curIdx])
#         dfs(list,curIdx+1,cursum+candidates[curIdx])
#         list.pop()
#         while curIdx+1<len(candidates) and candidates[curIdx+1]==candidates[curIdx]:
#             curIdx+=1
#         dfs(list,curIdx+1,cursum)
#         return
#     dfs([],0,0)
#     return res

#Appproach: Recursion Version  (Branch ouot and on each nracnh make decision of choosing or not choosing an element same as Susbet 1 and 2 problem)
#TIme Complexity: O(2^n)
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list
#Things to rememebr:
#1) Always remember that in this sort of approach our end result will be when we get our idx ouit of bound, so try to add your list into res whne w=you get out of bound
#2)try to retunr from recursion if found out that our curSum is greater than target cause it is impossible to have any correct result so avoid it and backtrack to valid solution
def combinationSum2(candidates, target):
    res=[]
    candidates.sort()   
    def dfs(list,curIdx,cursum):
        if cursum>target:                          #<- This is imp, not use it and you will get TLE
            return
        if curIdx>=len(candidates):                   #<- this is imp , not use it and u will not able to capture all result, or you will capture duplicates
            if cursum==target:                         #<-this ensures that end result is equalt o target we then onloy add it in our result and retunr
                res.append(list[:]) 
            return
        
        list.append(candidates[curIdx])
        dfs(list,curIdx+1,cursum+candidates[curIdx])
        list.pop()
        while curIdx+1<len(candidates) and candidates[curIdx+1]==candidates[curIdx]:
            curIdx+=1
        dfs(list,curIdx+1,cursum)
        return
    dfs([],0,0)
    return res


#Appproach: Recursion Version  (Branch out and on the way we add list into result if our sum is equals to target)
#TIme Complexity: O(2^n)
#Space Complexity: O(n) -> in this we ingonred space consumed by res array whihc we retunr at end, we just take O(n) space for list
#Intution:
#Intution is mixture of sumset2 and subset1 along wiht new added condition for checking if cursum equals to target
def combinationSum2(candidates, target):
    res=[]
    candidates.sort()   
    def dfs(list,curIdx,cursum):
        if cursum>target:           #<- This is imp, not use it and you will get TLE
            return
        if cursum==target:         #<-this ensures that end result is equalt o target we then onloy add it in our result, 
                                #here we dont actually return cause we are adding new list into result during traversal itslef, and not waiting for out of bound idx like prevoius solution look above
            res.append(list[:])
        for i in range(curIdx,len(candidates)):
            if i==curIdx or candidates[i]!=candidates[i-1]:           #<-removes duplicates just like problem subset 2
                list.append(candidates[i])
                cursum+=candidates[i]
                dfs(list,i+1,cursum)                           
                list.pop()
                cursum-=candidates[i]
        return
    dfs([],0,0)
    return res


def combinationSum3(candidates, target):
    res=[[]]
    curElement=None
    ans=[]
    for num in candidates:
        if curElement!=num:
            begin=0
        curElement=num
        reslenght=len(res)
        for i in range(begin,reslenght):
            newarr=res[i][:]
            newarr.append(num)
            if sum(newarr)==target:
                ans.append(newarr[:])
            if sum(newarr)<=target:
                res.append(newarr[:])
        begin=reslenght
    return res

combinationSum3([1,2,2],8)