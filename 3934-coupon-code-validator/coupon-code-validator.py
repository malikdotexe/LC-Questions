class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validcode ={
            "electronics":[],
            "grocery":[],
            "pharmacy":[],
            "restaurant":[]
        }
        for i in range(len(code)):
            if re.fullmatch(r"[A-Za-z0-9_]+", code[i]) and businessLine[i] in validcode and isActive[i]:
                validcode[businessLine[i]].append(code[i])
        res = []
   
        for codes in validcode.values():
            codes.sort()
            for code in codes:
                res.append(code)
        return res

