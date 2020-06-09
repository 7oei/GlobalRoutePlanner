# ある人からある人に最短でたどり着く場合に経由する人の数を返すプログラム
# 同ディレクトリ下にlinks.txtとnicknamesを置いた上で実行し
# 初めの人の名前、探したい人の名前を入力

from collections import deque
import time

list = [[] for i in range (10**7)] # 格人がフォローをしている人を格納
visited = [10**7 for i in range (10**7)] # 最短の探索経路長を格納(十分大きな値で初期化)
dict = {}
# 次に探索すべき人を格納するqueue
d = deque()


# nicknames.txtから名前と番号の辞書を作成
def makedict(dict):
    with open('wikipedia_links/pages.txt') as f:
        for s_line in f:
            line = s_line.split()
            dict[line[1]] = int(line[0])


# links.txtから各人がフォローしている人のリストを作成
def makefollowlist(list):
    with open ("wikipedia_links/links.txt") as f:
        for s_line in f:
            line = s_line.split()
            print(line[0], line[1])
            follow, follower = int(line[0]), int(line[1])
            list[follow].append(follower)


# 初期化
def initialize(d, visited, st, fi):
    start = (dict[st]) # スタートの人
    find = (dict[fi]) # 見つけたい人
    d.append(start)
    visited[start] = 0
    ans = 10**7
    return start, find, ans


# BFT
def search(start, find, d, list, visited, ans):
    # 自分探しした場合
    if start==find:
        print("me!")
        exit()

    t1 = time.time()
    # queueを使って幅優先探索
    # queueに要素がある間左からpopし、その人のfollow先の人を探索
    while (d):
        poped = d.popleft()
        for i in list[poped]:

            # 見つかった場合、最小経路だったらansを更新
            if i == find and ans > visited[poped]+1:
                ans = visited[poped]+1
                t2 = time.time()

            # 前回の探索より短い探索経路を見つけたら更新、探索すべきqueueに格納
            if visited[i] > visited[poped]+1:
                visited[i] = visited[poped]+1
                d.append(i)

    # ansが初期化のままだったら"not found", そうでなかったらansが答え
    print("found via", ans, "people\ntime = ",(t2-t1)*10**3,"[10^(-3)s]") if ans!=10**7 else print("Not found\n")



######## 入力 ########
print("Enter the name you want to strat with >>>")
st = input() # 初めの人の名前
print("Enter the name you want to find >>>")
fi = input() # 探したい人の名前


####### 実行 #########
makedict(dict)
makefollowlist(list)
start, find, ans = initialize(d, visited, st, fi)
search(start, find, d, list, visited, ans)
