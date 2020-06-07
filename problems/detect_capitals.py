# 520 Detect Capitals

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or  word == word.lower():
            return True
        
        if word[:1].upper() + word[1:].lower() == word:
            return True
        
        return False