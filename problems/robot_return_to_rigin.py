# 657 Robot Return to Origin

import logging

class Solution(object):
    
    def judgeCircle(self, moves:str):
        """
        :type moves: str
        :rtype: bool
        """
        values = {'U': 1, 'D': -1, 'R': 1, 'L': -1}
        pos = [0, 0]

        for move in moves:
            if move in 'LR':
                pos[0] += values[move]
            elif move in 'UD':
                pos[1] += values[move]

        return pos == [0, 0]
    
if __name__ == '__main__':
    executer = Solution()

    result = executer.judgeCircle('LL')
    logging.info(result)