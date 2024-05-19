import unittest
import _contest.weekly_167.index as main


class Test(unittest.TestCase):
    def test_maxSideLength(self):
        test_patterns = [
            (
                [
                    [1, 1, 3, 2, 4, 3, 2],
                    [1, 1, 3, 2, 4, 3, 10],
                    [1, 1, 3, 2, 4, 3, 100],
                ],
                4,
                2,
            ),
            ([[2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6]], 1, 0),
            # ([[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 6, 3),
            # ([[18, 70], [61, 1], [25, 85], [14, 40], [
            #  11, 96], [97, 96], [63, 45]], 40184, 2)
            # ([[21,91,65,94,46,95,70,26,88,29,73,24,62,32,35,49,79,67,23,45,6,7,60,98,31,69,86,64,28,78,47,57,20,17],[67,74,78,10,19,22,17,58,44,31,100,37,30,16,6,56,81,60,97,41,63,87,40,79,26,77,86,80,15,39,23,28,34,83],[24,73,55,82,0,62,89,54,49,28,77,43,81,12,84,91,72,25,5,29,68,23,93,42,34,13,69,94,35,19,37,36,78,74],[81,27,83,11,31,0,85,71,35,4,8,92,62,99,61,47,63,17,93,7,43,52,60,33,79,41,40,76,13,80,57,39,51,54],[21,81,28,100,47,83,5,62,60,97,86,90,85,46,0,42,72,58,74,77,38,69,41,35,95,54,8,99,1,87,33,51,66,27],[64,69,54,34,22,21,83,82,85,2,5,81,67,56,16,4,77,84,40,72,70,95,51,89,96,61,63,7,1,28,99,62,75,47],[2,15,95,54,89,10,96,27,6,85,1,25,81,33,37,18,39,63,49,72,77,69,48,31,24,22,87,66,8,53,17,74,86,68],[68,88,5,53,94,65,38,95,48,37,42,55,29,93,80,47,36,77,64,46,43,2,99,89,72,61,9,16,74,20,76,73,82,11],[28,57,76,12,86,31,37,62,70,96,27,17,13,77,59,41,85,55,94,97,3,34,56,67,74,47,33,38,6,64,51,63,83,80],[66,41,13,1,70,81,15,0,82,92,22,12,44,74,16,34,26,20,36,35,77,53,52,79,56,29,59,10,3,89,48,80,55,24],[92,15,98,32,23,62,68,93,1,17,53,28,21,54,60,49,51,43,52,77,3,34,46,10,84,35,75,89,26,24,80,45,31,22],[83,95,2,51,17,7,28,89,5,80,52,43,67,91,57,86,40,53,90,11,65,38,68,47,33,82,63,85,61,37,15,22,87,19],[2,99,69,61,0,20,50,77,48,11,22,17,28,66,1,70,98,74,88,82,63,34,75,76,78,24,23,8,10,35,26,85,19,57],[94,18,44,87,91,81,3,15,31,40,4,14,63,47,89,49,12,16,9,23,50,66,0,28,43,10,39,20,78,56,73,99,95,5],[94,26,89,14,69,27,8,85,87,12,24,35,44,81,15,56,38,63,75,60,99,47,32,76,10,19,62,93,20,98,70,21,3,30],[53,35,93,3,32,84,85,68,64,77,86,59,2,65,47,12,76,5,42,61,7,37,50,0,38,79,18,52,34,82,29,55,41,21],[96,25,50,55,69,19,15,9,30,88,16,32,38,41,80,6,97,79,28,27,65,47,89,0,73,84,3,51,11,33,1,72,23,92],[30,65,75,51,17,25,60,100,36,66,83,16,5,26,96,37,99,93,10,52,88,19,2,87,55,47,7,28,91,21,35,85,62,31],[63,96,6,57,68,71,60,81,64,4,70,72,1,74,34,80,17,67,28,54,79,32,23,12,73,39,89,93,55,100,40,24,58,45],[93,41,50,10,73,87,21,83,77,4,85,1,3,24,29,30,55,2,48,31,11,38,34,44,96,62,49,68,15,46,12,56,59,81],[48,47,87,10,30,78,23,44,11,58,39,7,9,53,20,46,73,77,40,69,2,62,21,88,75,43,90,14,36,13,85,91,54,28],[64,92,98,7,94,70,81,80,89,38,73,85,39,95,57,65,69,60,32,97,75,77,30,90,3,37,2,53,43,72,36,61,100,58],[46,47,90,10,12,50,83,98,75,25,55,11,51,0,60,86,63,28,79,91,72,78,88,14,67,92,9,19,54,85,57,99,7,38],[13,14,28,69,34,1,97,23,53,91,9,75,58,61,21,24,50,95,79,93,52,26,72,86,89,40,96,65,90,45,15,87,18,63],[89,100,79,64,55,40,32,65,57,93,23,49,29,54,56,2,14,34,44,73,52,47,25,33,20,51,76,81,18,21,98,96,7,97],[54,64,75,50,35,32,10,68,51,4,65,79,28,95,98,57,41,26,7,18,19,6,93,63,0,40,91,27,1,49,30,37,12,73],[83,73,24,70,8,72,6,21,80,93,43,13,82,33,99,37,26,40,69,64,11,2,81,53,46,38,55,76,62,74,92,49,30,4],[63,59,70,95,98,86,72,67,71,37,56,2,29,50,93,39,44,92,15,34,22,40,7,84,43,35,96,54,53,90,45,81,73,38],[32,79,50,29,83,16,54,90,66,19,51,96,92,87,9,93,94,76,23,56,12,95,98,31,15,97,30,71,42,81,7,43,52,88],[65,53,23,63,82,81,9,67,75,44,39,69,16,55,99,93,17,71,36,96,84,85,28,19,35,79,70,1,25,26,72,80,22,10],[3,75,58,74,18,46,16,88,21,10,1,29,76,93,73,98,40,32,52,62,22,26,14,66,38,57,55,34,82,72,60,83,90,19],[74,48,36,32,90,80,98,17,46,75,10,30,2,19,9,44,33,5,14,61,79,89,96,23,71,81,100,7,56,72,11,18,63,84],[93,81,35,27,18,95,13,44,23,49,54,86,87,96,19,8,57,24,62,66,74,3,32,78,46,17,22,53,30,56,25,6,61,9],[6,41,29,24,2,19,77,71,57,63,81,36,73,12,49,22,4,95,61,47,21,80,53,14,9,42,51,40,91,100,65,48,97,27],[75,4,70,8,58,25,50,2,30,93,22,24,29,31,87,57,39,71,73,69,94,81,48,100,9,14,60,27,54,36,77,47,92,68],[15,48,8,83,28,41,61,52,3,23,0,67,55,87,60,73,46,35,47,25,71,95,69,31,54,1,76,10,94,13,58,14,51,93],[27,54,43,13,68,76,82,88,19,47,8,100,36,58,72,39,84,63,16,31,33,57,60,30,99,69,98,10,24,38,44,86,29,67],[19,75,51,31,16,32,90,27,0,15,69,80,21,59,76,46,60,30,79,2,33,81,44,37,77,89,45,1,61,28,41,50,3,47],[72,19,99,80,33,86,2,96,100,22,85,74,55,18,42,70,21,73,76,95,90,26,51,75,38,41,3,69,49,31,7,61,68,53],[46,55,94,14,25,16,22,87,73,97,43,62,57,51,37,28,86,95,3,1,31,59,40,7,4,24,34,10,56,61,96,72,69,99],[26,3,36,72,62,83,52,60,99,27,57,11,86,64,10,70,43,73,29,48,67,68,87,20,92,14,25,47,8,17,22,21,49,78],[12,3,10,76,97,87,57,30,42,20,9,73,27,23,51,35,92,19,46,68,70,24,61,85,11,77,72,59,5,95,80,67,50,52],[25,28,17,10,76,56,99,96,54,83,15,12,71,48,84,49,58,14,43,21,88,75,68,98,29,85,73,22,89,50,55,72,30,5],[72,83,17,79,21,0,68,73,91,8,78,75,52,13,11,60,53,87,26,80,85,38,16,89,22,84,34,41,47,39,37,98,54,19],[42,39,16,8,44,36,96,63,79,83,5,33,98,7,64,35,49,10,41,40,18,73,65,70,23,47,55,50,28,4,26,3,100,13],[73,27,87,76,64,13,39,32,71,23,42,60,59,94,99,47,44,81,5,82,97,89,80,86,41,10,91,4,54,67,63,98,22,7],[39,47,96,35,29,72,18,19,95,76,85,71,63,88,36,16,10,55,45,62,61,69,99,65,50,81,41,7,14,59,33,97,23,98],[56,38,52,81,50,42,57,26,82,72,58,10,77,25,73,13,69,6,7,30,74,70,0,34,41,29,84,17,1,55,66,9,60,44],[31,96,45,52,79,33,95,55,32,98,89,26,69,24,87,58,29,6,30,40,23,70,62,15,9,17,0,21,91,48,88,12,3,11],[62,48,8,64,44,81,84,6,47,96,91,60,24,57,65,80,11,68,54,46,71,19,82,74,26,99,53,100,94,98,38,56,10,85],[77,97,12,72,92,73,6,85,9,95,11,83,54,51,61,66,20,16,39,90,93,5,8,47,75,32,22,35,33,60,56,18,38,0],[75,25,21,9,53,55,26,59,62,84,88,46,3,34,41,65,64,10,6,61,93,40,4,91,27,24,45,35,2,0,72,97,12,31],[98,24,92,16,29,17,42,75,76,7,88,66,80,3,84,72,5,68,67,45,18,41,32,46,78,23,40,60,21,63,9,53,77,10]], 51510, 32),
            # ([[11,4,64,99,8,66,58,71,88,27,6,48,82,10,94,69,43,35,81,41,50,92,7,1,100,17,76,61,23,67,45,75,91,53,15,90,30,12,62,22,28,14,52,13],[98,27,85,3,76,50,68,1,60,44,32,43,59,99,90,5,79,84,53,20,81,23,94,54,62,40,26,31,61,13,72,15,36,64,97,69,91,95,67,47,16,8,11,6],[27,6,24,71,66,73,21,45,68,32,49,98,37,83,67,46,30,40,90,2,19,86,74,44,64,80,93,85,26,100,17,33,36,8,1,42,88,69,75,15,63,4,43,61],[89,41,94,54,10,11,84,71,77,61,24,36,78,83,98,17,100,45,27,87,35,1,32,55,23,39,80,8,93,3,73,70,42,4,6,52,74,57,82,38,81,67,30,79],[49,28,74,37,32,89,38,64,43,88,18,53,50,12,97,22,23,94,78,1,68,30,98,10,92,57,86,84,33,24,15,48,85,95,39,27,14,60,0,19,81,62,47,21],[60,41,78,52,10,83,14,1,42,50,57,23,97,56,38,65,13,96,98,49,75,70,4,37,82,39,100,34,35,40,85,6,53,90,22,26,28,18,3,43,68,63,72,54],[75,68,57,67,91,37,45,55,3,85,13,30,41,34,20,77,23,93,35,27,99,29,62,32,21,84,96,38,81,9,66,60,87,47,69,95,59,65,2,98,12,61,18,39],[76,9,77,4,100,18,3,17,32,89,86,72,26,56,54,14,49,93,97,15,84,13,87,19,42,36,66,73,21,29,99,70,24,96,85,60,78,33,55,65,31,11,2,44],[32,57,49,73,15,39,4,88,6,28,43,30,19,59,71,97,37,70,40,56,35,80,77,64,68,26,34,98,83,67,27,94,5,25,17,8,72,24,75,54,29,45,14,50],[55,9,50,38,95,22,84,76,28,58,77,41,81,92,1,39,59,99,2,17,23,10,52,20,68,54,61,82,32,91,83,35,100,4,5,7,75,43,0,8,74,79,21,34],[4,42,18,58,31,26,79,24,17,43,81,27,73,56,29,69,47,53,90,7,72,95,93,94,65,40,87,8,76,38,3,57,25,32,84,14,23,21,0,86,67,5,45,66],[41,38,21,27,34,46,50,86,83,100,85,12,74,68,47,11,57,67,59,45,30,13,61,92,35,91,60,43,64,90,88,0,14,23,53,56,39,32,51,77,69,31,29,55],[46,1,11,81,26,96,93,66,59,74,5,14,28,12,69,25,33,55,20,98,37,48,70,47,23,67,9,51,88,27,2,43,36,65,75,78,64,76,89,87,40,100,39,68],[10,30,67,49,76,26,87,99,74,100,75,60,21,45,39,13,4,72,47,97,77,89,28,9,37,44,88,54,11,50,33,79,95,42,8,6,18,48,40,12,81,2,68,53],[22,7,90,97,63,33,8,91,93,56,6,34,88,66,15,62,49,98,52,94,55,65,67,44,9,86,71,10,13,14,78,43,82,50,27,19,96,46,75,40,1,39,35,95],[72,23,99,31,9,12,10,87,43,55,75,11,71,83,73,33,85,45,44,30,37,79,62,46,67,36,8,90,77,13,28,82,48,54,14,53,1,47,61,6,91,69,60,16],[55,48,67,21,86,20,28,65,68,45,34,51,6,80,30,62,4,18,52,99,11,100,74,58,7,81,16,95,63,69,89,88,31,92,84,46,97,71,53,64,59,90,41,50],[58,21,19,46,61,79,8,70,98,26,49,68,22,4,23,88,63,28,10,12,52,72,31,35,93,65,18,47,9,90,45,80,55,83,86,41,94,51,60,14,64,62,75,38],[17,76,26,44,19,66,100,60,47,33,5,34,8,21,64,1,91,81,11,0,23,65,72,89,80,78,16,31,13,71,75,63,49,40,79,93,52,58,28,24,99,29,61,97],[75,18,49,65,42,43,62,66,15,77,74,90,95,7,2,39,89,22,6,16,37,78,25,33,27,99,98,72,61,19,26,20,54,70,91,1,41,4,9,14,60,100,56,76],[57,86,64,26,93,80,48,63,68,84,51,18,76,52,74,25,22,82,14,75,8,17,15,41,35,81,49,7,60,28,5,45,55,29,24,91,96,9,40,6,11,1,87,78],[71,53,60,77,90,65,40,55,29,7,99,92,75,64,74,87,6,72,21,3,33,49,5,70,8,0,95,80,17,27,16,81,52,14,13,61,68,78,10,2,85,48,32,51],[62,32,46,3,83,96,100,68,72,31,54,28,17,73,56,34,6,44,11,51,48,42,4,9,66,64,35,67,18,78,37,14,74,94,40,89,70,61,93,39,7,86,88,25],[90,9,43,64,39,85,51,35,32,95,1,10,2,34,96,42,4,93,12,21,70,58,23,25,15,30,56,100,71,82,5,72,78,14,40,79,69,18,11,98,73,27,48,19],[22,35,63,19,98,68,43,55,50,56,60,69,45,47,82,92,1,67,21,40,49,27,84,93,5,28,89,62,75,87,71,48,44,33,3,57,52,51,0,81,17,83,10,42],[12,57,74,60,36,4,47,38,22,0,97,11,65,25,24,17,83,70,20,86,23,66,44,99,88,51,10,41,59,71,58,84,7,34,89,48,54,15,93,55,46,2,37,40],[41,28,96,98,74,11,30,68,13,48,70,64,14,24,73,31,18,59,76,34,38,90,37,32,94,3,5,43,36,29,81,66,88,19,72,77,95,67,15,79,40,33,56,100],[28,70,10,55,27,89,7,15,63,88,87,8,40,22,20,62,45,49,43,74,26,38,97,32,0,37,46,65,91,41,13,90,81,42,17,18,52,19,3,30,39,14,44,67],[62,46,39,91,99,6,85,27,41,69,13,72,78,33,95,100,82,34,35,19,60,75,49,93,83,92,1,90,64,22,98,54,29,21,28,77,36,86,73,50,0,61,15,56],[78,40,21,83,11,37,90,73,47,26,5,84,74,92,64,55,22,31,42,10,34,25,58,77,23,9,45,81,18,89,6,24,95,100,17,33,27,39,19,36,13,2,12,32],[14,92,84,17,10,47,28,52,13,16,94,44,87,25,36,80,76,60,98,56,1,24,35,23,73,29,31,43,97,79,85,86,81,100,4,48,95,72,15,78,50,58,57,0],[0,71,18,62,29,85,96,93,17,11,3,39,75,23,65,52,50,59,42,24,79,20,77,35,21,100,82,6,48,95,61,72,68,27,81,12,37,88,83,97,73,7,67,19],[74,26,69,48,29,22,6,82,54,78,81,65,75,71,61,24,21,53,7,31,92,35,15,96,9,58,89,86,88,76,4,37,20,13,55,23,33,80,67,12,64,10,52,36],[81,94,100,51,5,25,2,22,30,68,8,0,50,96,71,90,57,13,36,84,41,64,89,17,53,32,82,40,1,47,99,58,29,37,28,52,19,23,73,92,11,61,44,35],[74,67,15,99,9,71,58,1,76,14,57,78,54,21,18,93,86,44,55,7,70,77,49,89,28,62,48,36,95,4,83,40,56,65,41,47,39,31,73,5,27,51,12,32],[31,17,65,7,28,67,55,2,18,12,76,23,42,27,94,73,40,92,68,58,71,70,95,3,59,29,51,45,90,50,43,44,4,91,22,88,77,97,34,72,37,16,66,81],[61,49,24,22,96,27,97,70,2,82,53,38,34,57,71,80,90,92,95,16,59,35,81,32,52,64,29,50,45,78,37,26,15,67,25,73,66,7,86,91,68,1,83,75],[88,75,59,57,62,36,33,26,79,50,29,56,28,4,16,31,27,90,76,72,3,2,45,94,89,21,100,19,20,14,71,34,22,44,49,67,78,32,80,81,9,84,1,10],[56,14,45,25,60,88,76,82,15,23,39,42,71,78,57,59,73,44,6,0,86,16,32,35,98,63,38,55,17,81,68,9,20,22,99,64,10,87,36,3,89,70,96,58],[14,50,96,38,68,1,22,53,43,59,19,95,88,70,15,49,75,21,32,41,29,8,42,64,3,82,23,99,61,34,0,60,98,76,52,48,87,85,37,4,58,56,20,35],[51,77,9,36,62,61,53,27,0,5,38,34,19,33,85,40,14,7,86,56,15,45,80,69,16,46,95,89,6,48,55,71,28,73,79,20,67,47,49,68,17,31,78,65],[84,69,60,22,49,34,41,0,10,28,21,64,55,31,51,54,17,57,33,14,26,8,15,5,61,80,94,45,95,11,40,35,62,53,86,67,39,3,16,81,24,19,32,30],[46,27,29,45,52,82,6,49,75,55,87,4,54,36,0,14,9,100,50,26,2,81,12,57,85,84,62,92,35,47,44,10,16,67,32,58,3,73,34,76,68,72,88,25],[1,21,47,94,45,31,69,54,63,33,27,59,22,11,92,82,9,93,19,100,16,51,3,50,35,75,30,89,70,76,44,25,32,78,95,28,29,87,36,83,88,79,60,13],[72,6,32,60,27,4,34,94,76,30,79,58,44,98,11,97,7,81,35,40,16,59,92,66,54,38,90,39,45,17,20,37,47,42,96,80,26,36,31,55,3,1,29,23],[40,37,7,18,62,99,54,13,45,23,81,94,92,70,86,79,47,19,4,16,24,41,12,65,39,21,22,6,95,32,0,20,38,26,43,100,36,98,84,82,55,75,77,85],[13,39,16,45,64,1,68,78,80,95,73,30,49,29,8,92,53,67,56,82,47,7,81,77,44,6,5,58,14,69,0,35,94,65,34,61,17,27,2,90,83,46,4,91],[60,65,78,67,36,90,100,91,42,5,70,43,44,56,97,37,14,22,16,23,17,15,34,38,11,81,73,50,0,10,19,30,76,59,98,55,99,68,32,41,46,51,75,7],[18,49,28,84,83,89,79,25,72,95,44,100,14,1,5,60,11,70,94,80,42,48,51,0,27,76,55,52,32,7,38,71,53,12,40,37,20,30,34,31,68,9,2,92],[48,75,33,5,62,16,76,70,21,23,78,15,67,26,31,68,91,77,82,92,45,19,27,79,32,43,64,55,89,59,44,72,66,17,56,3,36,65,13,12,22,25,85,20],[8,38,9,75,33,99,17,46,18,78,35,28,5,82,6,84,97,51,22,69,57,81,58,91,7,12,24,79,39,71,32,70,20,40,26,85,16,52,50,25,23,15,3,4],[24,29,41,38,90,95,21,46,28,1,74,17,81,78,8,52,85,96,98,9,11,23,83,56,22,13,27,55,59,5,30,45,72,68,40,70,62,14,100,66,20,34,2,64],[11,10,12,81,52,59,53,34,43,63,95,18,37,19,85,1,27,72,32,0,74,78,68,45,42,79,14,22,93,50,35,84,88,6,75,61,70,98,49,8,67,91,56,15],[63,77,6,51,19,59,5,97,44,88,42,80,8,50,99,29,85,52,26,14,60,66,3,70,12,61,46,74,79,90,93,10,30,83,36,43,94,53,68,87,89,9,28,33],[41,40,82,46,55,5,56,35,7,29,6,68,10,85,23,3,69,67,44,38,95,26,88,39,18,51,19,32,1,31,4,77,58,16,87,42,62,97,89,66,53,21,65,80],[31,28,0,95,46,8,90,15,97,52,54,23,40,93,6,37,98,14,51,79,16,59,11,24,62,33,29,48,56,85,32,39,78,44,1,12,38,36,9,25,45,4,13,88],[16,39,9,75,90,35,50,27,53,34,42,43,94,52,56,12,88,14,91,97,11,37,17,23,80,77,4,54,59,31,66,18,63,81,21,58,79,3,5,40,74,47,28,82],[33,43,11,86,34,23,64,100,76,87,73,58,82,32,62,35,21,93,47,18,71,7,77,30,90,12,84,81,63,5,98,4,91,56,2,31,50,67,94,22,26,3,37,66],[52,78,61,64,89,24,23,63,36,98,27,81,25,29,88,53,20,96,38,42,5,6,12,100,2,48,11,0,70,40,94,30,82,9,22,68,85,3,90,8,47,14,67,80]], 46849, 31)
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.maxSideLength(arg1, arg2), expected)

    def test_sequentialDigits(self):
        test_patterns = [
            (58, 155, [67, 78, 89, 123]),
            (10, 100, [12, 23, 34, 45, 56, 67, 78, 89]),
            (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
            (
                10,
                1000000000,
                [
                    12,
                    23,
                    34,
                    45,
                    56,
                    67,
                    78,
                    89,
                    123,
                    234,
                    345,
                    456,
                    567,
                    678,
                    789,
                    1234,
                    2345,
                    3456,
                    4567,
                    5678,
                    6789,
                    12345,
                    23456,
                    34567,
                    45678,
                    56789,
                    123456,
                    234567,
                    345678,
                    456789,
                    1234567,
                    2345678,
                    3456789,
                    12345678,
                    23456789,
                    123456789,
                ],
            ),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.sequentialDigits(arg1, arg2), expected)


if __name__ == "__main__":
    unittest.main()
