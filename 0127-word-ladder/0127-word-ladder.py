class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj=defaultdict(list)
        visited=set()
        queue=deque()
        
        queue.append(beginWord)
        wordList.append(beginWord)
        visited.add(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                newWord=word[:i]+"*"+word[i+1:]
                adj[newWord].append(word)
        res=0    
        while queue:
            res+=1
            for i in range(len(queue)):
                curWord=queue.popleft()
                if curWord==endWord:
                    return res
                for j in range(len(curWord)):
                    newWord=curWord[:j]+"*"+curWord[j+1:]
                    for neighbor in adj[newWord]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
        return 0
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
    
    