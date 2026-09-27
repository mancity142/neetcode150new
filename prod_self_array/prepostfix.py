class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]* (len(nums))
        prefix=1
        for i in range(len(nums)):     # nums=[1,2,3,4]
            result[i]=prefix           # here we have the result and that is basically equal to prefix at first pass #
            prefix*=nums[i]            # here we increment the prefix to be the product of nums before that
        postfix=1                                # result =[1,1,2,6] after prefix #
        for i in range(len(nums) -1,-1,-1):      # expected result after postfix=[24, 12, 8, 6] #
            result[i]*=postfix                   # here the second pass result array need to hae the prefix elements there to be multiplied with postfix eleements #
            postfix*=nums[i]                   # postfix also same as prefix in reverse order 
            
        return result        

