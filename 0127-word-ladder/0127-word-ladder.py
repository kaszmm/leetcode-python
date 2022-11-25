class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)
        if endWord not in wordSet:
            return 0
        queue=deque()
        visited=set()
        res=0
        queue.append(beginWord)
        visited.add(beginWord)
        isConverted=False
        while queue:
            res+=1
            for i in range(len(queue)):
                curWord=queue.popleft()
                if curWord==endWord:
                    return res
                for j in range(len(curWord)):
                    for k in range(97,123):
                        newWord=curWord[:j]+chr(k)+curWord[j+1:]
                        if newWord in wordSet and newWord not in visited:
                            queue.append(newWord)
                            visited.add(newWord)
        return 0