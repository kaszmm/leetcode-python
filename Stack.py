from typing import List

#7

#The Intuition behind this solution is little intuitive  (NEETCODE EXPLAINED IT WELL)
#so we are gonna use monotonic increasing stack, why? hmmm let's talk about it
#we are start iterateing over every height in our heights arr and on wach ietration we check if the curretn height is less than top height of our stack
# if it is less than top of stack than we need to pop elements in stack till our current heights is greatee than top of stack
#but before poping elements from stack we need to calculate the area of element that we poping from stack
#so when popping we measure the area with formula (currentIdx-stackIdx)*stackHeight  [here stackIdx is idx on top of stack and stackHeihgt is height of top elment in stack]
#Now here is more intuitive part so when we pop element and measure the area of that popped element we need to keep track of idx of last element we popped from stack
#why? because let say we have 3,4,5 in our stack where 5 is top on element and its idx is let say 2 so when our current is height is 1 and idx=4 which is smaller than top of our stack
#we pop 5 (idx:2,val:5) , now top is (idx:1,val:4) which is also smaller than 1 so we calculate area adn pop this anow we have (idx:0,val:3) which is smaller than 1 so we calculate area
# and pop 3 as well
# now hear this so inserting 1 in to stack we insert (idx:0,val:1) instead of (idx:4,val:1) why? cause 1 is smaller than 3 so one can extend 1 backward till the index of 3(idx:0)
#because 1 is smaller than 3,4,5, means for element 1 we can make rectangle streach from current idx till index of 3 cause 1 is smaller than 3,4,5
#that is main intuition behind this solution we will only insert idx in stack till which we can extend our rectangle backwards

def largestRectangleArea(heights) -> int:
        maxArea=0
        stack=[]
        for i,h in enumerate(heights):
            start=i      #this start is index whihc we append in stack and when we go into while loop this start will get updated to last popped element in stack
            while stack and stack[-1][1]>h:
                idx, height= stack.pop()
                maxArea= max(maxArea, height*(i-idx))
                start=idx    #update our start to current popped element index
            stack.append((start,h))
            
        #there is possibilitiy than some elements wtill lets in stack, what are those element? this are elements which were able to extend till end of array like 3,4,5
        #in this we never need to pop any element in stack and we just append element in stack, so all 3,4,5 ablt to extend till end of array, so just calculate there area
        #from there current index till lenght of array
        for i,h in stack:
            maxArea=max(maxArea,h*(len(heights)-i))
            
        return maxArea
    
    

arr=[2,1,5,6,2,3]
largestRectangleArea(arr)