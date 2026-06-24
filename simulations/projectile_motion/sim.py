import numpy as np
from config import CONFIG
from plotter import plot_results


def compute_trajectory(cfg: dict) -> dict:
    """
    Compute projectile trajectory using Euler integration.
    Returns time, x, y, speed arrays.
    """
    angle_rad = np.radians(cfg["launch_angle_deg"])
    vx = cfg["initial_speed"] * np.cos(angle_rad)
    vy = cfg["initial_speed"] * np.sin(angle_rad)
    g = cfg["gravity"]
    dt = cfg["time_step"]

    t, x, y, speed = [0.0], [0.0], [0.0], [cfg["initial_speed"]]

    while y[-1] >= 0 or len(y) == 1:
        vx_new = vx
        vy_new = vy - g * dt
        x_new = x[-1] + vx * dt
        y_new = y[-1] + vy * dt

        if y_new < 0:
            break

        vx, vy = vx_new, vy_new
        t.append(t[-1] + dt)
        x.append(x_new)
        y.append(y_new)
        speed.append(np.sqrt(vx**2 + vy**2))

    return {
        "t": np.array(t),
        "x": np.array(x),
        "y": np.array(y),
        "speed": np.array(speed),
        "label": cfg["label"],
    }


def print_summary(data: dict) -> None:
    """Print key flight metrics to console."""
    print(f"\n--- {data['label']} ---")
    print(f"  Max height : {max(data['y']):.2f} m")
    print(f"  Range      : {max(data['x']):.2f} m")
    print(f"  Flight time: {max(data['t']):.2f} s")
    print(f"  Min speed  : {min(data['speed']):.2f} m/s  (at apex)")


if __name__ == "__main__":
    results = compute_trajectory(CONFIG)
    print_summary(results)
    plot_results(results)