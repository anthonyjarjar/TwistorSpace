class ComplexNumber:
    """This class represents a complex number with a real (rel) and imaginary (img) component.
       Functions include: 
            Add, Subtract, Multiply, Divide, Magnitude, Conjugate
    """

    def __init__(self, rel, img):
        self.rel = rel
        self.img = img

    def display(self):
        print(f"The real component is {self.rel}")
        print(f"The imaginary component is {self.img}i")

    def add(self, other: "ComplexNumber") -> "ComplexNumber":
        """Adds two complex numbers and returns a new ComplexNumber instance."""

        return ComplexNumber(self.rel + other.rel, self.img + other.img)

    def subtract(self, other: "ComplexNumber") -> "ComplexNumber":
        """Subtracts two complex numbers and returns a new ComplexNumber instance."""
        
        return ComplexNumber(self.rel - other.rel, self.img - other.img)

    def multiply(self, other: "ComplexNumber") -> "ComplexNumber":
        """Multiplies two complex numbers."""
        
        rel_part = self.rel * other.rel - self.img * other.img
        img_part = self.rel * other.img + self.img * other.rel
        return ComplexNumber(rel_part, img_part)

    def magnitude(self) -> int:
        """Returns the int value of the magnitude of the complex number."""

        return (self.rel**2 + self.img**2) ** 0.5
    
    def conjugate(self) -> "ComplexNumber":
        """Returns the complex conjugate of the given complex number."""

        return ComplexNumber(self.rel, -self.img)

    def divide(self, other: "ComplexNumber") -> "ComplexNumber":
        """Returns the fraction of the two given complex numbers, with the passed parameter as the denominator."""

        other_star = other.conjugate()
        other_magnitude_squared = other.magnitude() ** 2
        numerator = self.multiply(other_star)
        
        rel_part = numerator.rel / other_magnitude_squared
        img_part = numerator.img / other_magnitude_squared
        
        return ComplexNumber(rel_part, img_part)
