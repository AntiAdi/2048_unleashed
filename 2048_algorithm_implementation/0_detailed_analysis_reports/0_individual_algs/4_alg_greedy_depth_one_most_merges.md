# 2048 Algorithm Report  
**Algorithm Tested:** One Depth Greedy for  Most Merges 
**Total Test Cases:** 500  

---
## Algorithm Working 
This algorithm simply calculates the number of merges for each of the next four possible moves and chooses to run the one having the most number of tile merges.


---

## Summary Statistics

| Metric                         | Value      |
|-------------------------------|------------|
| Total Games Analyzed          | 500        |
| Average Moves Per Game        | 333.97     |
| Average Final Score           | 1566.23    |
| Most Common Largest Tile      | 128        |
| Max Score Achieved            | 4448       |
| Max Moves in a Single Game    | 1771       |

---

### Largest Tile Distribution

This section outlines how often each tile was the highest tile achieved across all games analyzed. It gives a clear sense of the algorithm’s ability to build up larger tiles and its general performance in long-term play.

| Largest Tile | Games Reached | Percentage (%) |
|--------------|----------------|----------------|
| 32           | 4              | 0.8%           |
| 64           | 71             | 14.2%          |
| 128          | 237            | 47.4%          |
| 256          | 184            | 36.8%          |
| 512          | 4              | 0.8%           |

#### Observations:
- Nearly **half of all games** capped at tile **128**, indicating a moderate performance threshold.
- **256** was reached in over a **third** of the games, suggesting occasional deeper progress.
- Very **few games** managed to reach **512**, highlighting room for improvement in long-term tile merging efficiency.
- The low frequency of smaller tiles (32 and 64) indicates that most games are progressing at least to a mid-tier level.





---
## Graphical Analysis

### Max Moves Survival
![Max Moves Survival](https://drive.google.com/uc?id=14DPFVuguuyorvHZ3bcehDa1ZirgYrFft)

This graph illustrates how many games survived to various maximum move counts. It helps understand the distribution of game lengths across all 500 test cases. Games that last longer may suggest better move efficiency or just favorable randomness.


### Max, Min and Avg Score vs Number of Moves
![Max, Min and Avg Score vs Number of Moves](https://drive.google.com/uc?id=17U-iIu1oaORT5A8Y-Srm-Vhuso8_jln5)

Here we compare the highest, lowest, and average scores achieved at each move number. This chart shows how score progression stabilizes or accelerates over time, highlighting moments where most games either plateau or score big.


### Final Scores vs Number of Games
![Final Scores vs Number of Games](https://drive.google.com/uc?id=1CYsTFXpg7hJTo8Vo-MCOQDo9Q_Fp4giK)

This bar graph shows how many games ended with a particular final score. It gives a clear idea of which score ranges are most frequent and how score distribution varies across all test cases.


### Average Score Progression per Move
![Average Score Progression per Move](https://drive.google.com/uc?id=1RRR0RI_-zBoLbMXlTb56t4zHCcimw_um)

This line graph plots the average score increase per move across all games. It provides insights into how effective the algorithm is in accumulating score as the game progresses.


### Final Score vs Move
![Final Score vs Move](https://drive.google.com/uc?id=1i3iulEh8EpvurnoLfpjb43gu63AkZfFd)

This graph maps the final score of each game against its total number of moves. It helps us observe if playing longer consistently leads to better scores or if high scores are achieved early in some runs.


### Largest Tile vs Number of Games
![Largest Tile vs Number of Games](https://drive.google.com/uc?id=1o9bxMzb3sQghHwK1ZeyP0Z4JyTEEbCMq)

This visualization shows how many games managed to reach specific tile values. It’s a useful measure of how far the algorithm can push the board, indicating the effectiveness of reaching larger tiles.


---

## Observations & Analysis

### Gameplay Performance
The algorithm demonstrates the ability to sustain gameplay for an average of **334 moves**, which is respectable for a baseline or heuristic-based strategy. However, despite the extended gameplay, the scoring doesn't scale proportionately, which could indicate inefficiencies in tile-merging strategy.

### Scoring Trends
The **average final score of 1566** suggests that the algorithm is capable of achieving decent merges throughout the game. However, it's important to note that the **most common largest tile** reached was only **128**, which is relatively low. This highlights the potential ceiling in performance where the algorithm struggles to transition from mid-game to late-game effectively.

### Outliers & Extremes
Some games performed significantly better, with the **maximum score reaching 4448** and the **longest game surviving 1771 moves**. These outliers could represent instances where the algorithm found an optimal merge path or was simply lucky with tile spawns.

---

## Insights & Takeaways

- There’s a consistent performance trend, but the algorithm seems to hit a wall after a certain point, both in terms of score and tile progression.
- Many games plateau around tile 128, indicating room for improvement in maximizing merges and planning future moves.

---

## Future Work


  **Depth-Based Lookahead**: Simulate 2-3 moves ahead instead of acting greedily.


---


