class Solution:
    def topKFrequent(self,nums:List[int],k:int) -> List[int]:
    count={}                                      ## initializing a hashmap 
    freq=[[] for i in range(len(nums)+1)]         ## sets up bucket sort array over here to have the array set with all numbers to n+1 ## 

    for n in nums:
        count[n]=1+count.get(n,0)                ## here assigns the count for elements as ex: {1:3,2:2} etc
    for n,c in count.items():
        freq[c].append(n)   
    res=[]
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res)==k:
                return res 
              

                      