"""
@name：剑指 Offer II 065. 最短的单词编码
@date:2022/6/22
@leetcode link:https://leetcode.cn/problems/iSwD2y/
@classify:
@remarks:
@analysis:
输入：words = ["time", "me", "bell"]
输出：10
解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。
words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"

"""
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        i = 0
        res_list = []
        res_list.append(words[0])
        while i < len(words) - 1:
            b = words[i].endswith(words[i + 1])
            if b:
                pass
            i += 1
        res_list.append(words[-1])
        return len('#'.join(res_list)) + 1


ss = Solution()
# words = ["time", "me", "bell"]
words = ["t"]
encoding = ss.minimumLengthEncoding(words)
print(encoding)
