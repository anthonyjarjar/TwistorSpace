from TwistorClasses.ComplexNumber import ComplexNumber
from TwistorClasses.Quaternion import Quaternion
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

    def compute_distance_matrix(points):
        """Computes the pairwise distance matrix for a list of ProjectivePoints.
        
        Args:
            points (list of ProjectivePoint): List of points for which to compute the distance matrix.
        
        Returns:
            list: A 2D list representing the distance matrix.
        """
        num_points = len(points)
        distance_matrix = [[0] * num_points for _ in range(num_points)]
        for i in range(num_points):
            for j in range(i + 1, num_points):
                distance = points[i].distance_to(points[j])
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance  
        return distance_matrix

