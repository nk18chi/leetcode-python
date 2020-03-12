# 929. Unique Email Addresses
# def numUniqueEmails(self, emails: List[str]) -> int:

from typing import List, Dict, Set


class Solution:
    # def numUniqueEmails(self, emails: List[str]) -> int:
    #     res: Set[str] = set()
    #     for e in emails:
    #         split: List[str] = e.split("@")
    #         email: str = ""
    #         for c in split[0]:
    #             if c == ".":
    #                 continue
    #             if c == "+":
    #                 break
    #             email += c
    #         res.add(email + "@" + split[1])

    #     return len(res)

    def numUniqueEmails(self, emails: List[str]) -> int:
        res: Set[str] = set()
        for e in emails:
            split: List[str] = e.split("@")
            local: str = split[0]
            domain: str = split[1]
            uniqueName: str = local.split("+")[0].replace(".", "")
            res.add(uniqueName + "@" + domain)

        return len(res)

    # def numUniqueEmails(self, emails: List[str]) -> int:
    #     res: Set[str] = set()
    #     for local, domain in [e.split("@") for e in emails]:
    #         uniqueName: str = local.split("+")[0].replace(".", "")
    #         res.add(uniqueName + "@" + domain)

    #     return len(res)
