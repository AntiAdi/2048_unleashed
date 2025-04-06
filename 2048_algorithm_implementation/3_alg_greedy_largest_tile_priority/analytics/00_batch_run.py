import subprocess

def run_analytics_batch():
    # Step 1: Run the first script and wait for it to finish
    print("Running: python ./analytics.py")
    subprocess.run(["python", "./analytics.py"], check=True)
    print("Finished: analytics.py")

    # Step 2: Run remaining scripts in parallel
    scripts = [
        "avg_score_and_avg_moves.py",
        "largest_tile_vs_num_of_games.py",
        "moves_survival.py",
        "report_generator.py",
        "score_min_max_per_move.py",
        "score_survival.py"
    ]

    processes = []
    for script in scripts:
        print(f"Launching: python ./{script}")
        proc = subprocess.Popen(["python", f"./{script}"])
        processes.append(proc)

    # Wait for all background scripts to complete
    for proc in processes:
        proc.wait()
        print(f"{proc.args[-1]} finished.")

    print("All scripts completed successfully.")

# Run it
if __name__ == "__main__":
    run_analytics_batch()
