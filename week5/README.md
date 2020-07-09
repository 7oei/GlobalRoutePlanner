# TSP Challenge
- week5, week7課題
- フォーク元 https://github.com/hayatoito/google-step-tsp-2018
- input_7: https://github.com/hayatoito/google-step-tsp/blob/master/input_7.csv


There are 7 challenges of TSP in the assignment, from N = 5 to N = 2048:

| Challenge   | N (= the number of cities) | Input file  | Output file  |
| ----------- | -------------------------: | ----------- | ------------ |
| Challenge 0 |                          5 | input_0.csv | output_0.csv |
| Challenge 1 |                          8 | input_1.csv | output_1.csv |
| Challenge 2 |                         16 | input_2.csv | output_2.csv |
| Challenge 3 |                         64 | input_3.csv | output_3.csv |
| Challenge 4 |                        128 | input_4.csv | output_4.csv |
| Challenge 5 |                        512 | input_5.csv | output_5.csv |
| Challenge 6 |                       2048 | input_6.csv | output_6.csv |
| Challenge 7 |                       8192 | input_7.csv | output_7.csv |

# How I solved
## 手法と結果をまとめたスライド
授業の課題も兼ねて作ったものです。かなり詳しく書きました。(一部未完成です 2020/07/09)
https://docs.google.com/presentation/d/1WU_MTpd8DmrmyF_k1jalVDzuBTzJ2xv3wYHle3jI900/edit?usp=sharing
## 初期経路
<img src="https://user-images.githubusercontent.com/52689687/87051433-85fc0800-c23a-11ea-9e48-de1d09a9345d.png" width="800">

## improvement
<img src="https://user-images.githubusercontent.com/52689687/87052703-0a9b5600-c23c-11ea-8521-828caab4c31f.png" width="800">

## 試したもの
- greedy nearest node
- [Krustal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- change start node
- 2-opt
- or-1-opt, or-2-opt
- minus mean
<br>
- Krustal's algorithm
    ... 「閉路ができないように重みが小さい順番から辺を選び、追加していく」 スライドP21
      
- ***2-opt***: -> ```2-opt.py```

        
        - A   B -             - A - B -
            ×         ==>
        - C   D -             - C - D -
        

- ***or-1-opt***: -> ```or-1-opt.py```

        
        - A       C -             - A   -   C -
            \   /     
              B           ==>           B
                                      /   \
        - D   -   E -             - D       E -
         

- ***or-2-opt***: -> ```or-2-opt.py```

        
        - A           D -             - A     -     D -
            \       /                     
              B - C           ==>           B - C
                                          /       \
        - D     -     E -             - D           E -
         
        
- ***minus-mean***:-> ```distance.py```
        各辺(距離)への重みづけ。 <br>
        It takes into account the distribution of the cost of edges leaving a node. If the distance average of both end nodes is large, we need to choose the edges with priority for preventing from getting local opitimal solution.

- ***minus-k-means***: -> ```distance.py``` <br>
        As we improve the solution, we only need to consider the average of the k edges, in decreasing order, since no edges grow between nodes at too great a distance. <br>
      

# Result

***Best Score***

|                                        | N = 5   | N = 8   | N = 16  | N = 64   | N = 128  | N = 512  | N = 2048 | 
| ----                                   | ----    | ----    | ----    | ----     | ----     | ----     | ----     | 
| kruskal + start node 30通り             | 3291.62 | 3778.72 | 4494.42 | 8118.40  | 10539.04 | 20263.87 | 40537.49 |

<img src="https://user-images.githubusercontent.com/52689687/87052043-513c8080-c23b-11ea-9766-377bd2da5749.png" width="400">

### 初期経路greedyのとき
|                                        | N = 5   | N = 8   | N = 16  | N = 64   | N = 128  | N = 512  | N = 2048 | 
| ----                                   | ----    | ----    | ----    | ----     | ----     | ----     | ----     | 
| greedy                                 | 3418.10 | 3832.29 | 5449.44 | 10519.16 | 12684.06 | 25331.84 | 49892.05 | 
| greedy + 2-opt                         | 3418.10 | 3832.29 | 4994.89 | 8970.05  | 11489.79 | 21363.60 | 42712.37 | 
| greedy + 2-opt + or-1-opt              | 3291.62 | 3778.72 | 4494.42 | 8656.07  | 11225.87 | 20902.75 | 41638.84 | 
| greedy + 2-opt + or-1-opt + or-2-opt   | 3291.62 | 3778.72 | 4494.42 | 8656.07  | 11225.87 | 20902.75 | 41638.84 | 
<img src="https://user-images.githubusercontent.com/52689687/87051991-4124a100-c23b-11ea-93ea-7d6413380079.png" width="400">

### improveは2-opt + or-1-opt + or-2-optで固定し、初期経路を変えたとき
|                                        | N = 5   | N = 8   | N = 16  | N = 64   | N = 128  | N = 512  | N = 2048 | 
| ----                                   | ----    | ----    | ----    | ----     | ----     | ----     | ----     | 
| greedy                                 | 3291.62 | 3778.72 | 4494.42 | 8656.07  | 11225.87 | 20902.75 | 41638.84 | 
| minus_mean                             | 3291.62 | 3778.72 | 4494.42 | 8388.24  | 11047.07 | 21178.11 | 42104.09 |
| minus_10_mean                          | 3291.62 | 3778.72 | 4494.42 | 8497.71  | 11338.02 | 21219.00 | 41247.10 |
| kruskal                                | 3291.62 | 3778.72 | 4494.42 | 8451.45  | 10925.97 | 20894.69 | 41110.98 |
| kruskal + start node 30通り             | 3291.62 | 3778.72 | 4494.42 | 8118.40  | 10539.04 | 20263.87 | 40537.49 |
<img src="https://user-images.githubusercontent.com/52689687/87052013-484baf00-c23b-11ea-8781-cd9f1b08f75c.png" width="400">

