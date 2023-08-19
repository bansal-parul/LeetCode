class Solution:
    def countBinarySubstrings(self, a: str) -> int:
        count = [0,0]
        subs_count = 0
        change = 0
        if a[0] == '0':
            count[0] =1
        else:
            count[1] = 1
        
        for i in range(1, len(a)):
            if a[i] == a[i-1]:
                if a[i] == '0':
                    count[0] = count[0]+1
                else :
                    count[1] = count[1]+1
            else:
                if change == 0:
                    change = 1
                    if a[i] == '0':
                        count[0] = 1
                    else:
                        count[1] = 1
                else:
                    subs_count = subs_count + min(count[0], count[1])
                    if a[i] =='0':
                        count[0] = 1
                    else :
                        count[1] = 1
        subs_count = subs_count + min(count[0], count[1])
        return subs_count 
