# 468. Validate IP Address
# https://leetcode.com/problems/validate-ip-address/

from typing import List, Set


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(s: str):
            print(s)
            if not s.isdigit():  # 11.11.1.a
                return False
            elif str(int(s)) != s:  # 11.11.1.01
                return False
            elif not 0 <= int(s) <= 255:  # 11.11.1.256
                return False
            return True

        def isIPv6(s: str):
            if len(s) > 4 or len(s) == 0:
                return False
            validLetters: Set[str] = set("0123456789abcdefABCDEF")
            for c in s:
                if c not in validLetters:
                    return False
            return True

        ipv4: List[str] = IP.split(".")
        if len(ipv4) == 4 and all(isIPv4(i) for i in ipv4):
            return "IPv4"
        ipv6: List[str] = IP.split(":")
        if len(ipv6) == 8 and all(isIPv6(i) for i in ipv6):
            return "IPv6"
        return "Neither"
