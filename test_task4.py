"""Small hand-checked cases for split_box (Task 4)"""

import numpy as np
from task4_split import split_box

# four colors that differ only in red, in mixed order
colors = np.array([[3, 0, 0],
                   [1, 0, 0],
                   [4, 0, 0],
                   [2, 0, 0]])

# equal counts -> cut in the middle, sorted by red
(low, _), (high, _) = split_box(colors, np.array([1, 1, 1, 1]), axis=0)
print("equal counts:", low[:, 0], "|", high[:, 0])
assert low[:, 0].tolist() == [1, 2]

# red=4 has most of the pixels -> it ends up alone on the upper side
(low, _), (high, _) = split_box(colors, np.array([1, 1, 10, 1]), axis=0)
print("heavy color :", low[:, 0], "|", high[:, 0])
assert high[:, 0].tolist() == [4]

# one color has almost all pixels -> neither side may be empty
(low, _), (high, _) = split_box(colors[:2], np.array([100, 1]), axis=0)
assert len(low) == 1 and len(high) == 1

print("all tests passed")
