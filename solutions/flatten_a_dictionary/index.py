# Flatten a Dictionary
# https://medium.com/@vickdayaram/flatten-a-dictionary-a5fa4426bf9d


class Solution:
    def flatten_dictionary(self, dictionary):
        res = {}
        for d in dictionary:
            if isinstance(dictionary[d], str):
                res[d] = dictionary[d]
                continue
            obj = self.flatten_dictionary(dictionary[d])
            for o in obj:
                if d == "" or o == "":
                    res[d + o] = obj[o]
                else:
                    res[d + "." + o] = obj[o]
        return res
