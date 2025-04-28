import csv
import itertools
from main import play_game_with_weights
from fn import dummy_add_2_or_4






def run_weight_tuner(num_runs_per_config=5, top_n=5, output_csv="tuning_results.csv"):
    # Define the ranges for the weight combinations
    empty_range = [1000, 3000, 5000]
    smooth_range = [5, 15, 30]
    monotonicity_range = [10, 30, 60]
    weighted_range = [0.001, 0.002, 0.005]
    corner_range = [1000, 3000, 5000]
    value_square_range = [0.0005, 0.001, 0.002]

    # Collect all possible weight combinations
    weight_combinations = []
    for empty in empty_range:
        for smooth in smooth_range:
            for monotonicity in monotonicity_range:
                for weighted in weighted_range:
                    for corner in corner_range:
                        for value_square in value_square_range:
                            weights = {
                                'empty': empty,
                                'smooth': smooth,
                                'monotonicity': monotonicity,
                                'weighted': weighted,
                                'corner': corner,
                                'value_square': value_square
                            }
                            weight_combinations.append(weights)

    # Log the results
    results = []

    for idx, weights in enumerate(weight_combinations):
        avg_score, max_tile = play_game_with_weights(weights, num_runs=num_runs_per_config)

        results.append({
            'Weights': weights,
            'Avg Score': avg_score,
            'Max Tile': max_tile
        })

        print(f"[{idx + 1}/{len(weight_combinations)}] Avg: {avg_score} | Max Tiles: {max_tile} | Weights: {weights}")

    # Sort results by Avg Score and print top configurations
    sorted_results = sorted(results, key=lambda x: x['Avg Score'], reverse=True)
    print("Top Results:")
    for i in range(top_n):
        print(f"#{i+1}: Avg Score = {sorted_results[i]['Avg Score']} | Max Tiles = {sorted_results[i]['Max Tile']}")
        print(f"  {sorted_results[i]['Weights']}")

    # Log the results to CSV
    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Weights', 'Avg Score', 'Max Tile'])
        writer.writeheader()
        for result in sorted_results:
            writer.writerow(result)



if __name__ == "__main__":
    run_weight_tuner(num_runs_per_config=5, top_n=5, output_csv="tuning_results.csv")