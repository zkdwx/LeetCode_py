"""
@name：剑指 Offer II 066. 单词之和
@date:2022/8/28
@leetcode link:
@classify:
@remarks:
@analysis:
"""


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map_dict = dict()

    def insert(self, key: str, val: int) -> None:
        self.map_dict[key] = val

    def sum(self, prefix: str) -> int:
        pre_sum = 0
        for key, val in self.map_dict.items():
            if key.startswith(prefix):
                pre_sum += val
        return pre_sum

# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert('12',2)
param_2 = obj.sum('12')
