import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.animation import FuncAnimation

# নাম: (x, y, রং, কাজ)
N = {
    "MS":  (1.2, 5.5, "#4FC3F7", "Mobile Station\nUser device"),
    "BTS": (3.9, 5.5, "#81C784", "Radio link\nwith MS"),
    "BSC": (6.6, 5.5, "#FFD54F", "Controls\nBTS"),
    "MSC": (9.8, 5.5, "#E57373", "Call switching\n& mobility"),
    "EIR": (2.2, 2.2, "#BA68C8", "Checks IMEI\n(phone valid?)"),
    "VLR": (5.2, 2.2, "#BA68C8", "Temporary\nlocation data"),
    "HLR": (8.2, 2.2, "#BA68C8", "Permanent\nsubscriber data"),
    "AuC": (10.9, 2.2, "#BA68C8", "Authentication\nkey data"),
    "Other Networks": (9.8, 7.2, "#B0BEC5", "Other networks\n(Internet, PSTN, etc.)")
}

# Communication flow: (কোথা থেকে, কোথায়, কাজ)
S = [("MS", "BTS", "Call request (radio)"),
     ("BTS", "BSC", "Forward request"),
     ("BSC", "MSC", "Send to core network"),
     ("MSC", "VLR", "Where is the user? (temporary data)"),
     ("MSC", "HLR", "Is subscriber valid? (permanent data)"),
     ("MSC", "AuC", "Authenticate SIM (key check)"),
     ("MSC", "EIR", "Is the phone allowed? (IMEI check)"),
     ("MSC", "BSC", "All OK, connect the call"),
     ("BSC", "BTS", "Assign radio channel"),
     ("BTS", "MS", "Call connected"),
     ("MSC", "Other Networks", "Connect to other networks")]

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor("#F5F7FA")
ax.set(xlim=(0, 12), ylim=(0, 8)); ax.axis("off")
ax.set_title("GSM Network Architecture & Call Flow", fontsize=17, weight="bold")

# লাইন (সংযোগ)
for a, b in [("MS", "BTS"), ("BTS", "BSC"), ("BSC", "MSC"), ("MSC", "Other Networks")] + [("MSC", d) for d in ("VLR", "HLR", "AuC", "EIR")]:
    ax.plot([N[a][0], N[b][0]], [N[a][1], N[b][1]], c="gray", lw=2, zorder=1)

# বাক্স
box = {}
for k, (x, y, c, txt) in N.items():
    box[k] = FancyBboxPatch((x - 1.05, y - 0.6), 2.1, 1.2, boxstyle="round,pad=0.03",
                            fc=c, ec="black", lw=1.5, zorder=2)
    ax.add_patch(box[k])
    ax.text(x, y + 0.25, k, ha="center", va="center", fontsize=13, weight="bold", zorder=3)
    ax.text(x, y - 0.2, txt, ha="center", va="center", fontsize=8.5, zorder=3)

dot, = ax.plot([], [], "o", c="red", mec="black", ms=15, zorder=5)
info = ax.text(6, 0.7, "", ha="center", fontsize=13, weight="bold",
               bbox=dict(boxstyle="round", fc="white", ec="gray"))

F = 20  # প্রতি ধাপে frame সংখ্যা
def update(f):
    s, t = divmod(f, F)
    a, b, msg = S[s]
    (x1, y1), (x2, y2) = N[a][:2], N[b][:2]
    dot.set_data([x1 + (x2 - x1) * t / (F - 1)], [y1 + (y2 - y1) * t / (F - 1)])
    info.set_text(f"Step {s+1}: {a} → {b}\n{msg}")
    for k, p in box.items():
        p.set_linewidth(4.5 if k in (a, b) else 1.5)

ani = FuncAnimation(fig, update, frames=len(S) * F, interval=40)
plt.tight_layout(); plt.show()