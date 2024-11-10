from TwistorClasses.TwistorMapping import spacetime_to_twistor
from TwistorClasses.ProjectiveLine import ProjectiveLine
from TwistorClasses.Quaternion import Quaternion
from sympy import cos, sin
from math import radians

point1 = spacetime_to_twistor(1, 1, 1, 1)
point2 = spacetime_to_twistor(2, 2, 2, 2)

print("Twistor Point 1:")
point1.display()
print("Twistor Point 2:")
point2.display()

line = ProjectiveLine(point1, point2)
print("Line formed between Twistor Points 1 and 2.")

angle = 45
rotation_quat = Quaternion(cos(radians(angle) / 2), 0, sin(radians(angle) / 2), 0)

line.rotate(rotation_quat)

print("Rotated Twistor Points:")
line.point_a.display()
line.point_b.display()
