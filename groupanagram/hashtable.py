class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)          
        for s in strs:                  
            count=[0]*26              ## array initialized to store upto 26 characters ##
            for c in s:                            # have each character in the word ##
                count[ord(c)-ord('a')]+=1        
            res[tuple(count)].append(s)      # here count is a list of 26 characters ex: [1,0,0,0,,0,,0,....] upto 26 and act as key here and to make it inmutable we use tuple ##
        return list(res.values())

    