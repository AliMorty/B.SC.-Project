from unionfind import unionfind
import queue
import pandas as pd
global cost1_arr
global infinite
infinite = 99999999.99

class MinSpanTreeClass:
    def __init__(self):
        self.child_list=None
        self.output_path = []
    def do_all(self, arr):
        self.MinimumSpanningTree(arr)
        self.make_path()
        var = self.output_path
        var = var[:-1]
        return var
    def MinimumSpanningTree(self, arr):
        q = queue.PriorityQueue()
        n = len(arr)
        inMST = [False] * n
        inMST[0]= True
        parent = [0] * n
        current_cost = [infinite] * n
        node_in_tree = 1
        for i in range (1, n):
            q.put((arr[(0,i)], i))
            current_cost[i] = arr[(0,i)]
        while (not q.empty() and node_in_tree < n):
            # print ("ismst: ", end='')
            # print (inMST)
            u= q.get()

            weight = u[0]
            v = u[1]
            if not inMST[v]:
                node_in_tree += 1
                inMST[v] = True
            for i in range (0, n):
                new_cost = arr[(v,i)]
                if not inMST[i] and new_cost < current_cost[i]:
                    parent[i]=v
                    current_cost[i] = new_cost
                    q.put((new_cost, i))



        childs_list = [list() for _ in range(n)]
        for i in range(1, n):
            # print ("edge: "+ str(i)+ ", "+ str (parent[i]))
            j = parent[i]
            childs_list[j].append(i)
        self.child_list = childs_list
        return childs_list


    def make_path (self):
        self.output_path = []
        self.DFS_on_tree(0)
        

    def DFS_on_tree (self, node_start):
        if self.child_list== None:
            print("child list in not made, error")
        self.output_path.append(node_start)
        for i in self.child_list[node_start]:
            self.DFS_on_tree(i)
            self.output_path.append(node_start)




    def read_from_file(self):
        cost1_df = pd.DataFrame.from_csv('./maps/1/cost1.csv', header=None, index_col=None)
        cost2_df = pd.DataFrame.from_csv('./maps/1/cost2.csv', header=None, index_col=None)
        global cost1_arr
        global cost2_arr
        cost1_arr = cost1_df.as_matrix(columns=None)
        cost2_arr = cost2_df.as_matrix(columns=None)

        self.cost1_arr = cost1_arr
        self.cost2_arr = cost2_arr

        global node_no
        node_no = len(cost1_arr)




G = {0:{1:11,2:13,3:12},1:{0:11,3:14},2:{0:13,3:10},3:{0:12,1:14,2:10}}
T = [(2,3),(0,1),(0,3)]
m = MinSpanTreeClass()
m.read_from_file()





m.MinimumSpanningTree(cost1_arr)
print (m.child_list)
m.make_path()
print (m.output_path[:-1])

