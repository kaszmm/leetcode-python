Tiem Complexity OF Djikstra's Algo is:
First, acknowledge that PQ can grow to size E, since we're just dumping all the neighbors into the PQ. Hence, PQ poll() and add() takes O(log E).
The while loop will execute V times, so ALREADY you have big O[ V( ) ].
INSIDE the while loop: you have to poll from the PQ which takes O(log E), THEN, for EACH neighboring node of the polled node (which there can be O(V) of, imagine each node is connect to every other node), you need to add to the PQ in log E, which takes total O(V log E)
​
So the final runtime is: O[V^2 log E]
​
Hence, we have O(V log E + E log E) = O(E log E).
Fact:  E = O(V^2). That is to say, the number of edges in the worst case = V^2.
O(E log V^2) = O(E * 2 log V) = O(E log V)