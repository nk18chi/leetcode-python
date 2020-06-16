import unittest
import solutions.validate_ip_address.index as main


class Test(unittest.TestCase):
    def test_validIPAddress(self):
        test_patterns = [
            ("172.16.254.1", "IPv4"),
            ("256.256.256.256", "Neither"),
            ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.validIPAddress(arg), expected)


if __name__ == '__main__':
    unittest.main()
