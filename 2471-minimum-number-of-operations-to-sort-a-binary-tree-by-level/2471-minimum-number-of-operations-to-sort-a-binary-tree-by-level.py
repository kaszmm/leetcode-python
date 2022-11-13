# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minSwapNeeded(self,temp):
        i=0
        count=0
        hashMap=defaultdict(int)
        sortedTemp=[]
        for i in range(len(temp)):
            hashMap[temp[i]]=i
            sortedTemp.append(temp[i])
        sortedTemp.sort()
        for i in range(len(temp)):
            if temp[i]!=sortedTemp[i]:
                p = hashMap[sortedTemp[i]]
                hashMap[sortedTemp[i]] = i
                hashMap[temp[i]] = p
                temp[i], temp[p]=temp[p], temp[i]
                count+=1          
        return count  
            
            
            
            
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        queue.append(root)
        count=0
        while queue:
            qLength=len(queue)
            temp=[]
            for i in range(0,qLength):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)
              
            count+=self.minSwapNeeded(temp)
        return count
            
                
                
                
                    
                
            
                    