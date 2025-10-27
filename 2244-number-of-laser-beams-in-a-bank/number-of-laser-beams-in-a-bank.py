class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        i=1
        res = 0
        fdevices = bank[0].count("1")
        while i<len(bank):
            sdevices = bank[i].count("1")
            if sdevices>0:
                res += fdevices * sdevices
                fdevices = sdevices
            i+=1
        return res


