import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Path to your CSV files
csv_dir = '../logs/'  # Replace with actual path
num_files = 500

largest_tiles = []

for i in range(1, num_files + 1):
    file_path = os.path.join(csv_dir, f'{i}_seed.csv')
    if not os.path.exists(file_path):
        continue

    df = pd.read_csv(file_path)
    if not df.empty and 'Largest_Tile' in df.columns:
        largest_tiles.append(df['Largest_Tile'].iloc[-1])

# Count occurrences of each largest tile
tile_counts = Counter(largest_tiles)

# Sort by tile value
sorted_tiles = sorted(tile_counts.items())

# Separate into X and Y for plotting
tiles, game_counts = zip(*sorted_tiles)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(tiles, game_counts, color='skyblue')
plt.xlabel('Maximum Tile Reached')
plt.ylabel('Number of Games')
plt.title('Maximum Tile Reached vs Number of Games')
plt.xticks(tiles)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()



# Save the figure
plt.savefig("largest_tile_vs_num_games.png", dpi=300)
plt.show()
