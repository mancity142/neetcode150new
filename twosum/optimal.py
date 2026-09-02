class Solution:
    from types import list
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmaps={}
        for i,n in enumerate(nums): # enumerate used as counter 
            diff=target-n
            if diff in prevmaps:
                return [prevmaps[diff],i]
            prevmaps[n]=i    # hashmap the values are indexed
        return

            