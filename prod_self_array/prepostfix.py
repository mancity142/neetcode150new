class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]* (len(nums))
        prefix=1
        for i in range(len(nums)):     # nums=[1,2,3,4]
            result[i]=prefix           # here we have the result and that is 
            prefix*=nums[i]
        postfix=1                                # result =[1,1,2,6] after prefix #
        for i in range(len(nums) -1,-1,-1):      # expected result after postfix=[, , 8,6]
            result[i]*=postfix                   
            postfix*=nums[i]
            
        return result        

