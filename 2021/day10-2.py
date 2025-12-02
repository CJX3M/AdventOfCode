from openData import getData
data = getData("day10Test.txt")
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
err_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
msg_points = {")": 1, "]": 2, "}": 3, ">": 4}
err_scores = []
msg_scores = []

for chunk in data:
    score = 0
    found = []
    for c in chunk:
        if c not in [")", "]", "}", ">"]:
            found.append(c)
        else:
            if c == pairs[found[-1]]:
                found.pop()
            else:
                err_scores.append(err_points[c])
                found = []
                break
    if found:
        for m in [pairs[x] for x in found[::-1]]:
            score = (score * 5) + msg_points[m]
        msg_scores.append(score)