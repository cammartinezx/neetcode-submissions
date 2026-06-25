class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #space n
        #time n
        score = 0
        points = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                points.pop()
            elif operations[i] == '+':
                points.append(int(points[-2])+int(points[-1]))
                #points.append(int(operations[i-2])+int(operations[i-1]))
            elif operations[i] == 'D':
                points.append(int(points[-1])*2)
            else:
                points.append(int(operations[i]))
        score=sum(points)
        return score

        