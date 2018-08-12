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


x = pulp.LpVariable.dicts("Xij",[(i,j) for i in node_index for j in node_index], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("Ui",node_index,-node_no, node_no, pulp.LpInteger)
prob = pulp.LpProblem( "TSP", pulp.LpMinimize )
prob += pulp.lpSum(cost1_arr[(i,j)]*x[(i,j)] for i in node_index for j in node_index)
for i in node_index:
    prob += pulp.lpSum(x[(i,j)] for j in node_index ) == 1
for j in node_index:
    prob += pulp.lpSum(x[(i,j)] for i in node_index ) == 1
for i in node_index:
    prob += x[(i,i)] == 0
for i in range (1, node_no):
    for j in range (1, node_no):
        if not i ==j:
            prob += (u[i]-u[j]+ node_no*x[(i,j)] <= node_no -1 )

prob.solve()
print (pulp.LpStatus[prob.status])

for i in node_index:
    for j in node_index:
        print (str(x[(i, j)].varValue)+",", end='')
    print ()
for i in node_index:
    print(str(u[i].varValue))



# REQUIRE = {
#     1:7,
#     2:5,
#     3:3,
#     4:2,
#     5:2
# }
# LOCATIONS = [1, 2, 3, 4, 5]
# PRODUCTS = [1, 2, 3, 4, 5]
# CAPACITY = 8
# prob  = pulp.LpProblem( "Product Minimize", pulp.LpMinimize )
# use_vars = pulp.LpVariable.dicts("UseLocation", LOCATIONS, 0, 1, pulp.LpBinary)
# waste_vars = pulp.LpVariable.dicts("Waste", LOCATIONS, 0, CAPACITY)
# assign_vars = pulp.LpVariable.dicts("AtLocation",[(i,j) for i in LOCATIONS for j in PRODUCTS], 0, 1, pulp.LpBinary)
# # objective function
# prob += pulp.lpSum(waste_vars[i] for i in LOCATIONS)
# # constraints
# for j in PRODUCTS:
#     prob += pulp.lpSum(assign_vars[(i,j)] for i in LOCATIONS ) == 1
# for i in LOCATIONS:
#     prob += pulp.lpSum(assign_vars[(i,j)]*REQUIRE[j]+waste_vars[i] for j in PRODUCTS) == CAPACITY * use_vars[i]
# prob.solve()
# TOL = 0.00001
# for i in LOCATIONS:
#     for j in PRODUCTS:
#         print (str(assign_vars[(i, j)].varValue)+",", end='')
#     print ()







# production = pulp.LpVariable.dicts("production",
#                                      ((month, factory) for month, factory in factories.index),
#                                      lowBound=0,
#                                      cat='Integer')

# IDENTIFIERS = ['A','B','C','D','E']
# PRICES      = dict( zip( IDENTIFIERS, [100.0, 99.0, 100.5, 101.5, 200.0 ] ) )
# n           = len( IDENTIFIERS )
#
# x     = pulp.LpVariable.dicts( "x", indexs = IDENTIFIERS, lowBound=0, upBound=1, cat='Integer', indexStart=[] )
# prob  = pulp.LpProblem( "Minimalist example", pulp.LpMaximize )
# prob += pulp.lpSum( [ x[i]*PRICES[i] for i in IDENTIFIERS ]  ), " Objective is sum of prices of selected items "
# prob += pulp.lpSum( [ x[i] for i in IDENTIFIERS ] )==2, " Constraint is that we choose two items "
# prob.solve()


