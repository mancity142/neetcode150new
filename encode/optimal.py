class Solution:
    def encode(self, strs: List[str]) -> str:
        res=''                          ## creating a res variable to have string here ##
        for s in str:                   ## iterating in s in strs ##
            res+=len(str)+"#"+s         ## here we are looking for smth like ex:'4#look5#paste'
        return res
    def decode(self,s:str)->List[str]
        res=[]                           ## here creating a case where we have the res stored as a list ##
        i=0                              ## setting pointers i =0 for start of the string
        while i <len(s):                  # checking condition if i goes out of the len (of s) 
            j=i                           # initilly in same position i,j
            while s[j]!='#':                # here we have the case where the s[j] !='#' then move j=j+1
                j+=1
            length=int(s[i:j])              # we require 
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res