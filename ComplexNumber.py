class ComplexNumber:
    """This class represents a complex number with a real (rel) and imaginary (img) component.
    
    Functions include: 
        - add
        - subtract
        - multiply
        - divide
        - magnitude
        - conjugate
    """

    def __init__(self, rel, img):
        """Initializes a ComplexNumber with real and imaginary components.
        
        Args:
            rel (float): The real part of the complex number.
            img (float): The imaginary part of the complex number.
        """
        self.rel = rel
        self.img = img

    def display(self):
        """Displays the real and imaginary components of the complex number."""
        print(f"The real component is {self.rel}")
        print(f"The imaginary component is {self.img}i")

    def add(self, other: "ComplexNumber") -> "ComplexNumber":
        """Adds two complex numbers and returns a new ComplexNumber instance.
        
        Args:
            other (ComplexNumber): The complex number to add.
        
        Returns:
            ComplexNumber: The result of the addition.
        """
        return ComplexNumber(self.rel + other.rel, self.img + other.img)

    def subtract(self, other: "ComplexNumber") -> "ComplexNumber":
        """Subtracts two complex numbers and returns a new ComplexNumber instance.
        
        Args:
            other (ComplexNumber): The complex number to subtract.
        
        Returns:
            ComplexNumber: The result of the subtraction.
        """
        return ComplexNumber(self.rel - other.rel, self.img - other.img)

    def multiply(self, other: "ComplexNumber") -> "ComplexNumber":
        """Multiplies two complex numbers.
        
        Args:
            other (ComplexNumber): The complex number to multiply by.
        
        Returns:
            ComplexNumber: The result of the multiplication.
        """
        rel_part = self.rel * other.rel - self.img * other.img
        img_part = self.rel * other.img + self.img * other.rel
        return ComplexNumber(rel_part, img_part)

    def magnitude(self) -> float:
        """Calculates the magnitude of the complex number.
        
        Returns:
            float: The magnitude of the complex number.
        """
        return (self.rel**2 + self.img**2) ** 0.5
    
    def conjugate(self) -> "ComplexNumber":
        """Calculates the complex conjugate of the complex number.
        
        Returns:
            ComplexNumber: The conjugate of the complex number.
        """
        return ComplexNumber(self.rel, -self.img)

    def divide(self, other: "ComplexNumber") -> "ComplexNumber":
        """Divides the complex number by another complex number.
        
        Args:
            other (ComplexNumber): The complex number to divide by.
        
        Returns:
            ComplexNumber: The result of the division.
        """
        other_star = other.conjugate()
        other_magnitude_squared = other.magnitude() ** 2
        numerator = self.multiply(other_star)
        
        rel_part = numerator.rel / other_magnitude_squared
        img_part = numerator.img / other_magnitude_squared
        
        return ComplexNumber(rel_part, img_part)
