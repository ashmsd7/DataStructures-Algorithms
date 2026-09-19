class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        #Really hard intutiton, i mean the complex part was to figure out how to find the closest point on the rectangle from the circle's centre but figured it.

        closest_x = max(x1,min(xCenter,x2))
        closest_y = max(y1,min(yCenter,y2))

        point = (closest_x,closest_y) #This is the point that is on the rectangle thats closest to the circle's centre.

        #Now we compare it with the radius of the circle. If it's less than the radius it means its inside the circle's diameter which results in an overlap.

        distance = (closest_x - xCenter) ** 2 + (closest_y - yCenter) ** 2

        if distance<=radius*radius:
            return True
        else:
            return False




        