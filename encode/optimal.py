class Solution:
    def encode(self, strs: List[str]) -> str:
        res=''                          ## creating a res variable to have string here ##
        for s in str:                   ## iterating in s in strs ##
            res+=len(str)+"#"+s         ## here we are looking for smth like ex:'4#look5#paste'
        return res
    def decode(self,s:str)->List[str]
        res=[]
        i=0
        while i <len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res