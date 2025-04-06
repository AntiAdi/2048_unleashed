import pandas as pd
import glob

# Path to CSV files (Modify accordingly)
csv_files = glob.glob("../logs/*.csv")  # Assumes all files are in the same directory

# Initialize lists to store results
move_counts = []
final_scores = []
largest_tiles = []

def extract_data(file):
    df = pd.read_csv(file)
    total_moves = len(df) - 1  # Moves count is line count - 1
    final_score = df.iloc[-1]['Score']  # Last recorded score
    largest_tile = df.iloc[-1]['Largest_Tile']  # Largest tile at end of game
    return total_moves, final_score, largest_tile

# Process all CSV files
for file in csv_files:
    moves, score, tile = extract_data(file)
    move_counts.append(moves)
    final_scores.append(score)
    largest_tiles.append(tile)

# Create summary statistics
summary = {
    "Total Games Analyzed": len(csv_files),
    "Average Moves Per Game": round(sum(move_counts) / len(move_counts), 2),
    "Average Final Score": round(sum(final_scores) / len(final_scores), 2),
    "Most Common Largest Tile Reached": max(set(largest_tiles), key=largest_tiles.count),
    "Max Score Achieved": max(final_scores),
    "Max Moves in a Single Game": max(move_counts)
}

# Generate report text
report = f"""
2048 Algorithm Performance Report
=================================

Total Games Analyzed: {summary['Total Games Analyzed']}
Average Moves Per Game: {summary['Average Moves Per Game']}
Average Final Score: {summary['Average Final Score']}
Most Common Largest Tile Reached: {summary['Most Common Largest Tile Reached']}
Max Score Achieved: {summary['Max Score Achieved']}
Max Moves in a Single Game: {summary['Max Moves in a Single Game']}

"""

# Save report to a text file
with open("2048_report.txt", "w") as f:
    f.write(report)

print("Report generated: 2048_report.txt")
