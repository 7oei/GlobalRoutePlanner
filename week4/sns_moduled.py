# ある人からある人にたどり着けるか判定するプログラム
# 同ディレクトリ下にlinks.txtとnicknamesを置いた上で

from collections import deque

list = [[] for i in range (54)] # 格人がフォローをしている人を格納
visited = [0 for i in range (54)] # その人を探索していない場合0, した場合1
dict = {}
# 次に探索すべき人を格納するqueue
d = deque()




# nicknames.txtから名前と番号の辞書を作成
def makenamedict(dict):
    with open('nicknames.txt') as f:
        for s_line in f:
            line = s_line.split()
            dict[line[1]] = int(line[0])


# links.txtから各人がフォローしている人のリストを作成
def makefollowlist(list):
    with open ("links.txt") as f:
        for s_line in f:
            line = s_line.split()
            parent, child = int(line[0]), int(line[1])
            list[parent].append(child)


# queueを使って幅優先探索
# queueに要素がある間左からpopし、その人のfollow先の人を探索
def BFT(d, start, find):
    # 最初はstartから探索
    d.append(start)

    while (d):
        for i in list[d.popleft()]:
            # 見つかった場合
            if i == find:
                return ("found")

            # 初めて訪れた場合だけ探索すべきqueueに格納
            if visited[i]==0:
                visited[i] = 1
                d.append(i)
    return ("Not found")


def initialize(st, fi):
    start = (dict[st]) # スタートの人
    find = (dict[fi]) # 見つけたい人
    return start, find


####### 入力 ########
print("Enter the name you want to strat with >>>")
st = input() # 初めの人の名前
print("Enter the name you want to find >>>")
fi = input() # 探したい人の名前


####### 実行 ########
makenamedict(dict)
makefollowlist(list)
start, find = initialize(st, fi)
print(BFT(d, start, find))
