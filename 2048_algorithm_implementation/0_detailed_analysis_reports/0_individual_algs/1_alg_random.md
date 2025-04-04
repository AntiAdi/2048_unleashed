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

## Data Visualizations  

### Score VS Number of Moves  
![Score vs Move](https://drive.google.com/uc?id=19L0RNMt4FiJZHod83CMX8cdGhMrMwOiI)  

### Min, Max, and Average Score vs Number of Moves  
![Min, Max and Average Score vs Moves](https://drive.google.com/uc?id=1aitNlFUgE74YRXgwxovkswLYAWGb7YzF)  

### Moves Survived vs Number of Games  
![Moves Survived vs Number of Games](https://drive.google.com/uc?id=1WXp89ZKQ72mLtBTTGg_WadjBWJ1GQwkh)  

### Final Score vs Number of Games  
![Final Score vs Number of Games](https://drive.google.com/uc?id=18Gw5MYNLy7YciPh-WwJdOlSPRHj214tF)  

## Observations  
- The majority of games ended with a **128 tile** as the highest tile achieved, indicating that the tested algorithm struggles to reach higher tile values.  
- The **highest recorded score** of 2536 suggests that some runs performed significantly better than the average, possibly due to lucky tile placements.  
- The **maximum number of moves in a single game** (252) suggests that some sequences prolonged the game without necessarily improving the final score.  

## Next Steps  
- Conduct further analysis to compare different algorithm performances.  
- Utilize deeper lookahead strategies to improve decision-making.  
- Explore reinforcement learning or heuristic-based approaches for better results.  

This report serves as a baseline for refining 2048-solving strategies and optimizing game performance.  

