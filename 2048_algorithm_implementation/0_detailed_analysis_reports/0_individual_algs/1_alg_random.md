    # 2048 Algorithm Implementation

## Algorithm: Random

### Overview  
This report presents an analysis of 500 test runs of a random move-based 2048-solving algorithm. The collected data includes the number of moves per game, final scores, and the highest tile achieved. The aim is to evaluate the performance and identify trends in game outcomes.  

### Summary of Results  
- **Total Test Runs:** 500  
- **Average Moves Per Game:** 120.48  
- **Average Final Score:** 975.16  
- **Most Common Largest Tile Reached:** 128  
- **Max Score Achieved:** 2536  
- **Max Moves in a Single Game:** 252  

### Largest Tile Distribution

This distribution provides insights into the highest tile reached in each game, helping us understand how far the algorithm typically progresses before the game ends.

| Largest Tile | Games Reached | Percentage (%) |
|--------------|----------------|----------------|
| 16           | 1              | 0.2%           |
| 32           | 37             | 7.49%          |
| 64           | 166            | 33.6%          |
| 128          | 251            | 50.81%         |
| 256          | 39             | 7.89%          |

#### Observations:
- **128** was the most commonly reached tile, achieved in **over half the games** (50.81%), showing the algorithm has reliable mid-game performance.
- **33.6%** of the games ended at **64**, suggesting a moderate success rate in achieving decent merges.
- Only **7.89%** reached **256**, revealing a sharp drop-off after 128 and highlighting potential bottlenecks in late-game decision-making.
- The presence of early exits is minimal, with just **0.2%** stuck at **16** and **7.49%** at **32**, indicating generally stable early-game play.



## Data Visualizations  

### Score VS Number of Moves  
![Score vs Move](https://drive.google.com/uc?id=19L0RNMt4FiJZHod83CMX8cdGhMrMwOiI)  

### Min, Max, and Average Score vs Number of Moves  
![Min, Max and Average Score vs Moves](https://drive.google.com/uc?id=1aitNlFUgE74YRXgwxovkswLYAWGb7YzF)  

### Moves Survived vs Number of Games  
![Moves Survived vs Number of Games](https://drive.google.com/uc?id=1WXp89ZKQ72mLtBTTGg_WadjBWJ1GQwkh)  

### Final Score vs Number of Games  
![Final Score vs Number of Games](https://drive.google.com/uc?id=18Gw5MYNLy7YciPh-WwJdOlSPRHj214tF) 

### Largest Tile vs Number of Games
![Largest Tile vs Number of Games](https://drive.google.com/uc?id=1Mweysa9zOwxKmN8IDlkPbo29d-xdSK63)


## Observations  
- The majority of games ended with a **128 tile** as the highest tile achieved, indicating that the tested algorithm struggles to reach higher tile values.  
- The **highest recorded score** of 2536 suggests that some runs performed significantly better than the average, possibly due to lucky tile placements.  
- The **maximum number of moves in a single game** (252) suggests that some sequences prolonged the game without necessarily improving the final score.  
- **Most number of games** had the **largest tile equal to 128**, Showcasing the **average** and **poor** performance of this algoithm.

## Next Steps  
- Conduct further analysis to compare different algorithm performances.  
- Utilize deeper lookahead strategies to improve decision-making.  
- Explore reinforcement learning or heuristic-based approaches for better results.  

This report serves as a baseline for refining 2048-solving strategies and optimizing game performance.  

