import pandas as pd
import glob
from collections import Counter

# Path to CSV files
csv_files = glob.glob("../logs/*.csv")  # Modify path as needed

# Initialize lists to store data
move_counts = []
final_scores = []
largest_tiles = []

def extract_data(file):
    df = pd.read_csv(file)
    total_moves = len(df) - 1
    final_score = df.iloc[-1]['Score']
    largest_tile = df.iloc[-1]['Largest_Tile']
    return total_moves, final_score, largest_tile

# Extract data from each CSV
for file in csv_files:
    moves, score, tile = extract_data(file)
    move_counts.append(moves)
    final_scores.append(score)
    largest_tiles.append(tile)

# Summary statistics
total_games = len(csv_files)
avg_moves = round(sum(move_counts) / total_games, 2)
avg_score = round(sum(final_scores) / total_games, 2)
max_score = max(final_scores)
max_moves = max(move_counts)
most_common_tile = max(set(largest_tiles), key=largest_tiles.count)

# Score thresholds
score_thresholds = [512, 1024, 2048, 4096]
score_counts = {s: sum(1 for x in final_scores if x >= s) for s in score_thresholds}
score_percentages = {s: round((count / total_games) * 100, 2) for s, count in score_counts.items()}

# Tile distribution
tile_counter = Counter(largest_tiles)
tile_lines = []
for tile, count in sorted(tile_counter.items()):
    percent = round((count / total_games) * 100, 2)
    tile_lines.append(f"- {tile}: {count} games ({percent}%)")

# Report generation
report = f"""
2048 Algorithm Performance Report
=================================

Total Games Analyzed: {total_games}
Average Moves Per Game: {avg_moves}
Average Final Score: {avg_score}
Most Common Largest Tile Reached: {most_common_tile}
Max Score Achieved: {max_score}
Max Moves in a Single Game: {max_moves}


Largest Tile Distribution:
--------------------------
""" + "\n".join(tile_lines) + "\n"

# Save to file
with open("2048_report.txt", "w") as f:
    f.write(report)

print("Detailed report saved to 2048_report.txt")
