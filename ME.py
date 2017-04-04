import sys, os
list1 = [0.66, 0.93, 1.14, 1.31, 1.47] #replace these with whatever numbers you have for the velocity
m = 67.1 #replace this with the mass 
list_lists = [[(0.2 * m *(x**2)) for x in list1], [(0.5 * m *(y**2))for y in list1]]
ME = [sum(x) for x in zip(*list_lists)]
print (ME)
