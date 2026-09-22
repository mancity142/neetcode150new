class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)          
        for s in strs:                  
            count=[0]*26              ## array initialized to store upto 26 characters ##
            for c in s:                            # have each character in the word ##
                count[ord(c)-ord('a')]+=1        
            res[tuple(count)].append(s)
        return list(res.values())