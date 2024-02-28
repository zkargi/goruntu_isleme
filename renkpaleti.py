import matplotlib.pyplot as plt
import numpy as np

def plot_color_palette(colors):
    n = len(colors)
    _, ax = plt.subplots(1, 1, figsize=(n, 1))
    ax.imshow([colors], aspect='auto', extent=[0, n, 0, 1])
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

# Örnek renkler (RGB formatında)
colors = [
    (255, 0, 0),  # Kırmızı
    (0, 255, 0),  # Yeşil
    (0, 0, 255),  # Mavi
    (255, 255, 0),  # Sarı
    (0, 255, 255),  # Cyan
    (255, 0, 255)   # Magenta
]


# 0-1 arasına normalize edilen renkler
normalized_colors = np.array(colors) / 255.0

plot_color_palette(normalized_colors)
