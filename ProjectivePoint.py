from sympy import cos, sin
from math import radians
from ComplexNumber import ComplexNumber
from Quaternion import Quaternion

class ProjectivePoint:
    def __init__(self, w: ComplexNumber, x: ComplexNumber, y: ComplexNumber, z: ComplexNumber):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print("Projective Point:")
        print(f"w: ({self.w.rel} + {self.w.img}i), x: ({self.x.rel} + {self.x.img}i), "
              f"y: ({self.y.rel} + {self.y.img}i), z: ({self.z.rel} + {self.z.img}i)")

    def scale(self, scale_factor: float):
        self.w = ComplexNumber(self.w.rel * scale_factor, self.w.img * scale_factor)
        self.x = ComplexNumber(self.x.rel * scale_factor, self.x.img * scale_factor)
        self.y = ComplexNumber(self.y.rel * scale_factor, self.y.img * scale_factor)
        self.z = ComplexNumber(self.z.rel * scale_factor, self.z.img * scale_factor)

    def to_affine(self):
        if self.w.magnitude() != 0:
            self.x = self.x.divide(self.w)
            self.y = self.y.divide(self.w)
            self.z = self.z.divide(self.w)
            self.w = ComplexNumber(0, 0) 
        else:
            raise ValueError("Point at infinity; cannot convert to affine coordinates.")
        
    def rotate(self, quaternion: Quaternion):
        """Rotate this projective point using a quaternion."""
        point_quat = Quaternion(0, self.x.rel, self.y.rel, self.z.rel)
        
        rotated_quat = quaternion.multiply(point_quat).multiply(quaternion.inverse())

        self.x = ComplexNumber(rotated_quat.x, 0)
        self.y = ComplexNumber(rotated_quat.y, 0)
        self.z = ComplexNumber(rotated_quat.z, 0)

class ProjectiveLine:
    def __init__(self, point_a: ProjectivePoint, point_b: ProjectivePoint):
        self.point_a = point_a
        self.point_b = point_b

    def cross_product(self, a: ProjectivePoint, b: ProjectivePoint) -> ProjectivePoint:
        w = a.x.multiply(b.y).subtract(a.y.multiply(b.x))
        x = a.y.multiply(b.z).subtract(a.z.multiply(b.y))
        y = a.z.multiply(b.w).subtract(a.w.multiply(b.z))
        z = a.w.multiply(b.x).subtract(a.x.multiply(b.w))

        return ProjectivePoint(w, x, y, z)

    def intersect(self, other_line: "ProjectiveLine") -> ProjectivePoint:
        return self.cross_product(self.point_a, other_line.point_a)
    
    def rotate(self, quaternion: Quaternion):
        """Rotate the line by applying the quaternion rotation to both defining points."""
        self.point_a.rotate(quaternion)
        self.point_b.rotate(quaternion)



def spacetime_to_twistor(t, x, y, z) -> ProjectivePoint:
    omega_1 = ComplexNumber(x, y)
    omega_2 = ComplexNumber(t + z, 0) 
    
    pi_1 = ComplexNumber(1, 0) 
    pi_2 = ComplexNumber(0, 1) 

    return ProjectivePoint(omega_1, omega_2, pi_1, pi_2)

point = spacetime_to_twistor(1, 2, 4, 5)


point_a = ProjectivePoint(ComplexNumber(1, 0), ComplexNumber(2, 3), ComplexNumber(3, 1), ComplexNumber(4, -1))
point_b = ProjectivePoint(ComplexNumber(0, 1), ComplexNumber(1, 0), ComplexNumber(-1, 2), ComplexNumber(3, 4))

point_c = ProjectivePoint(ComplexNumber(1, -1), ComplexNumber(0, 2), ComplexNumber(1, 3), ComplexNumber(-2, 1))
point_d = ProjectivePoint(ComplexNumber(2, 1), ComplexNumber(-1, 3), ComplexNumber(3, 1), ComplexNumber(0, 1))

line1 = ProjectiveLine(point_a, point_b)
line2 = ProjectiveLine(point_c, point_d)

intersection_point = line1.intersect(line2)
# intersection_point.display()

angle = 90  
rotation_quat = Quaternion(cos(radians(angle) / 2), 0, sin(radians(angle) / 2), 0)

point_a = ProjectivePoint(ComplexNumber(1, 0), ComplexNumber(2, 3), ComplexNumber(3, 1), ComplexNumber(4, -1))
point_b = ProjectivePoint(ComplexNumber(0, 1), ComplexNumber(1, 0), ComplexNumber(-1, 2), ComplexNumber(3, 4))

line = ProjectiveLine(point_a, point_b)

line.rotate(rotation_quat)

print("Rotated Line Points:")
line.point_a.display()
line.point_b.display()

