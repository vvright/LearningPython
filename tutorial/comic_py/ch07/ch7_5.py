# -*- coding:utf-8 -*-
#  代码文件：ch07/ch7_5.py

# 一篇文章文本
wordstring = """
    it was the best of times it was the worst of times.
    it was the age of wisdom it was the age of foolishness.
    """
# 将标点符号替换
wordstring = wordstring.replace('.', '')

# 分割单词
wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    # 统计单词出现个数
    wordfreq.append(wordlist.count(w))

print(wordlist)
print(wordfreq)

d = dict(zip(wordlist, wordfreq))
print(d)
