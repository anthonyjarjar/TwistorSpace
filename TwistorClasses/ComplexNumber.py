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
        print(f"The real component is {self.rel:.2f}")
        print(f"The imaginary component is {self.img:.2f}i")
    
    def __str__(self):
        """String representation for easier control over formatting in display methods."""
        return f"({self.rel:.2f} + {self.img:.2f}i)"

    # Operator overload for addition
    def __add__(self, other):
        """Allows the use of the + operator with ComplexNumber instances."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.rel + other.rel, self.img + other.img)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.rel + other, self.img)
        else:
            raise TypeError("Unsupported operand type for +")

    # Operator overload for subtraction
    def __sub__(self, other):
        """Allows the use of the - operator with ComplexNumber instances."""
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.rel - other.rel, self.img - other.img)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.rel - other, self.img)
        else:
            raise TypeError("Unsupported operand type for -")

    # Operator overload for multiplication
    def __mul__(self, other):
        """Allows the use of the * operator with ComplexNumber instances."""
        if isinstance(other, ComplexNumber):
            rel_part = self.rel * other.rel - self.img * other.img
            img_part = self.rel * other.img + self.img * other.rel
            return ComplexNumber(rel_part, img_part)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.rel * other, self.img * other)
        else:
            raise TypeError("Unsupported operand type for *")

    # Operator overload for true division
    def __truediv__(self, other):
        """Allows the use of the / operator with ComplexNumber instances."""
        if isinstance(other, ComplexNumber):
            other_star = other.conjugate()
            other_magnitude_squared = other.magnitude() ** 2
            numerator = self * other_star
            
            rel_part = numerator.rel / other_magnitude_squared
            img_part = numerator.img / other_magnitude_squared
            
            return ComplexNumber(rel_part, img_part)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.rel / other, self.img / other)
        else:
            raise TypeError("Unsupported operand type for /")
        
    def __neg__(self):
        """Allows the use of the unary - operator with ComplexNumber instances."""
        return ComplexNumber(-self.rel, -self.img)

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

