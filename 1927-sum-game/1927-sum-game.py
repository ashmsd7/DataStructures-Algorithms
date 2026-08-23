class Solution:
    def sumGame(self, num: str) -> bool:
        k = len(num)

        left_q = 0
        right_q = 0

        left_sum = 0
        right_sum = 0
        cnt = 0
        for i in range(k//2):
            if num[i] == '?':
                left_q+=1
                cnt+=1
            else:
                left_sum+=int(num[i])
        for i in range(k//2 , k):
            if num[i] == '?':
                right_q+=1
                cnt+=1
            else:
                right_sum+=int(num[i])

        if cnt %2 !=0 :
            return True
        
        if 2 * (left_sum - right_sum) == 9*(right_q - left_q):
            return False
        return True



        