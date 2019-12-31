# numの回数文ポーカーのペア判定を繰り返す
import collections
num = input()
for x in range(int(num)):
	answer = "No Pair"
	line = list(str(input()))
	c = collections.Counter(line)
	if len(c) == 3:
		answer = "One Pair"
	elif len(c) == 2:
		if c.most_common()[0][1]!=3:
			answer = "Two Pair"
		else:
			answer = "Three Card"
	elif len(c) == 1:
		answer = "Four Card"
	print(answer)