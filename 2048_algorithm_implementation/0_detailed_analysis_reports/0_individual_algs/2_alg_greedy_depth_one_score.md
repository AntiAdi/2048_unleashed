# 2048 Algorithm Implementation  
## Algorithm : One Depth Greedy for the Max Score

---

### Summary of Results

- **Total Games Analyzed:** 500  
- **Average Moves Per Game:** 165.09  
- **Average Final Score:** 1721.16  
- **Most Common Largest Tile Reached:** 128  
- **Max Score Achieved:** 5260  
- **Max Moves in a Single Game:** 376  

---

### Working of Algorithm
The *algorithm* simply checks the score increase for the **next 4 possible moves and chooses to perform the one with the highest score change**. If score changes are similar, It chooses randomly amongst the best moves.

One thing that **lacks** is the ability to **choose the move with more tiles merges if the score change is same**.


___

### Graphical Analysis

#### 1. Score vs Move (500 Test Cases)
Shows the trend of score accumulation as the game progresses, across all 500 test runs.

![Score vs Move](https://drive.google.com/uc?id=1i2oci1R74nbg8h71ZvPgvqAMywdwdI-f)

---

#### 2. Min, Max, and Average Score vs Number of Moves
Displays the highest, lowest, and average score values for each move number, indicating performance consistency.

![Score Min Max Avg vs Moves](https://drive.google.com/uc?id=1UDovhHe12UKx1BGzAstdWwX82x_FTGP-)

---

#### 3. Final Scores vs Number of Games
A histogram of final scores reached by each of the 500 games. Useful to assess score distribution.

![Final Score Distribution](https://drive.google.com/uc?id=1bzTgda4StCieSKb9KMPtAK-D8oPcQfBV)

---

#### 4. Max Moves in a Game vs Number of Games
How long each game lasted in terms of number of moves. Reflects game longevity.

![Moves Survived](https://drive.google.com/uc?id=1k78g57UOsVAl_BE46SaejJAxj6V7VEK8)

---

#### 5. Largest Tile Reached vs Number of Games
Bar graph of the frequency of the highest tile reached.

![Max Tile Reached](https://drive.google.com/uc?id=1UiWfCfCJUUy5pVgd4oF2mNruoH-gH2b3)

---

#### 6. Average Score vs Move Number
How the average score increased over the course of the game. Gives insight into scoring patterns.

![Average Score vs Moves](https://drive.google.com/uc?id=13lr_9bM9xo8Eo4OPNuSEBeNvUyin3pge)

---

### Observations

- The algorithm steadily builds up score, though a very few exceptional outliers reach high scores **(over 5000)**.
- Most games reach **128 or 256** as the largest tile.
- There's a gradual increase in scoring over moves, showing **somewhat efficient** tile merging.
- The distribution of scores shows a **wide range of performance** across different seeds.

---

### Conclusion

This analysis demonstrates the performance of the **algorithm based on 500 runs**. While the average game performs decently, **some extreme runs highlight potential**.</br>
Improvements will include better **tile placement strategies** and **increased lookahead depth**.

---

