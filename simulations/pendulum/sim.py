import numpy as np
from scipy.integrate import solve_ivp
from config import CONFIG
from plotter import plot_results


def equations(t: float, y: list, g: float, L: float, b: float) -> list:
    """
    Pendulum ODE system.
    y[0] = angle (radians), y[1] = angular velocity (rad/s).
    Returns [d_angle/dt, d_omega/dt].
    """
    theta, omega = y
    d_theta = omega
    d_omega = -(g / L) * np.sin(theta) - b * omega
    return [d_theta, d_omega]


def compute_trajectory(cfg: dict) -> dict:
    """
    Solve pendulum ODE using RK45 and return time and state arrays.
    """
    theta0 = np.radians(cfg["initial_angle_deg"])
    omega0 = cfg["initial_velocity"]
    t_span = (0.0, cfg["duration"])
    t_eval = np.arange(0.0, cfg["duration"], cfg["time_step"])

    solution = solve_ivp(
        equations,
        t_span,
        [theta0, omega0],
        args=(cfg["gravity"], cfg["length"], cfg["damping"]),
        t_eval=t_eval,
        method="RK45",
    )

    theta = solution.y[0]
    omega = solution.y[1]
    x = cfg["length"] * np.sin(theta)
    y = -cfg["length"] * np.cos(theta)

    return {
        "t": solution.t,
        "theta": theta,
        "omega": omega,
        "x": x,
        "y": y,
        "length": cfg["length"],
        "label": cfg["label"],
    }


def print_summary(data: dict) -> None:
    """Print key pendulum metrics to console."""
    print(f"\n--- {data['label']} ---")
    print(f"  Max angle  : {np.degrees(max(abs(data['theta']))):.2f} deg")
    print(f"  Max speed  : {max(abs(data['omega'])):.2f} rad/s")
    print(f"  Duration   : {max(data['t']):.2f} s")


if __name__ == "__main__":
    results = compute_trajectory(CONFIG)
    print_summary(results)
    plot_results(results)