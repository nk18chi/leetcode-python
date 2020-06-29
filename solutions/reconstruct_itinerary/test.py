import unittest
import solutions.reconstruct_itinerary.index as main


class Test(unittest.TestCase):
    def test_findItinerary(self):
        test_patterns = [
            ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]], ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
            ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "JFK"]], ["JFK", "SFO", "JFK", "ATL"]),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.findItinerary(arg), expected)


if __name__ == '__main__':
    unittest.main()
