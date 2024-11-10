from TwistorClasses.ComplexNumber import ComplexNumber
from TwistorClasses.ProjectivePoint import ProjectivePoint
from math import acos


def spacetime_to_twistor(t, x, y, z) -> ProjectivePoint:
    """Maps a spacetime point (t, x, y, z) to a twistor space ProjectivePoint.
    
    Args:
        t (float): The time coordinate.
        x (float): The x-coordinate in space.
        y (float): The y-coordinate in space.
        z (float): The z-coordinate in space.
    
    Returns:
        ProjectivePoint: A point in twistor space representing the spacetime event.
    """
    omega_1 = ComplexNumber(x, y)
    omega_2 = ComplexNumber(t + z, 0)
    pi_1 = ComplexNumber(1, 0) 
    pi_2 = ComplexNumber(0, 1) 

    return ProjectivePoint(omega_1, omega_2, pi_1, pi_2)

def spacetime_null_direction_to_twistor(t, x, y, z) -> ProjectivePoint:
    """Converts a null direction in spacetime to a twistor point.
    
    Args:
        t (float): The time component of the spacetime point.
        x (float): The x-coordinate in space.
        y (float): The y-coordinate in space.
        z (float): The z-coordinate in space.
    
    Returns:
        ProjectivePoint: A twistor point in projective space representing the null direction.
    """
    
    omega_1 = ComplexNumber(x, y)
    omega_2 = ComplexNumber(t + z, 0)
    pi_1 = ComplexNumber(1, 0)  
    pi_2 = ComplexNumber(0, 1) 

    return ProjectivePoint(omega_1, omega_2, pi_1, pi_2)