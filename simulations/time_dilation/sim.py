import numpy as np
from config import CONFIG
from plotter import plot_results


C = 299_792_458.0      # speed of light m/s
G = 6.674e-11          # gravitational constant


def compute_special_relativity(cfg: dict) -> dict:
    """
    Compute Lorentz factor and time dilation across a velocity sweep.
    Returns velocity fractions, Lorentz factors, and elapsed time ratios.
    """
    v_fractions = np.linspace(0.0, cfg["max_velocity_fraction"], cfg["steps"])
    v = v_fractions * C
    lorentz = 1.0 / np.sqrt(1 - (v / C) ** 2)
    time_ratio = 1.0 / lorentz

    return {
        "v_fractions": v_fractions,
        "lorentz": lorentz,
        "time_ratio": time_ratio,
        "label": "Special Relativity",
    }


def compute_gravitational(cfg: dict) -> dict:
    """
    Compute gravitational time dilation from surface outward to observer distance.
    Returns radial distances and time dilation factors relative to infinity.
    """
    r_min = cfg["gravitational_radius"]
    r_max = cfg["observer_distance"]
    radii = np.linspace(r_min, r_max, cfg["steps"])
    M = cfg["gravitational_mass"]
    dilation = np.sqrt(1 - (2 * G * M) / (radii * C ** 2))

    return {
        "radii": radii,
        "dilation": dilation,
        "label": "Gravitational (vs observer at infinity)",
    }


def print_summary(sr: dict, grav: dict) -> None:
    """Print key time dilation metrics to console."""
    print(f"\n--- Special Relativity ---")
    print(f"  Max Lorentz factor : {max(sr['lorentz']):.4f}")
    print(f"  Time ratio at max v: {min(sr['time_ratio']):.6f}")

    print(f"\n--- Gravitational ---")
    print(f"  Dilation at surface: {min(grav['dilation']):.8f}")
    print(f"  Dilation at {max(grav['radii'])/1e6:.0f}Mm : {max(grav['dilation']):.8f}")


if __name__ == "__main__":
    sr = compute_special_relativity(CONFIG)
    grav = compute_gravitational(CONFIG)
    print_summary(sr, grav)
    plot_results(sr, grav, CONFIG["label"])