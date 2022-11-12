

from collections import deque
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#1 
#Approach: Bottom Up Recrusion
#Time COmplexity:O(n)
#Space Complexity:O(n) because of recursion call stack
#Intuition is we calculate max depth from left side and max depth from right side and we caulculate those left and right depth and update our res if our res is less than it
#Now why left+right? becuase left+right is our diamter
def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res=0
        def calculateDiameter(root):
            if root is None:                #for edge case like [1,2] when on left side of 1 is 2 but on right side is null , so when we encounter root to be null we return -1 cause we need to balacne out the +1 we add after each recurion call
                return -1
            if (root.left is None and root.right is None):     #this condition is redundant just remove it the code will stiull work, btw this condition is when we encounter node wiht no left and right nodes
                return 0
            leftEdge= 1+calculateDiameter(root.left)   #we do 1+ because when there is no left and right element in root we return 0, but edge from this root to its recurive parent is 1 so use 1+
            rightEdge= 1+calculateDiameter(root.right)
            self.res= max(self.res,leftEdge+rightEdge)   #update max diameter
            return (max(leftEdge,rightEdge))            #return mac depth of left or right
        
        calculateDiameter(root)
        return self.res


#2 Balanced binary tree
#Approach: same as appraoch from above solution
#Time COmplexity:O(n)
#Space Complexity:O(n) because of recursion call stack
#Things to Rememeber the balacned tree here means is diff for this question please understand properly before proceeding to code
#We just get get get max difference from elft and right sub trees and if the diff is greater than 1 means it is not balanced
def isBalanced(self,root:TreeNode):
    self.res=0
    def calculateHeight(root):
        if root is None:
            return -1
        leftHeight=1+calculateHeight(root.left)
        rightheight=1+calculateHeight(root.right)
        self.res= max(self.res,abs(leftHeight-rightheight))
        return 1+max(leftHeight,rightheight)
    calculateHeight(root)
    return self.res<=1


#Second Approach
#here we return [bool,height] bool states that whther the sub tree or tree itself is valid of not
def OthIsBalanced(self,root:TreeNode):
    def dfs(root):
        if root is None:
            return [True,0]   #here why when we encounter null root we return 0 instead -1, cause in previous approach the calculation matters, cause our checking for whther tree is valis or not is based on our height diff calculations
                              #S0 in scenarios like [1,null,2] we need to retunrn -1 cause we add +1 to every recursion call stack in prev question, but here we dont do that +1 thing on every recurison call stack  
        leftHeight=dfs(root.left)
        rightHeight=dfs(root.right)
        balanced= abs(leftHeight[1]-rightHeight[1])<=1 and leftHeight[0] and rightHeight[0]   #we check first whether out left and right sub tree is valid or not ,
                                                                                         #once they are valid we check diff of left and right sub tree,
                                                                                         #  cause we need to check for root node itself whther the root is valid or not in each recursion
                                                                                         #so we also take diff of elft and right sub tree in it.
        return [balanced,1+max(leftHeight[1],rightHeight[1])]
    res=dfs(root)
    return res[0]



#3 Binary Tree Right Side View
#Approach: BFS Approach
#TIme COmplexity: ??
#Space COmplexity:O(n)
#Things to Remember: We are not adding any null nodes in queue so we dont need to check for null nodes
#Intuition:
#So we are doing this in BFS cause we have have to add the right most side node in our result on each level, and BFS is level order travseral
#so doing BFS is easier for this problem, so start ietrating and on each ietration we atke lenght of queue and based on that length we loop and pop and append nodes in queue
#so why this length of quue? cause remember we are doing level order so on each level we need to pop and ppend all the elements on that level so on level-2 (level-1 start from root node)
#we have only one length of queue so we add left and right from node whihc we popped form queue, but on level-3 we have 2 nodes so we pop and append two times in queue
#now once we know how to traver in order fashion we take a variable that will be updated when left is not null or right is not null, now doing that our variable will alwasy have node val
#which is right most side every time, and we just add that variable in our res
def rightSideView(root:TreeNode):
        if not root:
            return []
        queue=deque()
        queue.append(root)
        res=[]
        res.append(root.val)
        while len(queue)>0:
            qLength=len(queue)
            nodeInSight=None
            for i in range(0,qLength):
                treeNode=queue.popleft()
                if treeNode.left:
                    nodeInSight=treeNode.left.val
                    queue.append(treeNode.left)
                if treeNode.right:
                    nodeInSight=treeNode.right.val
                    queue.append(treeNode.right)
            if nodeInSight!=None:    #this is needed cause let say we have [1,2,3,4,5,6,7] so first we add 2,3 then 45,67 now we also try to loop for 4,5,6,7 which are leaf nodes in tree, on that scenario our nodeInSight value will remain None so dont add that to our res
                res.append(nodeInSight)
        return res

#Second Approach: BFS
#TIme COmplexity: ??
#Space COmplexity:O(n)
#Things to Remember: We are adding any null nodes in queue so we need to check for null nodes
#Intuition: Same as above just in here we add null in queue and then we handle it
def rightSideView(root:TreeNode):
        if not root:
            return []
        queue=deque()
        queue.append(root)
        res=[]
        while len(queue)>0:
            qLength=len(queue)
            rightSide=None
            for i in range(0,qLength):
                treeNode=queue.popleft()
                if treeNode:
                    rightSide=treeNode
                    queue.append(treeNode.left)
                    queue.append(treeNode.right)
            if rightSide!=None:
                res.append(rightSide.val)
        return res

#Thirs Approach: DFS
#TIme COmplexity: O(n)
#Space COmplexity:O(n)
#Things to Remember: We are adding any null nodes in queue so we need to check for null nodes
#Intuition: The solution is quite smart, so our level starts from 0..n
#now we start from level 0 we have 0 element in our result list so our levela nd size of result is same so we append that node to res
#NOW we travser first to right of that node then traverse left of that node, now on each level once we add node in our res, our len(res)>level due to this remaining nodes on that same level are inegligible to be added in our res, so we move to next level
def rightSideView(root:TreeNode):
        if not root:
            return []
        res=[]
        def Dfs(node,level):
            if not node:
                return
            if len(res)==level:
                res.append(node.val)
            Dfs(node.right,level+1)    #first go to right, cause we need to add the right most element first
            Dfs(node.left,level+1)
            return
        Dfs(root,0)
        return res



#4 Count Good Nodes in Binary Tree
#TIme Complexity:O(n)
#Space Complexity:O(log(n))
#Things To Rememeber:
#1) Good Node means any node whihc we encounter if that node is greater than or equal to max value we encountered while reaching this node then that node is good node
#2)In solution we are passing the maxval, but remember that maxval is not permamnently updated but it returns back to original value once the call stack pop the recursive call one after the other
#Intuition:
#We we use global variable to get count of good nodes
#we check in our dfs recursive function if node is greater than or equal to maxVal than we we knwo we encountered a good node so we increment our global counter by 1 
#and aslo we update our maxval to that current node
def goodNodes(self,root: TreeNode) -> int:
    self.numOfGoodNodes=0
    def DfsCountGoodNodes(self,node:TreeNode,maxVal:int)->None:
        if not node:
            return
        if maxVal<=node.val:
            self.numOfGoodNodes+=1
            maxVal=node.val
        DfsCountGoodNodes(self,node.left,maxVal)
        DfsCountGoodNodes(self,node.right,maxVal)
        return
    DfsCountGoodNodes(self,root,root.val)
    return self.numOfGoodNodes

#Approach: Same Approach but in this we dont use any global variable
#TIme Complexity:O(n)
#Space Complexity:O(log(n))
#intuition: Intuition is same as above just we dont use any global variable, now when we encounter that current node is >=maxVal then we make our res=1 ,
#we use that to recursively sum all the good nodes and we use += for left and right measn we add what ever values we get from elft and right tree and return res at end
def OthgoodNodes(root: TreeNode) -> int:
    def DfsCountGoodNodes(node:TreeNode,maxVal:int)->None:
        if not node:
            return 0
        if maxVal<=node.val:
            res=1
            maxVal=node.val
        else:
            res=0
        res+=DfsCountGoodNodes(node.left,maxVal)
        res+=DfsCountGoodNodes(node.right,maxVal)
        return res
    return DfsCountGoodNodes(root,root.val)

#Approach: Iterative BFS Approach 
#TIme Complexity:O(n)
#Space Complexity:O(log(n))
#Intuition: Here we use dequeue and intitally add root and set max to root.val cause  root is alwasy good node so we can set max to root.val
#we pop element from queue we get node and max value from that
#now we dont want to modify our max value cause in this iterative solution there is no recurison stack so here once we modify our max we are fucked 
#cause if max is from left tree it will then pollute our right side of tree
#so what check curMax and node val is node val is greater than we increment count
#and we add the left and rihgt node in queue along wiht node we also add max from curMax and node val
def OthgoodNodes2(root: TreeNode) -> int:
    queue=deque()
    queue.append([root,root.val])
    count=0
    while queue:
        node,maxval=queue.popleft()
        if maxval<=node.val:
            count+=1
        if node.left:
            queue.append([node.left,max(maxval,node.left.val)])
        if node.right:
            queue.append([node.right,max(maxval,node.right.val)])
    return count
treeN=TreeNode(val=2,right=TreeNode(val=4,left=TreeNode(val=10),right=TreeNode(val=8,left=TreeNode(val=4))))     
obj=OthgoodNodes2(treeN)