#2461. Maximum Sum of Distinct Subarrays With Length K
#Approach Sliding Window Approach
#TIme COmplexity: O(n)
#Space Complexity: O(n)
def maximumSubarraySum(nums, k: int) -> int:
        if k==1:
            return max(nums)
        start=0
        end=start
        curSum=0
        maxSum=0
        freqDict={}
        while start<=len(nums)-k:
            window=end-start
            while window<k and start<=len(nums)-k:           #if Window is less than k and oour start is not out of bound(here out of bound means start should not cross len(arr)-k)
                if nums[end] not in freqDict or freqDict[nums[end]]==0:   #if our end which is also our current value whihc will be added in our window is not in dict or its freq is 0 means it is unique and not available in our subarray 
                    freqDict[nums[end]] = 1          #increment the freq for end value 
                    curSum+=nums[end]                #incremnt our cursum cause our window is icreased by one more element
                    end+=1                          #shift our end point to next value now
                else:                                #if current end value is already in our subarray present and it's a duplciate then we decremnt our window from start 
                    curSum-=nums[start]                       #decrement our cursum cause we shift our start pointer to remove that duplciate value in our subarray
                    freqDict[nums[start]]-=1                  #decremnt freq for start
                    start+=1                                 #shift start
            if window==k:                      #if our window is of k length then update our max Subarray if needed
                maxSum=max(curSum,maxSum)                     
            
            #shrink window
            curSum-=nums[start]                      #we need to decremtn our window in order to check for next possible max subarray sum
            freqDict[nums[start]]-=1
            start+=1
        return maxSum   
            