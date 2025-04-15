
text = """My heart leaps up when I behold 
   A rainbow in the sky:
So was it when my life began; 
So is it now I am a man; 
So be it when I shall grow old, 
   Or let me die!
The Child is father of the Man;
And I could wish my days to be
Bound each to each by natural piety."""
print(text)
textlist = text.split()
# 간단 버전
wordcount = dict()
print(textlist)

for word in textlist:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1

for k, v in wordcount.items():
    print(f'{k}:{v}')

#두번째 버전 : defaultdict
from collections import defaultdict
wordcount = defaultdict(lambda:0)
for word in textlist:
    wordcount[word] += 1


print(wordcount)