class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        res=deque()
        res.append("")
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        for digit in digits:
            resLength=len(res)
            for i in range(resLength):
                removedChar=res.popleft()
                for character in digitToChar[digit]:
                    res.append(removedChar+character)
            
        return res