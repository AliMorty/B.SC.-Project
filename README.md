# B.CS.-Project
Implementation and Evaluation of "**Genetic**" and "**Simulated Annealing**" algorithms for Extended version of Travelling Salesman Problem. <br>
In this project, we tested the performance of two different heuristic approaches to solving an NP-Complete Problem. This problem is an extended version of the Travelling Salesman Problem. Since our approach is heuristic, there is not guaranty to find a global optimum answer. So we needed some other exact approach for computing the global optimum. For this purpose, we reduced our problem to an Integer Linear Programming Instance. So in small graph samples, we could compare our results with the optimum solution and for the large graph samples, we just compared our two different methods with each other. <br>

## Extended Travelling Salesman Problem
This problem is similar to Graphical TSP. (eg. A traveler can enter any node and edge more than one time) and every edge has two different costs. **First-Time-Cost** and **Second-Time-Cost**. When we use an edge for the first time, it has a cost, probably higher and for the second time and more, it has a lower cost. This problem can have some application like Airport Scheduling. Because in Airport, Round-trip ticket is cheaper than two one-way tickets. <br>
In fact, lots of real-world problems are NP-Complete. (Especially variations of the TSP Problem) <br>
In this project, we wanted to compare two different approaches ("Genetic" and "Simulated Annealing") for solving an NP-Complete Problem. <br>
![A Sample Grapg](/Images/a-simple-graph.bmp)
 
 ## Our Approach
 We used two different approaches.
 > Genetic Algorithm <br>
 > Simulated Annealing <br>

 ## Reduce To Integer Linear Programming
 Since our approaches do not guaranty to achieve the optimum result, we reduced our problem to Integer Linear Programming.  So in small graph samples, we could compare our results with the optimum solution and for the large graph samples, we just compared our two different methods with each other.
 <br>
 ### Normal Formulation
 #### Minimize <br>
 *c* and *c'* correspond to first and second costs. <br>
 if we use an edge for the first time then *x*=1 and if we use the edge for the second time then *x'*=1 (It can be easily proved that in the optimum solution we will use every edge at most two times. not more!) <br> 
![function](/Images/formula-1.bmp) 
 #### Problem constraints <br>
![Constraint](/Images/constraint.bmp)

### Problem: number of constraints is in an exponential order! 
The reason we used the last constraint is that we want the graph to be connected. Not like this:<br>
![Sample](/Images/lip-probelm.bmp) <br>
Since **all non-empty partitions** are in order of **all subset of all nodes** and therefore Exponential, normal constraints was not a good choice. So we used something like a flow in order. Suppose we want to inject water to every node from **node-1**, if the graph is not connected, there will be no way for doing so. So we used some other variables *f<sub>ij</sub>* and using them to guaranty that we can inject water into every node from **node-1**. <br>
So we removed the last constraint. Then add new constraints as below:<br>
![New Constraint](/Images/new-condition.bmp)

### Running The Program
![image](/Images/an-output.bmp) <br>
We tested different hyper parameters for our algorithms. 
### Genetic Algorithm
![image](/Images/genetic-pop-cost.bmp) <br>
### Simulated Annealing
![image](/Images/simulated-annealing-iteration-costt.bmp) <br>

