class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #Hashmap -> To store angles
        Hasher = {'North':0, 'West':1, 'South':2, 'East':3}

        Direction = Hasher['North']
        x , y = 0 , 0

        for instruction in instructions:
            if instruction == 'L':
                Direction+=1
            elif instruction == 'R':
                Direction-=1
            else:
                if Direction == 0:
                    y+=1
                elif Direction == 1:
                    x-=1
                elif Direction == 2:
                    y-=1
                else:
                    x+=1

            Direction%=4

        return (x==0 and y==0) or Direction!=0
        