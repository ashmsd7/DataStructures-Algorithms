class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        i=0
        while i<len(seq):
            depth = 0
            curr_str = ""

            while i < len(seq):
                if seq[i] == '(':
                    depth+=1
                
                else:
                    depth-=1
                
                curr_str+=seq[i]
                i+=1

                if depth == 0:
                    break

                
            j = 0
            zeros = 0
            ones = 0
            while j < len(curr_str):
                if curr_str[j] == '(':
                    if zeros <= ones:
                        zeros+=1
                        res.append(0)
                    
                    else:
                        ones+=1
                        res.append(1)

                elif curr_str[j] == ')':
                    if zeros >= ones:
                        zeros-=1
                        res.append(0)
                    
                    else:
                        ones-=1
                        res.append(1)
                j+=1
            
        return res
            
                
                    






        