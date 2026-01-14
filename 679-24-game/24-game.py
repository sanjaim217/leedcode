class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        TARGET = 24.0
        EPS = 0.00000000001
        
        def eq(a, b):
            return abs(a - b) < EPS
        
        def check(p):
            operations = [
                lambda a, b: a + b,
                lambda a, b: a - b,
                lambda a, b: a * b,
                lambda a, b: a / b if abs(b) > EPS else float('inf')
            ]
            
            for o1 in operations:
                for o2 in operations:
                    for o3 in operations:
                        if (eq(o3(o2(o1(p[0], p[1]), p[2]), p[3]), TARGET) or
                            eq(o3(o1(p[0], p[1]), o2(p[2], p[3])), TARGET) or
                            eq(o3(o2(p[0], o1(p[1], p[2])), p[3]), TARGET) or
                            eq(o3(p[0], o2(o1(p[1], p[2]), p[3])), TARGET) or
                            eq(o3(p[0], o2(p[1], o1(p[2], p[3]))), TARGET)):
                            return True
            return False
        
        def permutate(index=0):
            if index == len(permutation):
                return check(permutation)
            for i in range(len(cards)):
                if cards[i] != -1:
                    value = cards[i]
                    permutation[index] = float(value)
                    cards[i] = -1
                    if permutate(index + 1):
                        return True
                    cards[i] = value
            return False
        
        permutation = [0.0] * len(cards)
        return permutate()