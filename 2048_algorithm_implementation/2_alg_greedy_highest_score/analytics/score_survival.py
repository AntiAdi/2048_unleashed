import pandas as pd
import matplotlib.pyplot as plt
import glob

# Path to CSV files (Modify if needed)
csv_files = glob.glob("../logs/*.csv")

# List to store final scores
final_scores = []

# Loop through all CSV files
for file in csv_files:
    df = pd.read_csv(file)
    final_scores.append(df["Score"].iloc[-1])  # Last row's Score

# Convert to DataFrame
df_scores = pd.DataFrame(final_scores, columns=["Final Score"])

# Plot Histogram
plt.figure(figsize=(10, 5))
plt.hist(df_scores["Final Score"], bins=20, edgecolor="black", alpha=0.7, color="green")

# Labels and title
plt.xlabel("Final Score")
plt.ylabel("Number of Games")
plt.title("Distribution of Final Scores in 500 Games")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the graph
plt.show()
