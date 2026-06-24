import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os


def plot_results(data: dict) -> None:
    """
    Animate pendulum swing, angle, and angular velocity over time.
    Saves animation to outputs/ and displays it.
    """
    os.makedirs("outputs", exist_ok=True)
    plt.style.use("dark_background")

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(data["label"], fontsize=14)

    L = data["length"]
    ax1.set_xlim(-L * 1.2, L * 1.2)
    ax1.set_ylim(-L * 1.2, L * 0.2)
    ax1.set_aspect("equal")
    ax1.set_xlabel("x (m)")
    ax1.set_ylabel("y (m)")
    ax1.set_title("Pendulum")
    ax1.grid(True, linestyle="--", alpha=0.3)
    ax1.plot(0, 0, "w+", markersize=10)

    ax2.set_xlim(0, max(data["t"]))
    ax2.set_ylim(min(data["theta"]) * 1.1, max(data["theta"]) * 1.1)
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Angle (rad)")
    ax2.set_title("Angle vs Time")
    ax2.grid(True, linestyle="--", alpha=0.3)

    ax3.set_xlim(0, max(data["t"]))
    ax3.set_ylim(min(data["omega"]) * 1.1, max(data["omega"]) * 1.1)
    ax3.set_xlabel("Time (s)")
    ax3.set_ylabel("Angular velocity (rad/s)")
    ax3.set_title("Angular Velocity vs Time")
    ax3.grid(True, linestyle="--", alpha=0.3)

    rod, = ax1.plot([], [], color="white", linewidth=2)
    bob, = ax1.plot([], [], "o", color="cyan", markersize=12)
    trail, = ax1.plot([], [], color="cyan", linewidth=1, alpha=0.3)
    angle_line, = ax2.plot([], [], color="orange", linewidth=2)
    omega_line, = ax3.plot([], [], color="cyan", linewidth=2)

    def update(frame):
        """Update pendulum rod, bob, trail, and chart lines per frame."""
        x, y = data["x"][frame], data["y"][frame]
        rod.set_data([0, x], [0, y])
        bob.set_data([x], [y])
        trail.set_data(data["x"][:frame], data["y"][:frame])
        angle_line.set_data(data["t"][:frame], data["theta"][:frame])
        omega_line.set_data(data["t"][:frame], data["omega"][:frame])
        return rod, bob, trail, angle_line, omega_line

    total_frames = len(data["t"])
    interval_ms = max(1, int(1000 * data["t"][-1] / total_frames / 2))

    ani = animation.FuncAnimation(
        fig, update, frames=total_frames, interval=interval_ms, blit=True
    )

    plt.tight_layout()
    output_path = os.path.join("outputs", "pendulum.gif")
    ani.save(output_path, writer="pillow", fps=60)
    print(f"\n  Animation saved → {output_path}")
    plt.show()