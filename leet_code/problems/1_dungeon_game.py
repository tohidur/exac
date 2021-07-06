"""
The daemons had captured the princess(P) and imprisoned here in the botton
right corner of a dungeon consists of M x N rooms laid out in a 2D grid.
Our valiang knight (K) was initally positioned in the top-left room and must
fight his way through then dungeon to rescue the princess.

The knight has a initial health point represented by a positive integer. If at
any point his health point drops to 0 or less he dies immediately.

Some of the rooms are guarded by daemons, so the knight looses health upon
entering these rooms; other rooms are either empty or contains magic orbs
that increases the knight's health.

In order to reach the princes as quickly as possible, the knight decided to
move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that
he is able to rescue the princess.

Ex:

-2(k)   -3      3

-5      -10     1

10      30      -5(P)

Minimum health - 7
Steps - R -> R -> D -> D
"""

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        pass

