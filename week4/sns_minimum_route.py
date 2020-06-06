# ある人からある人に最短でたどり着く場合に経由する人の数を返すプログラム
# 同ディレクトリ下にlinks.txtとnicknamesを置いた上で
# 17行目に初めの人の名前を入力、18行目に探したい人の名前を入力し実行

from collections import deque

list = [[] for i in range (54)] # 格人がフォローをしている人を格納
visited = [10**5 for i in range (54)] # 最短の探索経路長を格納(十分大きな値で初期化)
dict = {}

# nicknames.txtから名前と番号の辞書を作成
with open('nicknames.txt') as f:
    for s_line in f:
        line = s_line.split()
        dict[line[1]] = int(line[0])

start = (dict['alan']) # スタートの人
find = (dict['emma']) # 見つけたい人


# links.txtから各人がフォローしている人のリストを作成
with open ("links.txt") as f:
    for s_line in f:
        line = s_line.split()
        follow, follower = int(line[0]), int(line[1])
        list[follow].append(follower)

# 次に探索すべき人を格納するqueue
d = deque()

# 初期化
d.append(start)
visited[start] = 0
ans = 10**3

# 自分探しした場合
if start==find:
    print("me!")
    exit()

# queueを使って幅優先探索
# queueに要素がある間左からpopし、その人のfollow先の人を探索
while (d):
    poped = d.popleft()
    for i in list[poped]:

        # 見つかった場合、最小経路だったらansを更新
        if i == find:
            ans = min(ans, visited[poped]+1)

        # 前回の探索より短い探索経路を見つけたら更新、探索すべきqueueに格納
        if visited[i] > visited[poped]+1:
            visited[i] = visited[poped]+1
            d.append(i)

# ansが初期化のままだったら"not found", そうでなかったらansが答え
print("fornd via", ans, "people") if ans!=10**3 else print("Not found\n")
