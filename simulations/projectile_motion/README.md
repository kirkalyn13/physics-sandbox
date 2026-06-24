# Simulation 01 — Projectile Motion

Simulates the trajectory of a launched object under gravity with no air resistance.

## Run

```bash
python sim.py
```

## Parameters

Edit `config.py` to adjust inputs:

| Parameter | Default | Description |
|---|---|---|
| `initial_speed` | 50.0 m/s | Launch speed |
| `launch_angle_deg` | 45.0° | Angle from horizontal |
| `gravity` | 9.81 m/s² | Gravitational acceleration |
| `time_step` | 0.01 s | Integration step size |
| `mass` | 1.0 kg | Reserved for drag extension |

## Output

- Console summary: max height, range, flight time, minimum speed
- Chart saved to `outputs/projectile_motion.png`
- Two plots: trajectory arc and speed vs time

## Physics

Uses Euler integration. No drag. Extends cleanly to RK4 via scipy when drag is introduced.