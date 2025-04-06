# 2048 Algorithm Performance Report

## Overview

This document presents a comprehensive performance breakdown of a custom 2048-playing algorithm based on **100 simulation runs**. The analysis focuses on key gameplay metrics such as average scores, move efficiency, tile progression, and success in reaching high-value tiles like **1024** and **2048**.


---

## Summary Statistics

| Metric                          | Value         |
|--------------------------------|---------------|
| **Total Games Analyzed**       | 100           |
| **Average Moves Per Game**     | 637.22        |
| **Average Final Score**        | 9382.88       |
| **Max Score Achieved**         | 24,796        |
| **Max Moves in a Single Game** | 1340          |
| **Most Common Largest Tile**   | 1024          |

The results show a strong average performance, with games generally ending with respectable scores and tile values. The **1024 tile was reached in nearly half of all games**, signaling consistent mid-to-late game strength. However, breaking into the 2048+ tier still requires refinement.

---

## Largest Tile Distribution

| Tile  | Games | Percentage |
|-------|-------|------------|
| 256   | 10    | 10.0%      |
| 512   | 40    | 40.0%      |
| 1024  | 48    | 48.0%      |
| 2048  | 2     | 2.0%       |

This breakdown reveals how deep the algorithm pushes toward the endgame. **88% of games reach at least 512**, while **just 2% manage to break through to 2048**. It's a promising sign, but there's clearly room for improvement in late-game tile control and board efficiency.

---

### Largest Tile vs Number of Games
See the frequency of top tiles achieved across all games. This is a great way to visualize the algorithm’s endgame reliability.  
![Largest Tile](https://drive.google.com/uc?id=1DtfwFw7Q-r6oNPiDKQFjKqrqkEbKtORb)

---

### Max Moves Survival Distribution  
Analyzes how long the algorithm survives — long games often correlate with strategic depth and smarter decision-making.  
![Max Moves](https://drive.google.com/uc?id=1PpdLX3JLnirx7Dlh2aR4tvCF9em4oV8v)

---

### Average Score Progression Per Move  
Shows how efficiently the score builds over time — flatter curves indicate stagnation, while steep gains reflect power plays and merges.  
![Average Score Progression](https://drive.google.com/uc?id=1YG17pxvopIRgMnyPuUe7tMaf7xYKmuUG)

---

### Final Score vs Move Count  
Do longer games always mean better scores? Not necessarily — this graph helps reveal the sweet spot between move count and scoring potential.  
![Score vs Move](https://drive.google.com/uc?id=1dZ-u0AeaOp1DTKCKbWY3nv5ZHakxgRcE)

---

### Min, Max, and Average Score vs Move Number  
Offers a more granular look at score consistency across moves. A tight band between min and max suggests stability, while wild swings hint at riskier plays.  
![Min Max Avg Score](https://drive.google.com/uc?id=1dxY_0lF4qskuHNGdlUqDnUUS6sOwD9Au)

---

### Final Score Distribution  
Summarizes how scores are spread across the entire set of games. This is helpful to gauge what a typical game looks like and how frequently high scores occur.  
![Final Scores](https://drive.google.com/uc?id=1gvixQdinGN_KYkFuwKAsmnvRSQAKJLnK)

---

## Final Thoughts

The current algorithm strikes a good balance between **move survival and score accumulation**. Reaching 1024 in 48% of games and 2048 in a few indicates that the foundation is solid. However, **the drop-off beyond 1024 shows a gap in late-game strategy** — possibly due to inefficient merges under pressure.
