import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Create figure
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")


# Function to draw a box
def box(x, y, w, h, title, text, color):
    p = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor=color,
        edgecolor="black",
        linewidth=1.5
    )
    ax.add_patch(p)

    ax.text(x + w/2, y + h - 0.35, title,
            ha="center", va="center",
            fontsize=12, fontweight="bold")

    ax.text(x + w/2, y + h/2 - 0.15, text,
            ha="center", va="center",
            fontsize=9)


# Function to draw arrow
def arrow(x1, y1, x2, y2, label):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", linewidth=1.8)
    )

    ax.text(
        (x1 + x2)/2,
        (y1 + y2)/2 + 0.18,
        label,
        ha="center",
        fontsize=9
    )


# 1. Main GSM components
box(0.7, 5.5, 2.2, 1.2,
    "MS", "Mobile Station\nUser device", "#E8F4FD")

box(3.4, 5.5, 2.2, 1.2,
    "BTS", "Radio link\nwith MS", "#EAF7EA")

box(6.1, 5.5, 2.2, 1.2,
    "BSC", "Controls BTS\nradio resources", "#FFF4D6")

box(8.8, 5.5, 2.2, 1.2,
    "MSC", "Call & mobility\nswitching", "#FDECEC")


# 2. GSM databases and security units
box(3.0, 2.7, 2.2, 1.2,
    "HLR", "Permanent\nsubscriber data", "#F0E8FF")

box(5.5, 2.7, 2.2, 1.2,
    "VLR", "Temporary\nlocation data", "#F0E8FF")

box(8.0, 2.7, 2.2, 1.2,
    "AuC", "Authentication\nand key data", "#F0E8FF")

box(9.0, 0.8, 2.2, 1.2,
    "EIR", "IMEI / equipment\ncheck", "#F0E8FF")


# 3. Communication flow
arrow(2.9, 6.1, 3.4, 6.1, "Radio")
arrow(5.6, 6.1, 6.1, 6.1, "Control")
arrow(8.3, 6.1, 8.8, 6.1, "Core")

arrow(9.9, 5.5, 4.1, 3.9, "Subscriber info")
arrow(9.9, 5.5, 6.6, 3.9, "Location")
arrow(9.9, 5.5, 9.1, 3.9, "Auth.")
arrow(10.0, 5.5, 10.1, 2.0, "IMEI check")


# Title
ax.text(
    6, 7.5,
    "GSM Network Architecture",
    ha="center",
    fontsize=16,
    fontweight="bold"
)


# Main flow
ax.text(
    0.8, 0.25,
    "Main flow: MS → BTS → BSC → MSC\n"
    "MSC uses HLR, VLR, AuC and EIR for subscriber, mobility and security",
    fontsize=10
)

plt.tight_layout()
plt.show()