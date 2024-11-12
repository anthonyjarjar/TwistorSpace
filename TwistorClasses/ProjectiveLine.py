from TwistorClasses.Quaternion import Quaternion
from TwistorClasses.ProjectivePoint import ProjectivePoint
from math import acos

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
    
    def intersect_bool(self, other_line: "ProjectiveLine") -> bool:
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
