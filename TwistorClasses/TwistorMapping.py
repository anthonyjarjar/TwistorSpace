from TwistorClasses.ComplexNumber import ComplexNumber
from TwistorClasses.ProjectivePoint import ProjectivePoint
from TwistorClasses.ProjectiveLine import ProjectiveLine

class Spinor:
    """Represents a two-component Weyl spinor."""
    def __init__(self, component1: ComplexNumber, component2: ComplexNumber):
        self.components = [component1, component2]

    def display(self):
        print(f"Spinor: [{self.components[0].rel} + {self.components[0].img}i, "
              f"{self.components[1].rel} + {self.components[1].img}i]")

class Twistor:
    """Represents a twistor with components (mu, lambda)."""
    def __init__(self, mu: Spinor, lambda_: Spinor):
        self.mu = mu 
        self.lambda_ = lambda_ 

    def display(self):
        print("Twistor components:")
        print("μ̇:", [(c.rel, c.img) for c in self.mu.components])
        print("λ:", [(c.rel, c.img) for c in self.lambda_.components])

class ComplexMinkowskiPoint:
    """Represents a point in complexified Minkowski space using a 2x2 Hermitian matrix."""
    def __init__(self, t: float, x: float, y: float, z: float):
        self.matrix = [
            [ComplexNumber((t + z) / (2**0.5), 0), ComplexNumber(x / (2**0.5), y / (2**0.5))],
            [ComplexNumber(x / (2**0.5), -y / (2**0.5)), ComplexNumber((t - z) / (2**0.5), 0)]
        ]

    def display(self):
        print("Complexified Minkowski Point Matrix:")
        for row in self.matrix:
            print([f"({elem.rel} + {elem.img}i)" for elem in row])

def twistor_mapping(minkowski_point: ComplexMinkowskiPoint, lambda_spinor: Spinor) -> Twistor:
    """
    Maps a complexified Minkowski point to twistor space.
    
    Args:
        minkowski_point (ComplexMinkowskiPoint): The point in complexified Minkowski space.
        lambda_spinor (Spinor): The spinor representing λα.
    
    Returns:
        Twistor: The twistor corresponding to the point.
    """
    mu_components = [
        minkowski_point.matrix[0][0] * lambda_spinor.components[0] +
        minkowski_point.matrix[0][1] * lambda_spinor.components[1],
        
        minkowski_point.matrix[1][0] * lambda_spinor.components[0] +
        minkowski_point.matrix[1][1] * lambda_spinor.components[1]
    ]
    
    mu_spinor = Spinor(mu_components[0], mu_components[1])
    
    return Twistor(mu=mu_spinor, lambda_=lambda_spinor)
