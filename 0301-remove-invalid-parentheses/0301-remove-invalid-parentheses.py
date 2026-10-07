class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        remove_left , remove_right , balance = 0 , 0 , 0
        for char in s:
            if char == ')':
                if balance>0:
                    balance-=1
                else:
                    remove_right+=1
            
            elif char == '(':
                balance+=1

            else:
                continue
        
        remove_left = balance
        res = set()

        def dfs(balance,remove_left,remove_right,idx,curr_str):
            if idx == len(s): #Base case
                if balance == 0 and remove_left == 0 and remove_right == 0:
                    res.add(curr_str)
                return

            if s[idx] == '(':
                if remove_left>0:
                    dfs(balance,remove_left-1,remove_right,idx+1,curr_str)

                dfs(balance+1,remove_left,remove_right,idx+1,curr_str+'(')

            elif s[idx] == ')':
                if remove_right >0:
                    dfs(balance,remove_left,remove_right-1,idx+1,curr_str)

                if balance>0:
                    dfs(balance-1,remove_left,remove_right,idx+1,curr_str+')')

            else:
                dfs(balance,remove_left,remove_right,idx+1,curr_str+s[idx])
        
        dfs(0,remove_left,remove_right,0,'')
        return list(res) if len(res)>0 else ['']



        