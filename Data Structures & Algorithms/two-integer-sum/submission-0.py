class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        i = 0
        arr = [0,0]
        for x in nums:
            y = target-x
            if y in h.keys():
                arr[0] = h[target-x]
                arr[1] = i
            
            else:
                h[x] = i
            i=i+1
        return arr