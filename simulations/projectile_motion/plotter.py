import matplotlib.pyplot as plt
import os


def plot_results(data: dict) -> None:
    """
    Render trajectory arc and speed-vs-time charts.
    Saves to outputs/ and displays the figure.
    """
    os.makedirs("outputs", exist_ok=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(data["label"], fontsize=14)

    ax1.plot(data["x"], data["y"], color="steelblue", linewidth=2)
    ax1.set_xlabel("Horizontal distance (m)")
    ax1.set_ylabel("Height (m)")
    ax1.set_title("Trajectory")
    ax1.set_ylim(bottom=0)
    ax1.grid(True, linestyle="--", alpha=0.5)

    ax2.plot(data["t"], data["speed"], color="darkorange", linewidth=2)
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Speed (m/s)")
    ax2.set_title("Speed vs Time")
    ax2.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    output_path = os.path.join("outputs", "projectile_motion.png")
    plt.savefig(output_path, dpi=150)
    print(f"\n  Chart saved → {output_path}")
    plt.show()