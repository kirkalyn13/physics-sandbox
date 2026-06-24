# Adjust these to change pendulum conditions.
CONFIG = {
    "length": 2.0,           # meters
    "gravity": 9.81,         # m/s^2
    "initial_angle_deg": 80, # degrees from vertical
    "initial_velocity": 0.0, # rad/s (angular velocity at t=0)
    "damping": 0.3,          # damping coefficient (0 = no friction)
    "duration": 10.0,        # seconds to simulate
    "time_step": 0.01,       # seconds per step
    "label": "Pendulum (no damping)",
}