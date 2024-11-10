from ComplexNumber import ComplexNumber
from Quaternion import Quaternion
from math import acos

class ProjectivePoint:
    """Represents a point in projective space using homogeneous coordinates."""

    def __init__(self, w: ComplexNumber, x: ComplexNumber, y: ComplexNumber, z: ComplexNumber):
        """Initializes a ProjectivePoint with ComplexNumber components for w, x, y, and z.
        
        Args:
            w (ComplexNumber): The w component in homogeneous coordinates.
            x (ComplexNumber): The x component in homogeneous coordinates.
            y (ComplexNumber): The y component in homogeneous coordinates.
            z (ComplexNumber): The z component in homogeneous coordinates.
        """
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        """Displays the components of the ProjectivePoint in a readable format."""
        print("Projective Point:")
        print(f"w: ({self.w.rel} + {self.w.img}i), x: ({self.x.rel} + {self.x.img}i), "
              f"y: ({self.y.rel} + {self.y.img}i), z: ({self.z.rel} + {self.z.img}i)")

    def scale(self, scale_factor: float):
        """Scales the projective point by a real number, preserving conformal structure.
        
        Args:
            scale_factor (float): The factor by which to scale the point.
        """
        self.w = ComplexNumber(self.w.rel * scale_factor, self.w.img * scale_factor)
        self.x = ComplexNumber(self.x.rel * scale_factor, self.x.img * scale_factor)
        self.y = ComplexNumber(self.y.rel * scale_factor, self.y.img * scale_factor)
        self.z = ComplexNumber(self.z.rel * scale_factor, self.z.img * scale_factor)

    def normalize(self):
        """Normalizes the projective point by scaling so that w is 1, if possible."""
        if self.w.magnitude() != 0:
            scale_factor = 1 / self.w.magnitude()
            self.scale(scale_factor)

    def to_affine(self):
        """Converts the projective point to affine coordinates by dividing by w.
        
        Raises:
            ValueError: If the point is at infinity (w = 0).
        """
        if self.w.magnitude() != 0:
            self.x = self.x.divide(self.w)
            self.y = self.y.divide(self.w)
            self.z = self.z.divide(self.w)
            self.w = ComplexNumber(0, 0) 
        else:
            raise ValueError("Point at infinity; cannot convert to affine coordinates.")

    def to_cartesian(self):
        """Converts the projective point to Cartesian coordinates.
        
        Returns:
            tuple: A tuple of (x, y, z) in Cartesian coordinates.
        
        Raises:
            ValueError: If the point is at infinity (w = 0).
        """
        if self.w.magnitude() != 0:
            x = self.x.divide(self.w)
            y = self.y.divide(self.w)
            z = self.z.divide(self.w)
            return (x, y, z)
        else:
            raise ValueError("Point is at infinity in projective space.")

    def distance_to(self, other: "ProjectivePoint") -> float:
        """Calculates a Euclidean-like distance between two projective points.
        
        Args:
            other (ProjectivePoint): The other point to calculate the distance to.
        
        Returns:
            float: The Euclidean-like distance between the two points.
        """
        dx = self.x.subtract(other.x).magnitude()
        dy = self.y.subtract(other.y).magnitude()
        dz = self.z.subtract(other.z).magnitude()
        return (dx**2 + dy**2 + dz**2) ** 0.5

    def angle_with(self, other: "ProjectivePoint") -> float:
        """Calculates the angle between this projective point and another.
        
        Args:
            other (ProjectivePoint): The other projective point to calculate the angle with.
        
        Returns:
            float: The angle between the two projective points in radians.
        """
        dot_product = (self.x.rel * other.x.rel + self.y.rel * other.y.rel + self.z.rel * other.z.rel)
        mag_self = (self.x.magnitude()**2 + self.y.magnitude()**2 + self.z.magnitude()**2) ** 0.5
        mag_other = (other.x.magnitude()**2 + other.y.magnitude()**2 + other.z.magnitude()**2) ** 0.5
        return acos(dot_product / (mag_self * mag_other))

    def rotate(self, quaternion: Quaternion):
        """Applies a quaternion-based rotation to the projective point.
        
        Args:
            quaternion (Quaternion): The rotation quaternion.
        """
        point_quat = Quaternion(0, self.x.rel, self.y.rel, self.z.rel)
        rotated_quat = quaternion.multiply(point_quat).multiply(quaternion.inverse())

        self.x = ComplexNumber(rotated_quat.x, 0)
        self.y = ComplexNumber(rotated_quat.y, 0)
        self.z = ComplexNumber(rotated_quat.z, 0)

class ProjectiveLine:
    """Represents a line in projective space defined by two points."""

    def __init__(self, point_a: ProjectivePoint, point_b: ProjectivePoint):
        """Initializes a ProjectiveLine with two ProjectivePoint endpoints.
        
        Args:
            point_a (ProjectivePoint): The first point defining the line.
            point_b (ProjectivePoint): The second point defining the line.
        """
        self.point_a = point_a
        self.point_b = point_b

    def display(self):
        """Displays the components of the ProjectiveLine by showing the two points."""
        print("Projective Line:")
        self.point_a.display()
        self.point_b.display()

    def cross_product(self, a: ProjectivePoint, b: ProjectivePoint) -> ProjectivePoint:
        """Calculates the cross product of two points to find the intersection line.
        
        Args:
            a (ProjectivePoint): The first projective point.
            b (ProjectivePoint): The second projective point.
        
        Returns:
            ProjectivePoint: The resulting projective point from the cross product.
        """
        w = a.x.multiply(b.y).subtract(a.y.multiply(b.x))
        x = a.y.multiply(b.z).subtract(a.z.multiply(b.y))
        y = a.z.multiply(b.w).subtract(a.w.multiply(b.z))
        z = a.w.multiply(b.x).subtract(a.x.multiply(b.w))
        return ProjectivePoint(w, x, y, z)

    def intersect(self, other_line: "ProjectiveLine") -> ProjectivePoint:
        """Finds the intersection of this line with another line in projective space.
        
        Args:
            other_line (ProjectiveLine): The other line to intersect with.
        
        Returns:
            ProjectivePoint: The intersection point of the two lines.
        """
        return self.cross_product(self.point_a, other_line.point_a)
    
    def intersects(self, other_line: "ProjectiveLine") -> bool:
        """Checks if two lines intersect in projective space.
        
        Args:
            other_line (ProjectiveLine): The other line to check for intersection.
        
        Returns:
            bool: True if the lines intersect, False otherwise.
        """
        intersection = self.intersect(other_line)
        return not (intersection.w.magnitude() == 0 and intersection.x.magnitude() == 0 
                    and intersection.y.magnitude() == 0 and intersection.z.magnitude() == 0)

    def normalize(self):
        """Normalizes the points defining the line, so each has w = 1 if possible."""
        try:
            self.point_a.normalize()
            self.point_b.normalize()
        except ValueError:
            print("One of the points is at infinity; normalization skipped for that point.")

    def rotate(self, quaternion: Quaternion):
        """Applies a quaternion-based rotation to the entire line by rotating both endpoints.
        
        Args:
            quaternion (Quaternion): The rotation quaternion.
        """
        self.point_a.rotate(quaternion)
        self.point_b.rotate(quaternion)

    def apply_transformation(self, transformation_matrix):
        """Applies a projective transformation to both points defining the line.
        
        Args:
            transformation_matrix (list): A 4x4 transformation matrix to apply to each point.
        """
        self.point_a = self.point_a.apply_transformation(transformation_matrix)
        self.point_b = self.point_b.apply_transformation(transformation_matrix)


def spacetime_to_twistor(t, x, y, z) -> ProjectivePoint:
    """Maps a spacetime point (t, x, y, z) to a twistor space ProjectivePoint.
    
    Args:
        t (float): The time coordinate.
        x (float): The x-coordinate in space.
        y (float): The y-coordinate in space.
        z (float): The z-coordinate in space.
    
    Returns:
        ProjectivePoint: A point in twistor space representing the spacetime event.
    """
    omega_1 = ComplexNumber(x, y)
    omega_2 = ComplexNumber(t + z, 0)
    pi_1 = ComplexNumber(1, 0) 
    pi_2 = ComplexNumber(0, 1) 

    return ProjectivePoint(omega_1, omega_2, pi_1, pi_2)

def spacetime_null_direction_to_twistor(t, x, y, z) -> ProjectivePoint:
    """Converts a null direction in spacetime to a twistor point.
    
    Args:
        t (float): The time component of the spacetime point.
        x (float): The x-coordinate in space.
        y (float): The y-coordinate in space.
        z (float): The z-coordinate in space.
    
    Returns:
        ProjectivePoint: A twistor point in projective space representing the null direction.
    """
    
    omega_1 = ComplexNumber(x, y)
    omega_2 = ComplexNumber(t + z, 0)
    pi_1 = ComplexNumber(1, 0)  
    pi_2 = ComplexNumber(0, 1) 

    return ProjectivePoint(omega_1, omega_2, pi_1, pi_2)

