INF = 9999999
with open('input.txt', 'r') as f:
    input_list = [[int(num) for num in line.split(' ')] for line in f if line.strip() != ""]

input_length = len(input_list)
selected = []
compare = []
for p in range(input_length):
    selected.append(0)
    compare.append([])
no_edge = 0
selected[0] = True
while no_edge < input_length - 1:
    minimum = INF
    x = 0
    y = 0
    for i in range(input_length):
        if selected[i]:
            for j in range(input_length):
                if (not selected[j]) and input_list[i][j]:
                    if minimum > input_list[i][j]:
                        minimum = input_list[i][j]
                        x = i
                        y = j
    compare[x].append(input_list[x][y])
    compare[y].append(input_list[x][y])
    selected[y] = True
    no_edge += 1
counter = 1
ans = []
for n in range(input_length):
    ans.append([])
    for m in range(input_length):
        for i in range(len(compare[n])):
            if n == m:
                ans[n].append("0")
                break
            if input_list[n][m] == compare[n][i]:
                ans[n].append(str(compare[n][i]))
                break
            if i == len(compare[n]) - 1:
                ans[n].append("∞")
                break
f.close()
print(ans)
f1 = open("output.txt", "w", encoding="utf-8")
for each in ans:
    f1.write(" ".join(each))
    f1.write("\n")
f1.close()