import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)

# Create a figure with 3 subplots (3 rows, 1 column)
fig, axs = plt.subplots(1, 3, figsize=(8,2))  # 3 rows, 1 column

# --- First subplot ---
axs[0].plot(x, np.sin(x), color='blue')
axs[0].set_title("Sine Wave")
axs[0].grid(True)

# --- Second subplot ---
axs[1].plot(x, np.cos(x), color='green')
axs[1].set_title("Cosine Wave")
axs[1].grid(True)

# --- Third subplot ---
axs[2].plot(x, np.tan(x), color='red')
axs[2].set_title("Tangent Wave")
axs[2].set_ylim(-10, 10)  # limit y for tan
axs[2].grid(True)

# Automatically adjust spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
