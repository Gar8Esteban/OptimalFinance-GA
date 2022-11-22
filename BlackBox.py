from collections import defaultdict
import numpy as np


class BlackBox:

    def transfers(self, transactions: list[list[int]]) -> int:
        score = defaultdict(int)
        
        for f, t, a in transactions:
            score[f] -= a
            score[t] += a

        positives = [v for v in score.values() if v > 0]
        negatives = [v for v in score.values() if v < 0]
        
        def recurse(positives, negatives):
            enablePass = len(positives) + len(negatives)
            if enablePass == 0:
                return 0
            
            negative = negatives[0]
            
            count = np.inf
            for positive in positives:
                
                newPositives = positives.copy()
                newNegatives = negatives.copy()
                
                newPositives.remove(positive)
                newNegatives.remove(negative)
                
                if positive == abs(negative):
                    pass
                elif positive > abs(negative):
                    newPositives.append(positive+negative)
                else:
                    newNegatives.append(positive+negative)
                    
                count = min(count, recurse(newPositives, newNegatives))
                
            return count + 1
        
        return recurse(positives, negatives)


if __name__ == '__main__':
    moves = [[0, 1, 10], 
             [1, 2, 1],
             [1, 2, 5],
             [2, 0, 5]]
    
    movesTest = [[0, 1, 10],
                 [2, 0, 5]]
    
    movesTest2 = [[0, 1, 10],
                  [1, 0, 5],
                  [3, 1, 5],
                  [2, 3, 12],
                  [0, 2, 9],
                  [2, 0, 5],
                  [0, 3, 11]]
    print(BlackBox().transfers(movesTest2))
   

    