import unittest
import solutions.unique_email_addresses.index as main


class Test(unittest.TestCase):
    def test_numUniqueEmails(self):
        test_patterns = [
            (["test.email+alex@leetcode.com", "test.email@leetcode.com"], 1),
            (["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"], 2),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.numUniqueEmails(arg), expected)


if __name__ == '__main__':
    unittest.main()
