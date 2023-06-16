from typing import List
from math import inf

class Solution:
    def minTime(self, n: int, locations: List[int], types: List[int]) -> int:
        num_types = max(types) + 1
        mn_loc = [inf] * num_types
        mx_loc = [-inf] * num_types

        for typ, loc in zip(types, locations):
            mn_loc[typ] = min(mn_loc[typ], loc)
            mx_loc[typ] = max(mx_loc[typ], loc)

        prev_min_loc = prev_max_loc = 0
        dp = [(0, 0)]  # Initialize with (0, 0)

        for typ in sorted(set(types)):
            current_min_loc = mn_loc[typ]
            current_max_loc = mx_loc[typ]

            dp.append((
                min(dp[-1][0] + abs(current_max_loc - prev_min_loc), dp[-1][1] + abs(current_max_loc - prev_max_loc)) + current_max_loc - current_min_loc,
                min(dp[-1][0] + abs(current_min_loc - prev_min_loc), dp[-1][1] + abs(current_min_loc - prev_max_loc)) + current_max_loc - current_min_loc
            ))

            prev_min_loc = current_min_loc
            prev_max_loc = current_max_loc

        return min(dp[-1][0] + abs(current_min_loc), dp[-1][1] + abs(current_max_loc))
