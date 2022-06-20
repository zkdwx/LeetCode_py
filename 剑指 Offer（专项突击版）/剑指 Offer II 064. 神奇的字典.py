"""
@date:2022/6/20
@leetcode link: https:#leetcode.cn/problems/US1pGT/
@classify: 字典 前缀树
@remarks:
@analysis: 字典法：以单词的长度为key值，减少循环次数；两个单词只有一个不同，统计方法可判断
"""
from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mag_dict = dict()

    def buildDict(self, dictionary: List[str]) -> None:
        for s in dictionary:
            if len(s) in self.mag_dict:
                self.mag_dict[len(s)].append(s)
            else:
                self.mag_dict[len(s)] = [s]

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.mag_dict:
            return False
        else:
            tar_list = self.mag_dict.get(len(searchWord))
            for s in tar_list:
                r = self.check_diff(s, searchWord)
                if r:
                    return True
            return False

    def check_diff(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        if count > 1 or count == 0:
            return False
        else:
            return True


magicDictionary = MagicDictionary()
magicDictionary.buildDict(["hello", "leetcode"])
print(magicDictionary.search("hello"))  # 返回 False
print(magicDictionary.search("hhllo"))  # 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
print(magicDictionary.search("hell"))  # 返回 False
print(magicDictionary.search("leetcoded"))  # 返回 False
