class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        for i in range(len(s)):
            c = s[i]
            if c not in first:
                first[c] = i
            
            last[c] = i

        ##def helper(string):
        #    for i in range(len(string)):
        #        char = string[i]
        #        if string.count(char) != len(hasher[char]):
        #            return False
        ##    return True
        
        def get_intervals(start):
            end = last[s[start]]

            p = start

            while p<=end:
                c = s[p]
                if first[c] < start :
                    return None
                
                end = max(last[c],end)

                p+=1
            
            return (start , end)
        
        candidates = []

        for i in range(len(s)):
            start = i
            interval = get_intervals(start)

            if interval:
                st , en = interval
                candidates.append((st,en))
            
        candidates.sort(key = lambda x:x[1])

        ans = []
        prev_end = -1

        for start , end in candidates:
            if start > prev_end:
                ans.append(s[start:end+1])
                prev_end = end

        return ans




        

                





                





        