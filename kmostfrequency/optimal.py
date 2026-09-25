class Solution:
    def topKFrequent(self,nums:List[int],k:int) -> List[int]:
    count={}                                      ## initializing a hashmap 
    freq=[[] for i in range(len(nums)+1)]         ## sets up bucket sort array over here to have the array set with all numbers to n+1 ## 

    for n in nums:
        count[n]=1+count.get(n,0)                ## here assigns the count for elements as ex: {1:3,2:2} etc
    for n,c in count.items():                    ## here we have the updation taking place in bucket sort array here n is the number and c is count ##
        freq[c].append(n)                         
    res=[]                                       ## creating a empty list to find result ##
    for i in range(len(freq)-1,0,-1):            ## in the bucket sort array moving from the most frequent to lower is desc order ##
        for n in freq[i]:                        ## iteration through the numbers in each frequency[index] ##
            res.append(n)                        ## adding it to result ##
            if len(res)==k:                       ## if length of the elements in res is more than k then reject only till equals it is possible ##
                return res 
              

                      