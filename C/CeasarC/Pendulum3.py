import pygame
import numpy as np

# Initialize pygame and set up the screen
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Constants
default_g = 9.81
default_mass1 = 1.0
default_mass2 = 0.5
default_friction_coefficient = 0.99975
dt = 0.12
length1, length2 = 200, 200
origin = (width // 2, height // 4)

# Variables with initial values
g = default_g
mass1 = default_mass1
mass2 = default_mass2
friction_coefficient = default_friction_coefficient
friction_enabled = False
theta1, theta2 = np.pi / 2, np.pi / 2
theta1_dot, theta2_dot = 0, 0

# Slider settings
slider_width, slider_height = 150, 10
slider_x = 20
slider_mass1_y = 100
slider_mass2_y = 150
slider_gravity_y = 200
back_to_default_rect = pygame.Rect(20, 300, 150, 30)

# Function to calculate angular accelerations
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

# Function to reset to default values
def reset_defaults():
    global g, mass1, mass2, friction_coefficient
    g = default_g
    mass1 = default_mass1
    mass2 = default_mass2
    friction_coefficient = default_friction_coefficient

# Function to draw slider
def draw_slider(y, value, label, max_value):
    pygame.draw.rect(screen, GRAY, (slider_x, y, slider_width, slider_height))
    pos_x = slider_x + int((value / max_value) * slider_width)
    pygame.draw.circle(screen, BLACK, (pos_x, y + slider_height // 2), 5)
    font = pygame.font.Font(None, 24)
    text = font.render(f"{label}: {value:.2f}", True, BLACK)
    screen.blit(text, (slider_x + slider_width + 10, y - 10))

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                friction_enabled = not friction_enabled
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle back to default button
            if back_to_default_rect.collidepoint(event.pos):
                reset_defaults()

    # Update slider values based on mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:  # If the left mouse button is pressed
        clamped_x = max(slider_x, min(mouse_x, slider_x + slider_width))  # Restrict within slider bounds
        if slider_mass1_y <= mouse_y <= slider_mass1_y + slider_height:
            mass1 = (clamped_x - slider_x) / slider_width * 100  # Scale to range 0-100 kg
        elif slider_mass2_y <= mouse_y <= slider_mass2_y + slider_height:
            mass2 = (clamped_x - slider_x) / slider_width * 100
        elif slider_gravity_y <= mouse_y <= slider_gravity_y + slider_height:
            g = (clamped_x - slider_x) / slider_width * 50  # Scale to range 0-50

    # Calculate the angular accelerations
    theta1_ddot, theta2_ddot = accelerations(theta1, theta2, theta1_dot, theta2_dot)
    
    # Update angular velocities and angles using Euler’s method
    theta1_dot += theta1_ddot * dt
    theta2_dot += theta2_ddot * dt
    theta1 += theta1_dot * dt
    theta2 += theta2_dot * dt

    # Apply friction if enabled
    if friction_enabled:
        theta1_dot *= friction_coefficient
        theta2_dot *= friction_coefficient

    # Calculate positions of the pendulum bobs
    x1 = origin[0] + length1 * np.sin(theta1)
    y1 = origin[1] + length1 * np.cos(theta1)
    x2 = x1 + length2 * np.sin(theta2)
    y2 = y1 + length2 * np.cos(theta2)

    # Draw the pendulum
    pygame.draw.line(screen, BLACK, origin, (x1, y1), 2)
    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)
    pygame.draw.circle(screen, BLUE, (int(x1), int(y1)), 10)
    pygame.draw.circle(screen, RED, (int(x2), int(y2)), 10)

    # Draw sliders
    draw_slider(slider_mass1_y, mass1, "Mass1", 100)
    draw_slider(slider_mass2_y, mass2, "Mass2", 100)
    draw_slider(slider_gravity_y, g, "Gravity", 50)

    # Draw friction toggle and default reset button
    pygame.draw.rect(screen, GRAY, back_to_default_rect)
    font = pygame.font.Font(None, 24)
    default_text = font.render("Back to Default", True, BLACK)
    screen.blit(default_text, (back_to_default_rect.x + 10, back_to_default_rect.y + 5))

    # Display friction status
    friction_status = font.render(f"Friction: {'On' if friction_enabled else 'Off'} (Press 'F' to toggle)", True, BLACK)
    screen.blit(friction_status, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
