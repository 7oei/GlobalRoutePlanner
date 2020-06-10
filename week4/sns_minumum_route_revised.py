# ある人からある人に最短でたどり着く場合に経由する人の数を返すプログラム
# 同ディレクトリ下にlinks.txtとnicknamesを置いた上で実行
# 初めの人の名前、探したい人の名前を入力

from collections import deque
import time

# nicknames.txtから名前と番号の辞書を作成
def makedict():
    nickname_dict = {}
    with open('nicknames.txt') as f:
        for s_line in f:
            line = s_line.split()
            nickname_dict[line[1]] = int(line[0])
    return nickname_dict


# links.txtから各人がフォローしている人の辞書を作成
def load_follows():
    follows = {}
    with open ("links.txt") as f:
        for s_line in f:
            line = s_line.split()
            follow_from, follow_to = int(line[0]), int(line[1])
            if follow_from not in follows:
                follows[follow_from] = []
            follows[follow_from].append(follow_to)
    return follows


# BFT
def search(st, fi, nickname_dict, follows):
    start = (nickname_dict[st]) # スタートの人
    find = (nickname_dict[fi]) # 見つけたい人

    # 次に探索すべき人を格納するqueue: (node, depth)
    d = deque()
    d.append((start,0))
    ans = 10**3

    # 自分探しした場合
    if start == find:
        print("me!")
        exit()

    t1 = time.time()
    # queueを使って幅優先探索
    # queueに要素がある間左からpopし、その人のfollow先の人を探索
    while (d):
        cur_node, cur_depth = d.popleft()
        for to_node in follows[cur_node]:

            # 見つかった場合
            if to_node == find:
                t2 = time.time()
                print('found via', cur_depth + 1, "people\ntime = ",(t2-t1)*10**3,"[10^(-3)s]")
                return

            # 初めて探索した場合
            if to_node not in d:
                d.append((to_node,cur_depth + 1))

    # 見つからなかった
    print("Not found\n")
    return



######## 入力 ########
print("Enter the name you want to strat with >>>")
st = input() # 初めの人の名前
print("Enter the name you want to find >>>")
fi = input() # 探したい人の名前


####### 実行 #########
nickname_dict = makedict()
follows = load_follows()
search(st, fi, nickname_dict, follows)
