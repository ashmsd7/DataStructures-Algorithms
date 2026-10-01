class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        a_count = 1
        res = []
        for word in sentence:
            if word[0] in 'aeiouAEIOU':
                word = word + 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            
            word = word + (a_count)*'a'
            res.append(word)
            a_count+=1
        
        return ' '.join(res)
        

        


        
            


        