# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:10:18 2022

@author: public
"""
import gurobipy as gp
import numpy as np

#　潜水艦ゲーム
#　盤面の大きさ N行M列
N, M = 3, 4

#　潜水艦のサイズ　n行m列
n, m = 1, 1
# 問題を設定
submarine_problem = gp.Model(name = "GurobiSample1")

#　変数を格納する二次元配列を生成する
X = [[0]*M for i in range(N)]

# 変数を設定（変数単体にかかる制約を含む）
for i in range(N):
    for j in range(M):
        
        X[i][j] = submarine_problem.addVar(vtype = gp.GRB.BINARY, name = "x" + str(i) + str(j))
        
def flatten(nested_list):
    """二重のリストをフラットにする関数"""
    return [e for inner_list in nested_list for e in inner_list]

summation = sum(flatten(X))

# 目的関数を設定
submarine_problem.setObjective(summation, sense = gp.GRB.MINIMIZE)

# 制約を設定
for i in range(N - (n - 1)):
    for j in range(M - (m - 1)):
        # 横の制約
        rectangle_list = [X[i+n1][j+m1] for n1 in range(n) for m1 in range(m)]
        rectangle_summation = sum(rectangle_list)
        submarine_problem.addConstr(rectangle_summation >= 1, name = "horizontal_2" + str(i) + str(j))
        
for i in range(N - (m - 1)):
    for j in range(M - (n - 1)):
        rectangle_list = [X[i+m1][j+n1] for m1 in range(m) for n1 in range(n)]
        rectangle_summation = sum(rectangle_list)
        submarine_problem.addConstr(rectangle_summation >= 1, name = "vertical_2" + str(i) + str(j))
        
# 解を求める計算
submarine_problem.optimize()

# 最適解が得られた場合、結果を出力
if submarine_problem.Status == gp.GRB.OPTIMAL:
    # 解の値をndarrayに変換する
    square = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            opt = X[i][j]
            square[i, j] = opt.X + 0
    # 目的関数の値
    val_opt = submarine_problem.ObjVal
    print(square)