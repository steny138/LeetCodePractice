# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        answer = ""
        
        minLen = min(len(ele) for ele in strs)

        for a in range(minLen):
            temp = strs[0][a]
            
            if all(temp == item[a] for item in strs):
                answer += temp
            else:
                return answer

        return answer
                