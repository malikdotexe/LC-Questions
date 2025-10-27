class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i=1
        res = 0
        fdevices = len([x for x in bank[0] if x=="1"])
        while i<len(bank):
            sdevices = len([x for x in bank[i] if x=="1"])
            if sdevices>0:
                res += fdevices * sdevices
                fdevices = sdevices
            i+=1
        return res


