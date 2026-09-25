class Solution:
    def encode(self, strs: List[str]) -> str:
        res=''
        for s in str:
            res+=len(str)+"#"+s
        return res
    def encode(self,s:str)->List[str]
        res=[]
        i=0
        while i<len(s):
            j=i
            