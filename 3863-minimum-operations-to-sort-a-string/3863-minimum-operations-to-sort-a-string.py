class Solution:
    def minOperations(self, s: str) -> int:

        #lets base solution on one test case that is 'edcba' worst case

        #if len is 2 then we check if sorted or not 

        if len(s) == 2:
            return 0 if s[0] <= s[1] else -1
        
        #answer can only be in these numbers -> {-1,0,1,2,3}

        #'edcba' -> sort first 4 -> bcdea -> last 4 -> bacde -> first 2 -> abcde . so at max it is 3.

        small = min(s)
        large = max(s)
        sort = True

        for i in range(1,len(s)):
            if s[i] < s[i-1] :
                sort = False
        
        
        #if any one of those are fixed it means we can sort prefix or suffix in 1 iteration .

        if large == s[-1] or small == s[0] :
            if sort:
                return 0
            else:
                return 1


        #Now how to deal with 2 or 3 condition.. 

        #Okay, so we check if any of the large or small is at opposite endpoint.

        #If yes, then answer is 3, because we cannot sort BOTH extremes in iteration and instead need to put 1 extra sort. 

        if any(small == s[i] or large == s[i] for i in range(1,len(s)-1)):
            return 2
        return 3

        #Good question 




        


        