import numpy as np
from scipy.integrate import solve_ivp
from config import CONFIG
from plotter import plot_results


def equations(t: float, y: list, G: float, M: float) -> list:
    """
    Two-body orbital ODE system.
    y = [x, y, vx, vy].
    Returns [vx, vy, ax, ay] where acceleration points toward central mass.
    """
    x, pos_y, vx, vy = y
    r = np.sqrt(x**2 + pos_y**2)
    ax = -G * M * x / r**3
    ay = -G * M * pos_y / r**3
    return [vx, vy, ax, ay]


def compute_trajectory(cfg: dict) -> dict:
    """
    Solve orbital ODE using RK45 and return position and velocity arrays.
    """
    y0 = [
        cfg["initial_x"],
        cfg["initial_y"],
        cfg["initial_vx"],
        cfg["initial_vy"],
    ]
    t_span = (0.0, cfg["duration"])
    t_eval = np.arange(0.0, cfg["duration"], cfg["time_step"])

    solution = solve_ivp(
        equations,
        t_span,
        y0,
        args=(cfg["G"], cfg["central_mass"]),
        t_eval=t_eval,
        method="RK45",
        rtol=1e-9,
        atol=1e-9,
    )

    x = solution.y[0]
    y = solution.y[1]
    vx = solution.y[2]
    vy = solution.y[3]
    r = np.sqrt(x**2 + y**2)
    speed = np.sqrt(vx**2 + vy**2)

    return {
        "t": solution.t,
        "x": x,
        "y": y,
        "vx": vx,
        "vy": vy,
        "r": r,
        "speed": speed,
        "label": cfg["label"],
    }


def print_summary(data: dict) -> None:
    """Print key orbital metrics to console."""
    print(f"\n--- {data['label']} ---")
    print(f"  Min altitude : {(min(data['r']) - 6.371e6) / 1000:.2f} km")
    print(f"  Max altitude : {(max(data['r']) - 6.371e6) / 1000:.2f} km")
    print(f"  Min speed    : {min(data['speed']):.2f} m/s")
    print(f"  Max speed    : {max(data['speed']):.2f} m/s")
    print(f"  Duration     : {max(data['t']):.2f} s")


if __name__ == "__main__":
    results = compute_trajectory(CONFIG)
    print_summary(results)
    plot_results(results)