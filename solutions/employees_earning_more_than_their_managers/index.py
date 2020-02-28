# 181. Employees Earning More Than Their Managers
# https://leetcode.com/problems/employees-earning-more-than-their-managers/

# from typing import List, Dict


# SELECT
#     name As Employee
# FROM
#     Employee
#     INNER JOIN
#     (
#         SELECT
#           id
#           , salary
#         FROM
#           Employee
#     ) M
#     ON Employee.ManagerId = M.id
# WHERE
#     Employee.salary > M.salary

# SELECT
#     E.name Employee
# FROM
#     Employee E
# INNER JOIN
#     Employee M ON E.ManagerId = M.id
# WHERE
#     E.salary > M.salary
