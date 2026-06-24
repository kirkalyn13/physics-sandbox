# Simulation 03 — Orbital Mechanics

Simulates a two-body gravitational orbit around a central mass.
Defaults to a satellite in Low Earth Orbit.

## Run

```bash
python sim.py
```

## Parameters

Edit `config.py` to adjust inputs:

| Parameter | Default | Description |
|---|---|---|
| `central_mass` | 5.972e24 kg | Mass of central body (Earth) |
| `initial_x` | 7.0e6 m | Starting x position from center |
| `initial_y` | 0.0 m | Starting y position from center |
| `initial_vx` | 0.0 m/s | Starting x velocity |
| `initial_vy` | 7546.0 m/s | Starting y velocity (circular orbit) |
| `duration` | 6000.0 s | Simulation duration |
| `time_step` | 1.0 s | Time resolution |
| `G` | 6.674e-11 | Gravitational constant |

## Output

- Console summary: min/max altitude, min/max speed, duration
- Animation saved to `outputs/orbital_mechanics.gif`
- Three panels: orbital path with Earth, altitude vs time, speed vs time

## Physics

Uses scipy `solve_ivp` with RK45 at high tolerance (rtol/atol 1e-9) to
preserve orbital energy over time. Acceleration is a 2D vector always
pointing toward the central mass. Tighter tolerances than the pendulum
because orbital errors accumulate fast over many revolutions.

## Experiments

- Set `initial_vy` lower than 7546 for an elliptical orbit
- Swap `central_mass` to 1.989e30 for a solar orbit (adjust distances)
- Watch altitude and speed oscillate inversely — that is Kepler's second law