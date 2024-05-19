# 1184. Distance Between Bus Stops
# https://leetcode.com/problems/distance-between-bus-stops/

from typing import List


class Solution:
    # def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    #     clockwise: int = 0
    #     counterclockwise: int = 0
    #     right: int = start
    #     left: int = start

    #     while right != destination or left != destination:
    #         if right != destination:
    #             clockwise += distance[right]
    #             right += 1
    #             if right == len(distance):
    #                 right = 0
    #         if left != destination:
    #             left -= 1
    #             if left < 0:
    #                 left = len(distance) - 1
    #             counterclockwise += distance[left]

    #     return min(clockwise, counterclockwise)

    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        if start > destination:
            start, destination = destination, start
        short: int = sum(distance[start:destination])
        long: int = sum(distance) - short
        return min(short, long)
