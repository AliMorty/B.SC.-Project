# B.CS.-Project
Implementation and Evaluation of "Genetic" and "Simulated Annealing" algorithms for Extended version of Travelling Salesman Problem.
In this project, we tested the performance of two different heuristic approaches in solving an NP-Complete Problem. This problem is an extended version of Travelling Salesman Problem. Since our approach is heuristic,there is not guaranty to find a global optimum answer. So we needed some other exact approach for computing the global optimum. For this purpose, we reduced our problem to an Integer Linear Programming Instance. So in small graph samples, we could compare our results with optimum solution and for the large graph samples, we just compared our two different methods with each other. 

## Extended Travelling Salesman Problem
This problem is similar to Graphical TSP. (eg. Traveller can enter any node and edge more than one time) and every edge has two different costs. **First-Time-Cost** and **Second-Time-Cost**. When we use an edge for the first time, it has a cost, probably higher and for the second time and more, it has lower cost. This problem can have some application like Airport Scheduling. Because in Airport, Round-trip ticket are cheaper than two one-way-tickets. <br>
In fact lots of real world problems are NP-Complete. (Specially varitaions of the TSP Problem) <br>
In this project, we wanted to compare two different approaches ("Genetic" and "Simulated Annealing") for solving an NP-Complete Problem. <br>
![A Sample Grapg](./a-simple-graph.bmp)
 
 
