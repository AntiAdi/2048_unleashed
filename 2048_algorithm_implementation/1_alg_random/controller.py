import subprocess
import os



# Number of Test Runs
test_runs = 1000






# Path to config.py . DO NOT CHANGE.
config_file = "program_files/config.py"


# Ensuring the logs directory exists.
log_dir = os.path.abspath("logs")
os.makedirs(log_dir, exist_ok=True)



# Function to update seed and log file name in config.py.
# We use this to create seperate log file for each test run.
def update_config(seed):
    with open(config_file, "r") as file:
        lines = file.readlines()
    
    with open(config_file, "w") as file:
        for line in lines:
            if "random_seed =" in line:
                file.write(f"random_seed = {seed}\n")  # Replace X with the new seed
            elif "log_filename =" in line:
                file.write(f'log_filename = "{log_dir}/{seed}_seed.csv"\n') # Update filename
            else:
                file.write(line)


"""
    IMPORTANT : Change Number of Seeds as Per your requirements in range() function.
"""


# Loop through required number of Seeds. !
for seed in range(1, 1+test_runs):
    print(f"Running with seed {seed}...")
    
    update_config(seed)  # Update the config file
    
    # Run main.py
    subprocess.run(["python", "./program_files/main.py"])  

print("All runs completed!\nRemoving Pycache.")

if os.name=="nt" :   
    print("Your Windows Suck ! Clear It Yourself !") 
else :
    os.system("rm -vr __pycache__")
    os.system("rm -vr ./program_files/__pycache__")