# ある人からある人にたどり着けるか判定するプログラム
# 同ディレクトリ下にlinks.txtとnicknamesを置いた上で
# 17行目に初めの人の名前を入力、18行目に探したい人の名前を入力し実行

from collections import deque

list = [[] for i in range (54)] # 格人がフォローをしている人を格納
visited = [0 for i in range (54)] # その人を探索していない場合0, した場合1
dict = {}

# nicknames.txtから名前と番号の辞書を作成
with open('nicknames.txt') as f:
    for s_line in f:
        line = s_line.split()
        dict[line[1]] = int(line[0])

start = (dict['adrian']) # スタートの人
find = (dict['alan']) # 見つけたい人


# links.txtから各人がフォローしている人のリストを作成
with open ("links.txt") as f:
    for s_line in f:
        line = s_line.split()
        parent, child = int(line[0]), int(line[1])
        list[parent].append(child)

# 次に探索すべき人を格納するqueue
d = deque()
# 最初はstartから探索
d.append(start)

# queueを使って幅優先探索
# queueに要素がある間左からpopし、その人のfollow先の人を探索
while (d):
    for i in list[d.popleft()]:
        # 見つかった場合
        if i == find:
            print("found")
            exit()
        # 初めて訪れた場合だけ探索すべきqueueに格納
        if visited[i]==0:
            visited[i] = 1
            d.append(i)

print("Not found")
