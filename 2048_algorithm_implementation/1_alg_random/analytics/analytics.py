import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Path where CSV files are stored
csv_folder = "../logs/"  # Change this to your actual folder path

# Read all CSV files
csv_files = sorted(glob.glob(os.path.join(csv_folder, "*_seed.csv")))

# Initialize a dictionary to store data
all_data = []

# Process each file
for file in csv_files:
    df = pd.read_csv(file)
    df["File"] = os.path.basename(file)  # Store filename for reference
    all_data.append(df)

# Combine all files into one DataFrame
full_data = pd.concat(all_data, ignore_index=True)

# Convert 'Move' and 'Score' to numeric for analysis
full_data["Move"] = pd.to_numeric(full_data["Move"])
full_data["Score"] = pd.to_numeric(full_data["Score"])

# Plot Score vs Move
plt.figure(figsize=(10, 6))
for file in full_data["File"].unique():
    subset = full_data[full_data["File"] == file]
    plt.plot(subset["Move"], subset["Score"], alpha=0.5)  # Faded lines for all runs

plt.xlabel("Move Number")
plt.ylabel("Score")
plt.title("Score vs Move for 500 Test Cases")
plt.grid(True)

# Save the figure
# plt.savefig("score_vs_move.png", dpi=300)
plt.show()

# Compute statistics
summary_stats = full_data.groupby("Move")["Score"].agg(["mean", "max", "min"])
print(summary_stats)

# Save summary statistics to CSV
summary_stats.to_csv("score_summary.csv")

print("Saved as score_summary.csv")

