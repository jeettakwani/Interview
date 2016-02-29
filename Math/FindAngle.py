__author__ = 'jtakwani'
import math
ab = int(raw_input())
bc = int(raw_input())
hypo = math.sqrt(ab**2 + bc**2)
mb = math.sqrt((2*ab**2 + 2*bc**2 - hypo**2)/4)
angle = math.acos((mb**2 + bc**2 - (hypo/2)**2)/(2*mb*bc))
print(str(int(round(math.degrees(angle)))) + "°")