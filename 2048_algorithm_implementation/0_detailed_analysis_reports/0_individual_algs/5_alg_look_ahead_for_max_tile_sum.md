# 2048 Algorithm Performance Report

### Overview  
This report presents the performance summary of a 2048-playing algorithm over the course of **200 test games**. The algorithm attempts to maximize score and tile values using a strategic decision-making process. The following insights and statistics were collected through analysis of the gameplay logs.

---
### Algorithm Working
This algorithm looks upto **four moves ahead**, And in each scenerio it generates **ONLY ONE case of random 2/4 spawning.** That Means it potentially checks at **Max 64 different possibilities** for each move. And the **score** for **each possibility is the sum of square of individual elements for each of the 4 moves in a possibility.**

**Square is used** here to **amplify **the **weight** of **larger numbers** and hence reaching **larger outcomes.**






---

### General Statistics

- **Total Games Analyzed:** 200  
- **Average Moves Per Game:** 754.82  
- **Average Final Score:** 11,053.85  
- **Most Common Largest Tile Reached:** 1024  
- **Maximum Score Achieved:** 25,062  
- **Maximum Moves in a Single Game:** 1,424  

These numbers indicate a highly consistent and strategic algorithm capable of sustaining long games and reaching high-scoring outcomes.

---

### Largest Tile Distribution

The largest tile achieved at the end of each game offers a direct reflection of the algorithm’s efficiency and depth of planning. Here is the breakdown:

| Largest Tile | Number of Games | Percentage |
|--------------|------------------|-------------|
| 128          | 1                | 0.5%        |
| 256          | 1                | 0.5%        |
| 512          | 64               | 32.0%       |
| 1024         | 122              | 61.0%       |
| 2048         | 12               | 6.0%        |

The majority of games (61%) ended with a 1024 tile as the maximum, showcasing consistent progress toward the end-game tiles. Notably, **6% of games** managed to reach **2048**, which is a strong indicator of the ***algorithm’s potential to win.***

---
### Score vs Moves
![Score vs Moves](https://drive.google.com/uc?id=157-SiitJha3C3_q8ovbWQcEtmj9ClRXg)

This plot shows the correlation between the total number of moves and the final scores achieved across multiple games. A general upward trend suggests that games with more moves tend to yield higher scores, reflecting the algorithm’s long-term score-optimization capability.

---

### Min, Max, and Avg Score vs Moves
![Min, Max, and Avg Score vs Moves](https://drive.google.com/uc?id=15GIgJ05l8utEoUCU_Q4c8dMUI7sn9DkT)

This graph illustrates how score boundaries (min, max, and average) evolve as the game progresses. It provides insight into score consistency and the variability introduced with longer games.

---

### Max Moves Survival
![Max Moves Survival](https://drive.google.com/uc?id=1HtUW5a0fP8xHDjqp05mzcjoqKMGEBKWo)

This histogram captures how many games reached certain move counts. It’s useful for evaluating how often the algorithm sustains long-running games, which is crucial for reaching higher tile values like 2048.

---

### Final Scores vs Number of Games
![Final Scores vs Number of Games](https://drive.google.com/uc?id=1_qjV4AzgkogNCjROeiSRuxv1VORhba55)

This chart shows the distribution of final scores across all test runs. It helps identify how often high-scoring games occurred and whether there are performance outliers.

---

### Largest Tiles vs Number of Games
![Largest Tiles vs Number of Games](https://drive.google.com/uc?id=1lRJZnrAcGJ-r_b32zt9j0trWncNdKw0O)

Here, we analyze how frequently each tile  appeared as the highest achieved tile per game. This offers a solid metric of how effectively the algorithm progresses in the 2048 hierarchy.

---

### Average Score Progression per Move
![Average Score Progression per Move](https://drive.google.com/uc?id=1yPEwiazlX4wG4G0mhcGydpc36Fp_cwPt)

This graph demonstrates the cumulative average score growth as the number of moves increases. It's an excellent way to visualize scoring efficiency per move and to identify diminishing returns or scoring plateaus.


---
### Interpretation

- The **average score** of over 11,000 suggests that the algorithm performs well across long runs and prioritizes score optimization effectively.
- Reaching **1024 in over 60% of games** highlights a stable and balanced move-selection strategy.
- The fact that **only 0.5%** of games capped at 128 or 256 tiles shows that early-game failure is extremely rare.
- **2048** was achieved in a non-trivial portion of the games, which is impressive and likely tied to high move counts and good decision-making depth.

---

### Next Steps

- Further tuning could be done to **increase the rate of reaching 2048 or beyond**, possibly through deeper lookahead or tile-merging heuristics.

---
