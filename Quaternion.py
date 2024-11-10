from sympy import cos, sin, rad


class Quaternion:
    """This class represents a quaternion with a real (w) and three imaginary (x, y, z) components.
       Functions include:
            Add, Subtract, Multiply, Conjugate, Magnitude, Normalize
    """

    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(f"The real (scalar) component is {self.w}")
        print(f"The imaginary components are {self.x}i, {self.y}j, {self.z}k")

    def add(self, other: "Quaternion"):
        """Adds two quaternions."""

        self.w = self.w + other.w
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z

    def subtract(self, other: "Quaternion"):
        """Subtracts two quaternions."""

        self.w = self.w - other.w
        self.x = self.x - other.x
        self.y = self.y - other.y
        self.z = self.z - other.z

    def multiply(self, other: "Quaternion") -> "Quaternion":
        """Multiplies two quaternions."""

        w_part = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x_part = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y_part = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z_part = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w

        return Quaternion(w_part, x_part, y_part, z_part)

    def magnitude(self) -> float:
        """Returns the magnitude of the quaternion."""

        return (self.w**2 + self.x**2 + self.y**2 + self.z**2) ** 0.5

    def conjugate(self) -> "Quaternion":
        """Returns the conjugate of the quaternion."""

        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def normalize(self) -> "Quaternion":
        """Returns a normalized (unit) quaternion."""

        mag = self.magnitude()
        return Quaternion(self.w / mag, self.x / mag, self.y / mag, self.z / mag)

    def inverse(self) -> "Quaternion":
        """Returns the inverse of the quaternion."""

        conj = self.conjugate()
        mag_squared = self.magnitude() ** 2
        return Quaternion(conj.w / mag_squared, conj.x / mag_squared, conj.y / mag_squared, conj.z / mag_squared)
    

class VectorRotation: 
    def __init__(self, x, y, z):
        self.vector_q = Quaternion(0, x, y, z)

    def active_rotation(self, q: Quaternion): 
        """Applies an active rotation to the vector using quaternion rotation: q * p * q^*"""

        mult_1 = self.vector_q.multiply(q)
        q_star = q.conjugate()
        
        p_prime_q = q_star.multiply(mult_1)
        
        rotated_vector = [p_prime_q.x, p_prime_q.y, p_prime_q.z]
        
        return rotated_vector
    
    def passive_rotation(self, q: Quaternion):
        """Applies a passive rotation to the vector using quaternion rotation: q^* * p * q"""

        q_star = q.conjugate()
        mult_1 = self.vector_q.multiply(q_star)
        
        p_prime_q = q.multiply(mult_1)
        
        rotated_vector = [p_prime_q.x, p_prime_q.y, p_prime_q.z]
        
        return rotated_vector


vector = [1, 0, 0]    
vector_to_be_rotated = VectorRotation(vector[0], vector[1], vector[2])

angle = 90
rotation_q = Quaternion(cos(rad(angle) / 2), 0, sin(rad(angle) / 2), 0)
rotation_q.display()

rotated_vector_active = vector_to_be_rotated.active_rotation(rotation_q)
print("Active Rotation Result:", rotated_vector_active)

rotated_vector_passive = vector_to_be_rotated.passive_rotation(rotation_q)
print("Passive Rotation Result:", rotated_vector_passive)
