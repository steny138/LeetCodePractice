# 929. Unique Email Addresses

import re
class Solution:
    def numUniqueEmails(self, emails: List[str]):
        
        pattern = re.compile(r"\+.*")
        
        result = {}
        
        for email in emails:
                
            first, domain = email.split('@', 1)
            
            first = pattern.sub('', first).replace('.', '')

            current = f'{first}@{domain}'
            
            result[current] = 1
        
        return len(result)
            