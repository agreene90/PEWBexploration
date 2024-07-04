import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c

def positive_energy_warp_field(r, sigma, rho):
    """Calculate the warp field using positive energy density."""
    return rho * np.exp(-r**2 / sigma**2)

def anisotropic_warp_field(x, y, z, t, rho, sigma, k, omega):
    """Calculate the anisotropic warp field."""
    r = np.sqrt(x**2 + y**2 + z**2)
    return rho * np.exp(-r**2 / sigma**2) * (1 + np.cos(k*x + omega*t))

def validate_positive_energy_warp_field():
    # Define parameters
    rho = 1.0
    sigma = 1.0
    r = np.linspace(-5, 5, 100)
    
    # Calculate warp field
    warp_field = positive_energy_warp_field(r, sigma, rho)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(r, warp_field, label='Warp Field')
    plt.title('Positive Energy Warp Field')
    plt.xlabel('Radial Distance (r)')
    plt.ylabel('Warp Field Intensity')
    plt.legend()
    plt.grid(True)
    plt.show()

def validate_anisotropic_warp_field():
    # Define parameters
    rho = 1.0
    sigma = 1.0
    k = 1.0
    omega = 1.0
    t = 0
    
    # Calculate warp field for different directions
    x = np.linspace(-5, 5, 100)
    warp_field_x = anisotropic_warp_field(x, 0, 0, t, rho, sigma, k, omega)
    
    y = np.linspace(-5, 5, 100)
    warp_field_y = anisotropic_warp_field(0, y, 0, t, rho, sigma, k, omega)
    
    z = np.linspace(-5, 5, 100)
    warp_field_z = anisotropic_warp_field(0, 0, z, t, rho, sigma, k, omega)
    
    # Plot results
    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(x, warp_field_x, label='Warp Field (x-direction)')
    plt.title('Anisotropic Warp Field - X Direction')
    plt.xlabel('Distance (x)')
    plt.ylabel('Warp Field Intensity')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    plt.plot(y, warp_field_y, label='Warp Field (y-direction)')
    plt.title('Anisotropic Warp Field - Y Direction')
    plt.xlabel('Distance (y)')
    plt.ylabel('Warp Field Intensity')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(z, warp_field_z, label='Warp Field (z-direction)')
    plt.title('Anisotropic Warp Field - Z Direction')
    plt.xlabel('Distance (z)')
    plt.ylabel('Warp Field Intensity')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    validate_positive_energy_warp_field()
    validate_anisotropic_warp_field()
