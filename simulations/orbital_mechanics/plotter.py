import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import numpy as np
import os


EARTH_RADIUS = 6.371e6


def plot_results(data: dict) -> None:
    """
    Animate orbital path on the left, altitude and speed stacked on the right.
    Saves animation to outputs/ and displays it.
    """
    os.makedirs("outputs", exist_ok=True)
    plt.style.use("dark_background")

    fig = plt.figure(figsize=(14, 10))
    fig.suptitle(data["label"], fontsize=14)

    gs = fig.add_gridspec(2, 2, width_ratios=[1.4, 1], hspace=0.4, wspace=0.35)

    ax1 = fig.add_subplot(gs[:, 0])   # left column, full height
    ax2 = fig.add_subplot(gs[0, 1])   # right column, top
    ax3 = fig.add_subplot(gs[1, 1])   # right column, bottom

    margin = max(abs(data["x"].max()), abs(data["y"].max())) * 1.15
    ax1.set_xlim(-margin, margin)
    ax1.set_ylim(-margin, margin)
    ax1.set_aspect("equal")
    ax1.set_xlabel("x (m)")
    ax1.set_ylabel("y (m)")
    ax1.set_title("Orbital Path")
    ax1.grid(True, linestyle="--", alpha=0.2)

    earth = patches.Circle((0, 0), EARTH_RADIUS, color="deepskyblue", zorder=5)
    ax1.add_patch(earth)

    ax2.set_xlim(0, max(data["t"]))
    ax2.set_ylim(
        (min(data["r"]) - EARTH_RADIUS) / 1000 * 0.95,
        (max(data["r"]) - EARTH_RADIUS) / 1000 * 1.05,
    )
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Altitude (km)")
    ax2.set_title("Altitude vs Time")
    ax2.grid(True, linestyle="--", alpha=0.3)

    ax3.set_xlim(0, max(data["t"]))
    ax3.set_ylim(min(data["speed"]) * 0.98, max(data["speed"]) * 1.02)
    ax3.set_xlabel("Time (s)")
    ax3.set_ylabel("Speed (m/s)")
    ax3.set_title("Speed vs Time")
    ax3.grid(True, linestyle="--", alpha=0.3)

    orbit_trail, = ax1.plot([], [], color="cyan", linewidth=1, alpha=0.4)
    satellite, = ax1.plot([], [], "o", color="cyan", markersize=6, zorder=6)
    altitude_line, = ax2.plot([], [], color="orange", linewidth=2)
    speed_line, = ax3.plot([], [], color="cyan", linewidth=2)

    def update(frame):
        """Update satellite position, trail, altitude, and speed per frame."""
        orbit_trail.set_data(data["x"][:frame], data["y"][:frame])
        satellite.set_data([data["x"][frame - 1]], [data["y"][frame - 1]])
        altitude_line.set_data(
            data["t"][:frame],
            (data["r"][:frame] - EARTH_RADIUS) / 1000,
        )
        speed_line.set_data(data["t"][:frame], data["speed"][:frame])
        return orbit_trail, satellite, altitude_line, speed_line

    step = 10
    frames = range(0, len(data["t"]), step)
    interval_ms = max(1, int(1000 * data["t"][-1] / len(data["t"]) / 2))

    ani = animation.FuncAnimation(
        fig, update, frames=frames, interval=interval_ms, blit=True
    )

    output_path = os.path.join("outputs", "orbital_mechanics.gif")
    ani.save(output_path, writer="pillow", fps=60)
    print(f"\n  Animation saved → {output_path}")
    plt.show()