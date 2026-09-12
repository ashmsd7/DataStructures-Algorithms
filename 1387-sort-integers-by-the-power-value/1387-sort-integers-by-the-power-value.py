class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {1:0}

        def simplify(number):
            steps = 0
            if number in dic:
                return dic[number] + steps
            
            num = number

            while number not in dic:
                if number%2 == 0:
                    number = number //2
                else:
                    number = number *3 + 1
                steps+=1
            dic[num] = dic[number]+ steps
            return dic[num]

        res = [0] * (hi-lo+1)

        for i in range(0,hi-lo+1):
            number = lo + i
            res[i] = [number,simplify(number)]
        
        res = sorted(res,key = lambda x:(x[1],x[0]))
    
        return res[k-1][0]



            


        