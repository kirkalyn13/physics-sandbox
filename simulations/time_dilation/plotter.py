import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os


def plot_results(sr: dict, grav: dict, label: str) -> None:
    """
    Animate special and gravitational time dilation curves across their sweep ranges.
    Saves animation to outputs/ and displays it.
    """
    os.makedirs("outputs", exist_ok=True)
    plt.style.use("dark_background")

    fig = plt.figure(figsize=(16, 10))
    fig.suptitle(label, fontsize=14)

    gs = fig.add_gridspec(2, 2, hspace=0.4, wspace=0.35)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[0, 1])
    ax4 = fig.add_subplot(gs[1, 1])

    ax1.set_xlim(0, max(sr["v_fractions"]))
    ax1.set_ylim(0, max(sr["lorentz"]) * 1.05)
    ax1.set_xlabel("Velocity (fraction of c)")
    ax1.set_ylabel("Lorentz factor γ")
    ax1.set_title("Lorentz Factor vs Velocity")
    ax1.grid(True, linestyle="--", alpha=0.3)

    ax2.set_xlim(0, max(sr["v_fractions"]))
    ax2.set_ylim(0, 1.05)
    ax2.set_xlabel("Velocity (fraction of c)")
    ax2.set_ylabel("Traveller time / Observer time")
    ax2.set_title("Time Ratio vs Velocity")
    ax2.grid(True, linestyle="--", alpha=0.3)
    ax2.axhline(y=1.0, color="white", linewidth=0.5, linestyle="--", alpha=0.4)

    ax3.set_xlim(min(grav["radii"]), max(grav["radii"]))
    ax3.set_ylim(min(grav["dilation"]) * 0.999, 1.001)
    ax3.set_xlabel("Distance from center (m)")
    ax3.set_ylabel("Time dilation factor")
    ax3.set_title("Gravitational Time Dilation vs Radius")
    ax3.grid(True, linestyle="--", alpha=0.3)
    ax3.axhline(y=1.0, color="white", linewidth=0.5, linestyle="--", alpha=0.4)

    ax4.set_xlim(0, max(sr["v_fractions"]))
    ax4.set_ylim(0, 1.05)
    ax4.set_xlabel("Velocity (fraction of c)")
    ax4.set_ylabel("Time dilation factor")
    ax4.set_title("Special vs Gravitational (normalised)")
    ax4.grid(True, linestyle="--", alpha=0.3)

    lorentz_line, = ax1.plot([], [], color="cyan", linewidth=2)
    time_ratio_line, = ax2.plot([], [], color="orange", linewidth=2)
    grav_line, = ax3.plot([], [], color="magenta", linewidth=2)
    sr_norm_line, = ax4.plot([], [], color="cyan", linewidth=2, label="Special")
    grav_norm_line, = ax4.plot([], [], color="magenta", linewidth=2, label="Gravitational")
    ax4.legend(loc="lower left", fontsize=9)

    grav_normalised = np.interp(
        sr["v_fractions"],
        np.linspace(0, 1, len(grav["dilation"])),
        grav["dilation"],
    )

    total_frames = len(sr["v_fractions"])

    def update(frame):
        """Update all four chart lines to current frame index."""
        lorentz_line.set_data(sr["v_fractions"][:frame], sr["lorentz"][:frame])
        time_ratio_line.set_data(sr["v_fractions"][:frame], sr["time_ratio"][:frame])
        grav_line.set_data(grav["radii"][:frame], grav["dilation"][:frame])
        sr_norm_line.set_data(sr["v_fractions"][:frame], sr["time_ratio"][:frame])
        grav_norm_line.set_data(sr["v_fractions"][:frame], grav_normalised[:frame])
        return lorentz_line, time_ratio_line, grav_line, sr_norm_line, grav_norm_line

    step = 5
    frames = range(0, total_frames, step)
    interval_ms = 16

    ani = animation.FuncAnimation(
        fig, update, frames=frames, interval=interval_ms, blit=True
    )

    output_path = os.path.join("outputs", "time_dilation.gif")
    ani.save(output_path, writer="pillow", fps=60)
    print(f"\n  Animation saved → {output_path}")
    plt.show()