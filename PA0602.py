import statistics

marks = [70, 54, 68]
mean_mark = statistics.mean(marks)
median_mark = statistics.median(marks)

print(mean_mark)
print(median_mark)

from collections import Counter

marks1 = [45, 68, 32, 54, 70, 25]

results = []

for mark in marks1:
    if mark >=50:
        results.append("Pass")
    else:
        results.append("Fail")

counter = Counter(results)

print("Pass:", counter["Pass"])
print("Fail:", counter["Fail"])
