# 196. Delete Duplicate Emails
# https://leetcode.com/problems/delete-duplicate-emails/

"""
DELETE FROM Person WHERE id NOT IN (
    SELECT
        *
    FROM
        (SELECT
            MIN(id) id
        FROM
            Person p
        GROUP BY
            Email) t
)
"""
