# Simulation 04 — Time Dilation

Simulates both special relativistic and gravitational time dilation.
No ODE solver needed — both are closed-form equations swept across a range.

## Run

```bash
python sim.py
```

## Parameters

Edit `config.py` to adjust inputs:

| Parameter | Default | Description |
|---|---|---|
| `max_velocity_fraction` | 0.9999 | Max velocity as fraction of c |
| `gravitational_mass` | 5.972e24 kg | Central mass (Earth) |
| `gravitational_radius` | 6.371e6 m | Surface radius |
| `observer_distance` | 1.0e8 m | Outer boundary for grav sweep |
| `steps` | 1000 | Number of evaluation points |

## Output

- Console summary: max Lorentz factor, time ratio, gravitational dilation
- Animation saved to `outputs/time_dilation.gif`
- Four panels: Lorentz factor, time ratio, gravitational dilation, combined

## Physics

Special relativity uses the Lorentz factor γ = 1 / √(1 - v²/c²).
Gravitational dilation uses the Schwarzschild metric: √(1 - 2GM/rc²).
At Earth's surface the gravitational effect is tiny — swap in a neutron
star mass to see it become dramatic.

## Experiments

- Set `max_velocity_fraction` to 0.99999 to see γ explode past 200
- Swap `gravitational_mass` to 2.0e30 (neutron star) for extreme curvature
- Reduce `observer_distance` toward the Schwarzschild radius to approach
  the event horizon where dilation factor approaches zero