class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        #Only one letter
        if not s:
            return 0
        
        ans = 1
        count = 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                count = 1
            
            ans = max(ans,count)
        
        #Two distinct letters

        def two_distinct(x,y,forbidden):
            best = 0
            count_x = 0
            count_y = 0
            seen = {0:-1}
            for i , ch in enumerate(s):
                if ch == forbidden:
                    count_x = 0
                    count_y = 0
                    seen = {0:i} # discarding the old hashmap and using a new one as now we are in an entirely different sequence.
                    continue
                
                if ch == x:
                    count_x+=1
                
                else : 
                    count_y+=1
                
                diff = count_x - count_y
                if diff in seen:
                    best = max(best, i - seen[diff])
                else:
                    seen[diff] = i
            
            return best
            
        ans = max(ans,two_distinct('a','b','c'))
        ans = max(ans,two_distinct('a','c','b'))
        ans = max(ans,two_distinct('b','c','a'))
                

        #Three distinct letters
        seen = {(0,0): -1}

        count_a = 0
        count_b = 0
        count_c = 0

        for i , ch in enumerate(s):
            if ch == 'a':
                count_a+=1
            
            elif ch == 'b':
                count_b+=1

            elif ch == 'c':
                count_c+=1
            
            state = (count_a - count_b , count_a - count_c)

            if state in seen:
                length = i - seen[state]
                ans = max(ans,length)
            
            else:
                seen[state] = i
            
        return ans

            


        