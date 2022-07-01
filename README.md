# 数独を数理最適化で解く
数独を数理最適化ソルバーgurobipyを用いて解くプログラムを作成した。

## 実行環境
windows 10 64bit

Anaconda 4.13.0

gurobipy 9.5.1

## プログラムの使い方
変数sが数独の問題設定です。.(ドット)は空欄を示す。
.(ドット)や数字を自由に書き換えて実行することで、その問題の解をnumpy.ndarrayで出力する。

変数s(問題設定)

![スクリーンショット (20)](https://user-images.githubusercontent.com/108399244/176651104-b50c96be-b961-4279-aec9-89d8e27dbca4.png)

出力(問題の解)

![スクリーンショット (21)](https://user-images.githubusercontent.com/108399244/176651580-d5258da3-4cb2-463b-8f73-86123d3a77dd.png)

# 最適化の数理モデル
0-1バイナリ変数を要素とした9×9×9の三次元配列$X$を用意する。${(i, j, k)}$成分の値${X(i, j, k)}$が1の時、数独の$i$行$j$列の数字が$k$であることを意味する。

### 制約条件
#### 制約(1)
一つのマスに入る数字は一つであることを示す制約を入れる。

制約の数は9×9の81個。

$$&\sum_{k=1}^9 X(i, j, k)=1,\quad i=1, 2,...9.\quad j=1, 2,...,9.$$

#### 制約(2)
行方向に同じ数字は入らないことを示す制約を入れる。

制約の数は81個。
$$&\sum_{j=1}^9 X(i, j, k)=1,\quad i=1, 2,...9.\quad k=1, 2,...,9.$$

#### 制約(3)
列方向に同じ数字は入らないことを示す制約を入れる。

制約の数は81個。
$$\sum_{i=1}^9 X(i, j, k)=1,\quad j=1, 2,...9.\quad k=1, 2,...,9.$$

#### 制約(4)
3×3のマスの中に同じ数字は入らないことを示す制約を入れる。

これも制約の数は81個となる。
$$\sum_{p=1}^3 \sum_{q=1}^3 X(3i+p,\ 3j+q,\ k)=1,\quad i=0, 1, 2.\quad j=0, 1, 2.\quad k=1, 2, 3,...,9.$$

### 目的関数
これらの制約を満たせば解が出るので、特に設定しない。

プログラムでは適当に0を入れた。
