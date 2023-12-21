import re
x = re.findall(r"((\w)\2*)",input())
print(max(list(map(len,[m[0] for m in x]))))

