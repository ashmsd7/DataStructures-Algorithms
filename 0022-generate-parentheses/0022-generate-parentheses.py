class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        open_p = 0
        closed_p = 0


        def backtrack(curr_str,open_p,closed_p):
            if len(curr_str) == 2*n:
                res.append(curr_str)
                return

            if open_p < n and open_p >= closed_p:
                backtrack(curr_str + '(',open_p+1,closed_p)
            
            if closed_p < n and open_p >=closed_p:
                backtrack(curr_str + ')',open_p,closed_p+1)


        backtrack('',0,0)
        return res



            






        