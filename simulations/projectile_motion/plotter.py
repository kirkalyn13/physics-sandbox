import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os


def plot_results(data: dict) -> None:
    """
    Animate trajectory arc and speed-vs-time using FuncAnimation.
    Saves animation to outputs/ and displays it.
    """
    os.makedirs("outputs", exist_ok=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(data["label"], fontsize=14)

    ax1.set_xlim(0, max(data["x"]) * 1.05)
    ax1.set_ylim(0, max(data["y"]) * 1.2)
    ax1.set_xlabel("Horizontal distance (m)")
    ax1.set_ylabel("Height (m)")
    ax1.set_title("Trajectory")
    ax1.grid(True, linestyle="--", alpha=0.5)

    ax2.set_xlim(0, max(data["t"]) * 1.05)
    ax2.set_ylim(min(data["speed"]) * 0.9, max(data["speed"]) * 1.05)
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Speed (m/s)")
    ax2.set_title("Speed vs Time")
    ax2.grid(True, linestyle="--", alpha=0.5)

    trail, = ax1.plot([], [], color="steelblue", linewidth=2)
    dot, = ax1.plot([], [], "o", color="steelblue", markersize=6)
    speed_line, = ax2.plot([], [], color="darkorange", linewidth=2)

    def update(frame):
        """Update both charts to frame index on each animation tick."""
        trail.set_data(data["x"][:frame], data["y"][:frame])
        dot.set_data([data["x"][frame - 1]], [data["y"][frame - 1]])
        speed_line.set_data(data["t"][:frame], data["speed"][:frame])
        return trail, dot, speed_line

    total_frames = len(data["t"])
    interval_ms = max(1, int(1000 * data["t"][-1] / total_frames / 2))

    ani = animation.FuncAnimation(
        fig, update, frames=total_frames, interval=interval_ms, blit=True
    )

    plt.tight_layout()
    output_path = os.path.join("outputs", "projectile_motion.gif")
    ani.save(output_path, writer="pillow", fps=60)
    print(f"\n  Animation saved → {output_path}")
    plt.show()