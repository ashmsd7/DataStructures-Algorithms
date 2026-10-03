class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = 0
        for char in corridor:
            if char == 'S':
                count+=1

        if count == 2:
            return 1
        
        if count %2!=0 or count<2 :
            return 0
        
        MOD = 10**9 + 7

        curr , seats =  0 , 0
        res = 1

        for char in corridor:
            if char == 'S':
                seats+=1

                if seats%2!=0 and seats>2 :
                    res = res*(curr+1) % MOD
                    curr = 0
            
            else:
                if seats>=2 and seats%2==0:
                    curr+=1
        
        return res % MOD
                
        

        

        


        