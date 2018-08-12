import pulp
import pandas as pd
import numpy as np




cost1_df = pd.DataFrame.from_csv('./maps/1/cost1.csv',header=None,index_col=None)
cost2_df = pd.DataFrame.from_csv('./maps/1/cost2.csv',header=None,index_col=None)

cost1_arr = cost1_df.as_matrix(columns=None)
cost2_arr = cost2_df.as_matrix(columns=None)

node_no = len(cost1_arr)
node_index = list(range(0, node_no))
print (node_index)
test= [1]


x1 = pulp.LpVariable.dicts("Xij",[(i,j) for i in node_index for j in node_index], 0, 1, pulp.LpBinary)
x2 = pulp.LpVariable.dicts("X'ij",[(i,j) for i in node_index for j in node_index], 0, 1, pulp.LpBinary)

f = pulp.LpVariable.dicts("Flow(i,j)",[(i,j) for i in node_index for j in node_index], 0, node_no - 1)
# u = pulp.LpVariable.dicts("Ui",node_index,-node_no, node_no, pulp.LpInteger)

prob = pulp.LpProblem( "Extended TSP", pulp.LpMinimize )
prob += pulp.lpSum(cost1_arr[(i,j)]*x1[(i,j)]+cost2_arr[(i,j)]*x2[(i,j)] for i in node_index for j in node_index)
for i in node_index:
    prob += pulp.lpSum(x1[(i,j)] + x2[(i,j)] - x1[(j,i)] - x2[(j,i)] for j in node_index) == 0

for j in node_index:
    prob += pulp.lpSum(x1[(i,j)]+x2[(i,j)] for i in node_index ) >= 1
    #TODO: maybe this costraint is not necessary, I am not sure

for i in node_index:
    prob += x1[(i,i)] == 0
    prob += x2[(i,i)] == 0
    prob += f[(i, i)] == 0
for i in range (0, node_no):
    for j in range (0, node_no):
        if not i==j:
            prob += x2[(i, j)] <= x1[(j, i)]
            prob += x1[(i, j)] + x2[(i, j)] <= 1
            prob += f[(i, j)] <= (x1[(i, j)] + x2[(i, j)]) * (node_no - 1)
            #only when cost2 is bigger than cost1:
            prob += x1[(i,j)]+x1[(j,i)]<=1


for i in range (1, node_no):
    prob += pulp.lpSum(f[(j,i)]-f[(i,j)] for j in node_index) == 1


prob.solve()

print (pulp.LpStatus[prob.status])
for i in node_index:
    for j in node_index:
        print (str(x1[(i,j)].varValue)+",", end='')
    print ()

print ()
for i in node_index:
    for j in node_index:
        print (str(x2[(i,j)].varValue)+",", end='')
    print ()


