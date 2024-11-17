import pygame
import numpy as np

# Initialize pygame and set up the screen
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Constants
g = 9.81                # gravitational acceleration
dt = 0.01               # time step for simulation
length1, length2 = 200, 200   # lengths of the pendulum rods
mass1, mass2 = 1.0, 1.0 # masses of the pendulum bobs
origin = (width // 2, height // 4)  # origin point

# Initial angles (in radians) and angular velocities
theta1, theta2 = np.pi / 2, np.pi / 2
theta1_dot, theta2_dot = 0, 0

# Function to calculate angular accelerations using the actual equations of motion for a double pendulum
def accelerations(theta1, theta2, theta1_dot, theta2_dot):
    delta = theta2 - theta1
    denom1 = (mass1 + mass2) * length1 - mass2 * length1 * np.cos(delta) ** 2
    denom2 = (length2 / length1) * denom1

    theta1_ddot = ((mass2 * length1 * theta1_dot ** 2 * np.sin(delta) * np.cos(delta) +
                    mass2 * g * np.sin(theta2) * np.cos(delta) +
                    mass2 * length2 * theta2_dot ** 2 * np.sin(delta) -
                    (mass1 + mass2) * g * np.sin(theta1)) / denom1)
    
    theta2_ddot = ((-mass2 * length2 * theta2_dot ** 2 * np.sin(delta) * np.cos(delta) +
                    (mass1 + mass2) * (g * np.sin(theta1) * np.cos(delta) - length1 * theta1_dot ** 2 * np.sin(delta) -
                                       g * np.sin(theta2))) / denom2)
    
    return theta1_ddot, theta2_ddot

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the angular accelerations
    theta1_ddot, theta2_ddot = accelerations(theta1, theta2, theta1_dot, theta2_dot)
    
    # Update angular velocities and angles using Euler’s method
    theta1_dot += theta1_ddot * dt
    theta2_dot += theta2_ddot * dt
    theta1 += theta1_dot * dt
    theta2 += theta2_dot * dt

    # Calculate positions of the pendulum bobs
    x1 = origin[0] + length1 * np.sin(theta1)
    y1 = origin[1] + length1 * np.cos(theta1)
    x2 = x1 + length2 * np.sin(theta2)
    y2 = y1 + length2 * np.cos(theta2)

    # Clear the screen and draw the pendulum
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), origin, (x1, y1), 2)
    pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)
    pygame.draw.circle(screen, (0, 0, 255), (int(x1), int(y1)), 10)
    pygame.draw.circle(screen, (255, 0, 0), (int(x2), int(y2)), 10)

    pygame.display.flip()
    clock.tick(1010)  # Limit to 60 FPS

pygame.quit()
