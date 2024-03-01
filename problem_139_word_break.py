from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    for word in wordDict:
        if word not in s:
            return False
        s = s.replace(word, '')
    return True


s = "leetcode"
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))
