class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        ori=[0,0]
        temp=[0,0]

        for move in moves:
            if move=="U":
                temp[1]+=1
            elif move=="D":
                temp[1]-=1
            elif move=="L":
                temp[0]+=1
            elif move=="R":
                temp[0]-=1

        return ori==temp
            