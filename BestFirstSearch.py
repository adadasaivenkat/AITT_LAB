import heapq
def best(graph,h,StartNode,GoalNode):
    openSet=[]
    heapq.heappush(openSet,(h[StartNode],StartNode))
    closedSet=set()
    parents={}
    parents[StartNode]=StartNode
    while len(openSet)>0:
        priority,n=heapq.heappop(openSet)
        if n==GoalNode:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(StartNode)
            path.reverse()
            return path
        closedSet.add(n)
        for i in graph[n]:
            if i in closedSet:
                continue
            heapq.heappush(openSet,(h[i],i))
            parents[i]=n
    return None
V=int(input("Enter the number of nodes/vertices : "))
E=int(input("Enter the number of edges : "))
graph={}
for i in range(1,E+1):
    src,des,wt=input(f"Enter edge {i} (source, destination, weight) : ").split()
    if src not in graph:
        graph[src]={}
    if des not in graph:
        graph[des]={}
    graph[src][des]=int(wt)
    #graph[des][src]=int(wt)  # For undirected graph
h={}
for i in range(1,V+1):
    node,hval=input(f"Enter heuristic value for node {i} (node, heuristic) : ").split()
    h[node]=int(hval)
StartNode=input("Enter the starting node : ")
GoalNode=input("Enter the goal node : ")
result=best(graph,h,StartNode,GoalNode)
if result:
    print(f"Path : {result}")
else:
    print("No path found.")