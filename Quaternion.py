from sympy import cos, sin
from math import radians

class Quaternion:
    """Represents a quaternion with real (w) and imaginary (x, y, z) components."""

    def __init__(self, w, x, y, z):
        """Initializes a Quaternion with given components.
        
        Args:
            w (float): The real (scalar) component.
            x (float): The i (first imaginary) component.
            y (float): The j (second imaginary) component.
            z (float): The k (third imaginary) component.
        """
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        """Displays the components of the quaternion in a readable format."""
        print(f"Quaternion: {self.w} + {self.x}i + {self.y}j + {self.z}k")

    def add(self, other: "Quaternion") -> "Quaternion":
        """Adds two quaternions.
        
        Args:
            other (Quaternion): The quaternion to add.
        
        Returns:
            Quaternion: The sum of the two quaternions.
        """
        return Quaternion(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)

    def subtract(self, other: "Quaternion") -> "Quaternion":
        """Subtracts two quaternions.
        
        Args:
            other (Quaternion): The quaternion to subtract.
        
        Returns:
            Quaternion: The difference of the two quaternions.
        """
        return Quaternion(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)

    def multiply(self, other: "Quaternion") -> "Quaternion":
        """Multiplies two quaternions.
        
        Args:
            other (Quaternion): The quaternion to multiply by.
        
        Returns:
            Quaternion: The product of the two quaternions.
        """
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(w, x, y, z)

    def magnitude(self) -> float:
        """Calculates the magnitude of the quaternion.
        
        Returns:
            float: The magnitude of the quaternion.
        """
        return (self.w**2 + self.x**2 + self.y**2 + self.z**2) ** 0.5

    def conjugate(self) -> "Quaternion":
        """Calculates the conjugate of the quaternion.
        
        Returns:
            Quaternion: The conjugate of the quaternion.
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def normalize(self) -> "Quaternion":
        """Normalizes the quaternion to unit length.
        
        Returns:
            Quaternion: A normalized (unit) quaternion.
        """
        mag = self.magnitude()
        return Quaternion(self.w / mag, self.x / mag, self.y / mag, self.z / mag)

    def inverse(self) -> "Quaternion":
        """Calculates the inverse of the quaternion.
        
        Returns:
            Quaternion: The inverse of the quaternion.
        """
        conj = self.conjugate()
        mag_squared = self.magnitude() ** 2
        return Quaternion(conj.w / mag_squared, conj.x / mag_squared, conj.y / mag_squared, conj.z / mag_squared)

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

vector = [1, 0, 0]    
vector_to_be_rotated = VectorRotation(vector[0], vector[1], vector[2])

angle = 90
rotation_q = Quaternion(cos(radians(angle) / 2), 0, sin(radians(angle) / 2), 0)
rotation_q.display()

rotated_vector_active = vector_to_be_rotated.active_rotation(rotation_q)
print("Active Rotation Result:", rotated_vector_active)

rotated_vector_passive = vector_to_be_rotated.passive_rotation(rotation_q)
print("Passive Rotation Result:", rotated_vector_passive)
