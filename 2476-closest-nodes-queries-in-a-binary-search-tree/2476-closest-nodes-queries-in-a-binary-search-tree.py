# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            temp.append(node.val)
            traverse(node.right)
        
        traverse(root)
        
        for query in queries:
            minVal=-1
            maxVal=-1
            left=0
            right=len(temp)-1
            while left<=right:
                mid=(left+right)//2
                if temp[mid]==query:
                    minVal=temp[mid]
                    maxVal=temp[mid]
                    break
                if temp[mid]>query:
                    right=mid-1
                else:
                    left=mid+1
    
            if temp[mid]<query:
                minVal=temp[mid]
                maxVal=temp[mid+1] if mid+1<len(temp) else -1
            elif temp[mid]>query:
                maxVal=temp[mid]
                minVal=temp[mid-1] if mid-1>=0 else -1
            res.append([minVal,maxVal])
        return res
                
            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
               
                    
                    
            
                    