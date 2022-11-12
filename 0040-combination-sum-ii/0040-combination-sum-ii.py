class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[[]]
        curElement=None
        ans=[]
        candidates.sort()
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
        return ans