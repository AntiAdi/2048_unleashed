import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv("score_summary.csv")

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df["Move"], df["mean"], label="Mean Score", color="blue", marker="o")
plt.plot(df["Move"], df["max"], label="Max Score", color="green", linestyle="dashed")
plt.plot(df["Move"], df["min"], label="Min Score", color="red", linestyle="dotted")

# Labels and title
plt.xlabel("Move Number")
plt.ylabel("Score")
plt.title("Score Progression per Move")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
