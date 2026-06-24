# Simulation 02 — Pendulum

Simulates a simple pendulum using a nonlinear ODE solver.
Supports optional damping for a decaying swing.

## Run

```bash
python sim.py
```

## Parameters

Edit `config.py` to adjust inputs:

| Parameter | Default | Description |
|---|---|---|
| `length` | 2.0 m | Pendulum rod length |
| `initial_angle_deg` | 30° | Starting angle from vertical |
| `initial_velocity` | 0.0 rad/s | Angular velocity at t=0 |
| `damping` | 0.0 | Friction coefficient (0 = no friction) |
| `duration` | 10.0 s | Simulation duration |
| `time_step` | 0.01 s | Time resolution |

## Output

- Console summary: max angle, max speed, duration
- Animation saved to `outputs/pendulum.gif`
- Three panels: pendulum swing, angle vs time, angular velocity vs time

## Physics

Uses scipy `solve_ivp` with RK45. Full nonlinear equation — accurate at
large angles unlike the small-angle approximation. Set `damping > 0`
to simulate energy loss over time.