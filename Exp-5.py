import numpy as np, matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(1, 1000)
rss = lambda bs: 40 - 40 - 10*3*np.log10(abs(x - bs))   # Pt - PL0 - 10*n*log10(d)
R1, R2 = rss(0), rss(1000)

i = np.argmin(abs(R1 - R2)); h = x[i]
print("Handover Point:", h, "m | RSS:", round(R1[i], 2), "dBm")

fig, (a, b) = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle("Two-Cell Handover Simulation", fontsize=16, weight="bold")

# বাম: RSS graph
a.plot(x, R1, color="tab:blue", lw=2, label="Cell 1 (BS1)")
a.plot(x, R2, color="tab:red", lw=2, label="Cell 2 (BS2)")
a.axvspan(0, h, color="tab:blue", alpha=.08)
a.axvspan(h, 1000, color="tab:red", alpha=.08)
a.axvline(h, ls="--", c="gray", label=f"Handover ({h} m)")
a.set(xlabel="Mobile Position (m)", ylabel="RSS (dBm)", title="Signal Strength")
a.legend(); a.grid(alpha=.3)

dot1, = a.plot([], [], "ko", ms=9)                               # কালো: handover-এর আগে
dot2, = a.plot([], [], "o", c="gold", mec="k", ms=12, zorder=5)  # হলুদ: handover-এর পরে

# ডান: Cell map
t = np.linspace(0, 2*np.pi, 7)
for n, c in enumerate(["tab:blue", "tab:red"]):
    bs = n * 1000
    b.fill(bs + 500*np.cos(t), 500*np.sin(t), color=c, alpha=.15)
    b.plot(bs, 0, "^", color=c, ms=14)
    b.text(bs, -90, f"BS{n+1}", ha="center", weight="bold")
b.axvline(h, ls="--", c="gray")
b.set(xlim=(-600, 1600), ylim=(-600, 600), title="Cell Map")
b.set_aspect("equal"); b.grid(alpha=.3)
mobile, = b.plot([], [], "o", c="green", ms=12)
status = b.text(500, 520, "", ha="center", fontsize=13, weight="bold")

def update(k):
    mobile.set_data([x[k]], [0])
    left = x[k] < h
    if left:
        dot1.set_data([x[k]], [R1[k]]); dot2.set_data([], [])
    else:
        dot1.set_data([], []); dot2.set_data([x[k]], [R2[k]])
    status.set_text("Connected: BS1" if left else "Handover: BS1 -> BS2")
    status.set_color("tab:blue" if left else "tab:red")
    return mobile, dot1, dot2, status

ani = FuncAnimation(fig, update, frames=range(0, len(x), 5), interval=20, repeat=False)
plt.tight_layout(); plt.show()