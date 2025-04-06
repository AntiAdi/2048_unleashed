import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv("score_summary.csv")  # Update this if needed

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(df["Move"], df["mean"], label="Average Score", color="blue", marker="o")

# Labels and title
plt.xlabel("Number of Moves")
plt.ylabel("Average Score")
plt.title("Average Score Progression per Move")
plt.legend()
plt.grid(True)



# Save the figure
plt.savefig("Average_Score_Progression_per_Move.png", dpi=300)


# Show the graph

plt.show()
