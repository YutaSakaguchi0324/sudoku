# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:10:18 2022

@author: public
"""
import gurobipy as gp
import numpy as np
import re

#数独
#マス目の大きさ
n = 3
N = n**2

s = ('. . 5 |3 . . |. . . '
     '8 . . |. . . |. 2 . '
     '. 7 . |. 1 . |5 . . '
     '------+------+------'
     '4 . . |. . 5 |3 . . '
     '. 1 . |. 7 . |. . 6 '
     '. . 3 |2 . . |. 8 . '
     '------+------+------'
     '. 6 . |5 . . |. . 9 '
     '. . 4 |. . . |. 3 . '
     '. . . |. . 9 |7 . . ')

data = re.sub(r'[^\d.]','',s) # 数字とドット以外を削除

# 問題を設定
sudoku = gp.Model(name = "Sudoku")

#　変数を格納する三次元配列を生成する
X = [[[0]*N for i in range(N)] for j in range(N)]

# 変数を設定（変数単体にかかる制約を含む）
for i in range(N):
    for j in range(N):
        if data[N*i+j] == ".":
            for k in range(N):
                X[i][j][k] = sudoku.addVar(vtype = gp.GRB.BINARY, name = "x" + str(i) + str(j) + str(k))
        else:
            for k in range(N):
                if k+1 == int(data[N*i+j]):
                    X[i][j][k] = 1
                else:
                    X[i][j][k] = 0
            
# 目的関数を設定
sudoku.setObjective(0, sense = gp.GRB.MINIMIZE)

# 制約を設定
# 一つのマスに入る数字は一つだけ
for i in range(N):
    for j in range(N):
        sum_list = [X[i][j][k] for k in range(N)]
        sudoku.addConstr(sum(sum_list) == 1, name = "number" + str(i) + str(j) + str(k))
        
# 同じ行に入る数字は一つだけ
for i in range(N):
    for k in range(N):
        sum_list = [X[i][j][k] for j in range(N)]
        sudoku.addConstr(sum(sum_list) == 1, name = "horizontal" + str(i) + str(j) + str(k))

# 同じ列に入る数字は一つだけ
for j in range(N):
    for k in range(N):
        sum_list = [X[i][j][k] for i in range(N)]
        sudoku.addConstr(sum(sum_list) == 1, name = "vertical" + str(i) + str(j) + str(k))
        
# 3×3のマスに入る数字は一つだけ
for i in range(n):
    for j in range(n):
            for k in range(N):
                sum_list = [X[n*i+p][n*j+q][k] for p in range(n) for q in range(n)]
                sudoku.addConstr(sum(sum_list) == 1, name = "square" + str(i) + str(j) + str(k))
        
# 解を求める計算
sudoku.optimize()

# 最適解が得られた場合、結果を出力
if sudoku.Status == gp.GRB.OPTIMAL:
    # 解の値をndarrayに変換する
    solution = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                opt = X[i][j][k]
                if type(opt) == int:
                    if opt == 1:
                        solution[i, j] = k+1
                else:
                    if opt.X == 1:
                        solution[i, j] = k+1
                    
    print(solution)