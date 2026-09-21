class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  

        result=defaultdict(list)            ## here creating a result dictionary to hold on to same keys and corresponding strings ##
                          
        for s in strs:                        # movving through the strs to find each s
            sortedS=''.join(sorted(s))        # here we get a string after joining the sorted list
               
            result[sortedS].append(s)         # result = to the key pair append the string to get like {act:["cat"],["tac"]}

        return list(result.values())          # return the values like [["act"],["posts"]]