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
        if not isinstance(point_a, ProjectivePoint) or not isinstance(point_b, ProjectivePoint):
            raise TypeError("Both endpoints must be instances of ProjectivePoint")
        
        self.point_a = point_a
        self.point_b = point_b

    def display(self):
        """Displays the components of the ProjectiveLine by showing the two points."""
        print("Projective Line:")
        print("Point A:")
        self.point_a.display()
        print("Point B:")
        self.point_b.display()

    def cross_product(self, a: ProjectivePoint = None, b: ProjectivePoint = None) -> ProjectivePoint:
        """Calculates the cross product of two points to find the intersection line.
        
        Args:
            a (ProjectivePoint): The first projective point. Defaults to point_a.
            b (ProjectivePoint): The second projective point. Defaults to point_b.
        
        Returns:
            ProjectivePoint: The resulting projective point from the cross product.
        """
        if a is None:
            a = self.point_a
        if b is None:
            b = self.point_b

        w = a.x * b.y - a.y * b.x
        x = a.y * b.z - a.z * b.y
        y = a.z * b.w - a.w * b.z
        z = a.w * b.x - a.x * b.w
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
        tolerance = 1e-10
        return not (abs(intersection.w.magnitude()) < tolerance and abs(intersection.x.magnitude()) < tolerance 
                    and abs(intersection.y.magnitude()) < tolerance and abs(intersection.z.magnitude()) < tolerance)

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
        
        Raises:
            ValueError: If transformation_matrix is not a valid 4x4 matrix.
        """
        if len(transformation_matrix) != 4 or any(len(row) != 4 for row in transformation_matrix):
            raise ValueError("Transformation matrix must be 4x4")
        
        self.point_a = self.point_a.apply_transformation(transformation_matrix)
        self.point_b = self.point_b.apply_transformation(transformation_matrix)
