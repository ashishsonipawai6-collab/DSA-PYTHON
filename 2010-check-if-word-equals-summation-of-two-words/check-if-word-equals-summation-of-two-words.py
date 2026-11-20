class Solution(object):
    def getvalue(self, Word):
    
        value = ""
        
        for ch in Word:
            ord(ch) - ord('a')
            value += str(ord(ch) - ord('a'))
        return int(value)

    def isSumEqual(self, firstWord, secondWord, targetWord): 

        a =  self. getvalue(firstWord)
        b =  self.getvalue(secondWord)
        c =  self.getvalue(targetWord)

        return a + b == c

       
        