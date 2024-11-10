from Quaternion import Quaternion
from math import acos

class VectorRotation:
    """Represents a vector in quaternion form and applies quaternion-based rotations."""

    def __init__(self, x, y, z):
        """Initializes a vector as a quaternion with a zero scalar component.
        
        Args:
            x (float): The x component of the vector.
            y (float): The y component of the vector.
            z (float): The z component of the vector.
        """
        self.vector_q = Quaternion(0, x, y, z)

    def active_rotation(self, q: Quaternion):
        """Applies an active rotation to the vector using the quaternion rotation q * p * q^*.
        
        Args:
            q (Quaternion): The quaternion representing the rotation.
        
        Returns:
            list: The rotated vector as a list of x, y, z components.
        """
        rotated_q = q.multiply(self.vector_q).multiply(q.conjugate())
        return [rotated_q.x, rotated_q.y, rotated_q.z]

    def passive_rotation(self, q: Quaternion):
        """Applies a passive rotation to the vector using the quaternion rotation q^* * p * q.
        
        Args:
            q (Quaternion): The quaternion representing the rotation.
        
        Returns:
            list: The rotated vector as a list of x, y, z components.
        """
        rotated_q = q.conjugate().multiply(self.vector_q).multiply(q)
        return [rotated_q.x, rotated_q.y, rotated_q.z]

    def distance_to(self, other: "VectorRotation") -> float:
        """Calculates the Euclidean distance between two vectors.
        
        Args:
            other (VectorRotation): The other vector to calculate the distance to.
        
        Returns:
            float: The Euclidean distance between the two vectors.
        """
        dx = self.vector_q.x - other.vector_q.x
        dy = self.vector_q.y - other.vector_q.y
        dz = self.vector_q.z - other.vector_q.z
        return (dx**2 + dy**2 + dz**2) ** 0.5

    def angle_with(self, other: "VectorRotation") -> float:
        """Calculates the angle between this vector and another vector.
        
        Args:
            other (VectorRotation): The other vector to calculate the angle with.
        
        Returns:
            float: The angle between the two vectors in radians.
        """
        dot_product = (self.vector_q.x * other.vector_q.x +
                       self.vector_q.y * other.vector_q.y +
                       self.vector_q.z * other.vector_q.z)
        mag_self = (self.vector_q.x**2 + self.vector_q.y**2 + self.vector_q.z**2) ** 0.5
        mag_other = (other.vector_q.x**2 + other.vector_q.y**2 + other.vector_q.z**2) ** 0.5
        return acos(dot_product / (mag_self * mag_other))