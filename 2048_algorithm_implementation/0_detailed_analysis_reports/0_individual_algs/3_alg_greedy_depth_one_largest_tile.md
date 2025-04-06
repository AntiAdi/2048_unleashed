# 2048 Algorithm Implementation  
## Algorithm: Greedy for Largest Tile Combination with Depth One

---

### Overview

This report presents the results of running the algorithm on **500 independent and random test cases**. The data collected includes move count, score progression, and tile merging behavior, with the goal of understanding how effectively the algorithm performs over time.

---

## Algorithm Working 
The algorithm simply **simulates the next four possible moves** and checks for the **largest tile combination** amongst those, Whilst **disregarding the score change** as in the previous algorithm.



---

### Summary Statistics

- **Total Games Analyzed:** 500  
- **Average Moves Per Game:** 310.02  
- **Average Final Score:** 1739.78  
- **Most Common Largest Tile Reached:** 256  
- **Max Score Achieved:** 5068  
- **Max Moves in a Single Game:** 1784  

These statistics indicate that the algorithm is capable of sustaining longer games with relatively high tile values, though it may not at all reach extreme scores (Not even 1024). A large number of games concluded with 256 as the maximum tile, suggesting room for optimization in deeper planning.

---
### Largest Tile Distribution

This section presents how frequently each tile was the highest achieved in the analyzed games. It provides insights into the algorithm's merging efficiency and typical performance limits.

| Largest Tile | Games Reached | Percentage (%) |
|--------------|----------------|----------------|
| 32           | 1              | 0.2%           |
| 64           | 49             | 9.8%           |
| 128          | 216            | 43.2%          |
| 256          | 221            | 44.2%          |
| 512          | 13             | 2.6%           |

#### Observations:
- The majority of games reached **128 or 256**, with **over 87%** of runs ending in one of these two tiles.
- Only **2.6%** of the games reached **512**, indicating the algorithm occasionally achieves higher-level merges but lacks consistency in pushing further.
- Very few games peaked at **32** or **64**, suggesting most runs had a decent merging strategy and didn’t end prematurely.
- The balance between **128 and 256** as peak tiles shows a relatively stable mid-level performance, with frequent tile doubling in many sessions.

This breakdown helps evaluate how well the algorithm scales and where it tends to plateau, offering guidance for refining future strategies.



---

### Graphical Data Analysis

#### Score vs Moves for 500 Test Cases
![Score vs Moves for 500 Test Cases](https://drive.google.com/uc?id=1gcXax8Orl4fygVEKfZXW4qX9u8rCfkCW)

This line graph shows how the score evolves over time for each of the 500 test cases. While there's randomness in each run, we can still observe a general upward trend as more moves are made.



#### Max Moves vs Number of Games
![Max Moves vs Number of Games](https://drive.google.com/uc?id=1OlyZjJIzX5zhurM8QL4bifEFrrISXddK)

This graph reflects how long each game lasted in terms of total moves. Most games fall within a specific range, but there are outliers with significantly higher move counts.


#### Max, Min and Avg Scores vs Moves
![Max, Min and Avg Scores vs Moves](https://drive.google.com/uc?id=1zxDZp5wSgDltmbnvDYRtxKcLGXTpdB_e)

Here we compare the best, worst, and average scores at each move count. The average score rises steadily, showing consistent point accumulation. Max scores spike occasionally, usually after large merges.


#### Largest Tiles vs Number of Games
![Largest Tiles vs Number of Games](https://drive.google.com/uc?id=1QT2Oqcmsrz8ao16n4QZCVf-lCUCH0Dvk)

This chart displays how many times a particular tile was the largest one reached in a game. The tile 256 appears most often, indicating that the algorithm frequently reaches mid-level merges.


#### Final Scores vs Number of Games
![Final Scores vs Number of Games](https://drive.google.com/uc?id=1QTT2uTXBrpgyRMFNBhja69p45U1HQc-l)

This graph presents the final scores for all 500 games. Most scores cluster in the mid-to-lower range, with only a few games achieving high final scores above 4000.


#### Average Score vs Progression Per Move
![Average Score vs Progression Per Move](https://drive.google.com/uc?id=1LmQDfrcOBn22rbulc8XezZoJ9U1_jonz)

This graph focuses on the average score at each move index across all test cases. The curve starts off steep, then gradually flattens as the game progresses and the board becomes harder to manage.




---

### Key Insights

- **Game Longevity**  
  With an average of **310 moves per game**, the algorithm shows an ability to avoid early deadlocks, implying efficient tile movement and decent decision-making.

- **Scoring Trends**  
  The **average final score of 1739.78** shows consistent mid-level performance. Although not very high, the stability of scoring across games may reflect the algorithm's reliability rather than aggressiveness.

- **Tile Progression**  
  Most games capped at **256** as the largest tile, meaning the algorithm often struggles to chain merges beyond early exponential growth.

- **Outlier Games**  
  Some games reached scores exceeding **5000** or survived up to **1784 moves**, which are significant outliers. These show the potential of the algorithm under ideal conditions and suggest that tuning parameters or combining strategies could yield better consistency.

---

### Areas for Improvement

**Lookahead Depth**  
  Increasing the lookahead depth may help evaluate longer-term board states, leading to better planning for merges and maximizing opportunities.



---

### Conclusion

This algorithm demonstrates **strong survivability** but limited scoring potential. It manages to avoid premature terminations and produces consistent results. While the average largest tile is capped at 256, the data shows that with better foresight and smarter merge heuristics, there's significant room for improvement.

---

### Next Steps

- Compare with other algorithms using the same evaluation metrics.  
- Implement deeper lookahead with all tile spawn possibilities.  

---

