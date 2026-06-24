# Adjust these to change orbital conditions.
CONFIG = {
    "central_mass": 5.972e24,      # kg (Earth by default)
    "satellite_mass": 1.0,         # kg (negligible, not used in force calc)
    "initial_x": 7.0e6,            # m (starting x position from center)
    "initial_y": 0.0,              # m (starting y position from center)
    "initial_vx": 0.0,             # m/s (starting x velocity)
    "initial_vy": 7546.0,          # m/s (circular orbit velocity at 7000km)
    "duration": 1000.0,            # seconds (~one orbit)
    "time_step": 0.5,              # seconds per step
    "G": 6.674e-11,                # gravitational constant
    "label": "Orbital Mechanics (Low Earth Orbit)",
}