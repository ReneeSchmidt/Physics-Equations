import sys,os
m = 67.1 #mass
g = 9.8 #gravity
list1 = [0.062, 0.099, 0.132, 0.165, 0.200] #heights
PE = [m * g * x for x in list1]
print (PE)
