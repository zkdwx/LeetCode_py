
from typing import List


class Solution:
    # 利用py的startwith遍历字典即可，因为其潜在
    def replaceWords(self, dictionary  : List[str], sentence: str) -> str:
        dictionary_list = sorted(dictionary, key=lambda x: len(x))
        words = sentence.split(" ")
        res_list = []
        for s in words:
            for dic in dictionary_list:
                if s.startswith(dic):
                    res_list.append(dic)
                    break
            else:
                res_list.append(s)
        return " ".join(res_list)


dictionary = ["catt", "cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
solution = Solution()
words = solution.replaceWords(dictionary, sentence)
print(words)
