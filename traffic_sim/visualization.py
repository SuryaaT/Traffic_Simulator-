import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(sim, pos, filename="simulation.gif"):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        sim.step()

        # roads
        for r in sim.roads:
            x1, y1 = pos[r.start]
            x2, y2 = pos[r.end]
            ax.plot([x1, x2], [y1, y2], 'k-', linewidth=2)

        # junctions
        for j, (x, y) in pos.items():
            ax.plot(x, y, 'bo', markersize=6)
            ax.text(x, y + 0.15, j.id, ha='center')

        # vehicles
        for r in sim.roads:
            x1, y1 = pos[r.start]
            x2, y2 = pos[r.end]

            for v in r.vehicles:
                ratio = min(v.progress, 1)
                x = x1 + (x2 - x1) * ratio
                y = y1 + (y2 - y1) * ratio
                ax.plot(x, y, marker='o', color=v.color, markersize=6)

        ax.set_xlim(-1, 7)
        ax.set_ylim(-1, 7)
        ax.set_title(f"Time {sim.time}")

    # 🔥 UPDATED PART (LONGER + SMOOTH)
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=300,   # increased duration (~15 sec)
        interval=50   # keeps motion smooth
    )

    ani.save(filename, writer="pillow")
    print("Saved:", filename)