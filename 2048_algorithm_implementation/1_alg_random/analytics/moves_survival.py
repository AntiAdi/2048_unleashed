import pandas as pd
import matplotlib.pyplot as plt
import glob

# Path to CSV files (Modify if needed)
csv_files = glob.glob("../logs/*.csv")

# List to store move counts
move_counts = []

# Loop through all CSV files
for file in csv_files:
    with open(file, "r") as f:
        lines = f.readlines()
        move_counts.append(len(lines) - 1)  # Exclude header

# Convert to DataFrame
df_moves = pd.DataFrame(move_counts, columns=["Moves Survived"])

# Plot Histogram
plt.figure(figsize=(10, 5))
plt.hist(df_moves["Moves Survived"], bins=30, edgecolor="black", alpha=0.7, color="blue")

# Labels and title
plt.xlabel("Total Moves Survived")
plt.ylabel("Number of Games")
plt.title("Distribution of Moves Survived by Games")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the graph
plt.show()
