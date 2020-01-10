# 596. Classes More Than 5 Students
# https://leetcode.com/problems/classes-more-than-5-students/

# from typing import List

"""
# 1
SELECT
    a.class as class
FROM
    ( SELECT student, class FROM courses GROUP BY student, class  ) as a
GROUP BY
    a.class
Having
    count(*) >= 5
"""

"""
# 2
SELECT
    class
FROM
    courses
GROUP BY
    class
HAVING
    COUNT(DISTINCT(student)) >= 5
"""
