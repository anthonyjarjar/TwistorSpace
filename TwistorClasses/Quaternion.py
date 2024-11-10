from math import acos

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

    def dot_product(self, other: "Quaternion") -> float:
        """Calculates the dot product of two quaternions.
        
        Args:
            other (Quaternion): The quaternion to perform the dot product with.
        
        Returns:
            float: The result of the dot product.
        """
        return self.w * other.w + self.x * other.x + self.y * other.y + self.z * other.z

    def angle_with(self, other: "Quaternion") -> float:
        """Calculates the angle between two quaternions.
        
        Args:
            other (Quaternion): The quaternion to calculate the angle with.
        
        Returns:
            float: The angle between the two quaternions in radians.
        """
        dot_prod = self.dot_product(other)
        return acos(dot_prod / (self.magnitude() * other.magnitude()))

