import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 1. SET YOUR PHYSICS PARAMETERS HERE ---
u = 5.0    # Initial Velocity (m/s)
a = 2.0    # Acceleration (m/s^2)
t_max = 10 # Total time to simulate (seconds)

# --- 2. SETUP CALCULATIONS ---
dt = 0.1   # Time step
t_values = np.arange(0, t_max, dt)

# Calculate S for every time step: S = ut + 0.5 * a * t^2
S_values = u * t_values + 0.5 * a * t_values**2

# --- 3. CREATE THE PLOT ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
plt.subplots_adjust(hspace=0.4)

# Plot 1: The "Real World" (A car moving on a track)
ax1.set_xlim(0, max(S_values) * 1.1)
ax1.set_ylim(-1, 1)
ax1.set_xlabel('Distance (meters)')
ax1.set_yticks([])
ax1.set_title(f'Real-World Motion: u={u} m/s, a={a} m/s²')
car_dot, = ax1.plot([], [], 'ro', markersize=15, label='Car') # 'ro' = Red Circle
ax1.legend()
ax1.grid(True, axis='x')

# Plot 2: The Math (Distance vs. Time Graph)
ax2.set_xlim(0, t_max)
ax2.set_ylim(0, max(S_values) * 1.1)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Displacement (S)')
ax2.set_title('The Math: S = ut + ½at²')
line, = ax2.plot([], [], 'b-', lw=2) # Blue line
time_text = ax2.text(0.02, 0.9, '', transform=ax2.transAxes)

# --- 4. ANIMATION FUNCTION ---
def animate(i):
    # Current time and displacement
    current_t = t_values[:i]
    current_S = S_values[:i]
    
    # Update the "Car" position (only moves along x-axis)
    if i < len(S_values):
        car_dot.set_data([S_values[i]], [0])  # x=Distance, y=0
    
    # Update the Graph line
    line.set_data(current_t, current_S)
    
    # Update the timer text
    if i < len(t_values):
        time_text.set_text(f't = {t_values[i]:.1f} s\nS = {S_values[i]:.1f} m')
    
    return car_dot, line, time_text

# --- 5. RUN ANIMATION ---
ani = animation.FuncAnimation(fig, animate, frames=len(t_values), interval=50, blit=True)

plt.show()
