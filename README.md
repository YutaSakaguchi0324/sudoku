# プログラム概要
gurobipyを用いて数独を解くプログラムをつくる

# 実行環境
windows 10 64bit

Anaconda 4.13.0

gurobipy 9.5.1

# プログラムの使い方
変数sが数独の問題設定です。.(ドット)は空欄を示しています。
.(ドット)や数字を自由に書き換えて実行することで、その問題の解をnumpy.ndarrayで出力します。

変数s(問題設定)

![スクリーンショット (20)](https://user-images.githubusercontent.com/108399244/176651104-b50c96be-b961-4279-aec9-89d8e27dbca4.png)

出力(問題の解)

![スクリーンショット (21)](https://user-images.githubusercontent.com/108399244/176651580-d5258da3-4cb2-463b-8f73-86123d3a77dd.png)

# 最適化の数理モデル
0-1バイナリ変数を要素とした9×9×9の三次元配列$X$を用意します。${(i, j, k)}$成分の値${X(i, j, k)}$が1の時、数独の$i$行$j$列の数字が$k$であることを意味することにします。

# 制約条件

$$\sum_{k=1}^9 X(i, j, k)=1,\ i=1, 2,...9,\ j=1, 2,...,9$$
