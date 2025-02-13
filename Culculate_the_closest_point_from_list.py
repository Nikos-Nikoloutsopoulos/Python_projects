#Using the Pythagorio Theorima calculates the best distance from a point
import math

our_point=(1,1)
point_list=[(2,2),(5,6),(4,0),(-2,1),(3,1)]

#calculate the distance between two points
def culculate_distance (point1,point2):
    x1,y1 =point1
    x2,y2 =point2

    dx=math.pow(x2-x1,2)
    dy=math.pow(y2-y1,2)

    return math.sqrt(dx+dy)

#initialize the closest distance and the closest point

closest_distance = float('inf')
closeest_point = None

#Iterarte the list with the points to find the closest
for point in point_list:
    current_distance = culculate_distance(our_point,point)
    if current_distance < closest_distance:
        closest_distance =current_distance
        closeest_point = point
print(f"The closest distance is: {closest_distance}")        
print(f"The closest point is: {closeest_point}")   