class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        
        for r in set(ranks):
            if ranks.count(r)>=3:
                return "Three of a Kind"        

        for r in set(ranks):
            if ranks.count(r)>=2:
                return "Pair"
        
        return "High Card"
        