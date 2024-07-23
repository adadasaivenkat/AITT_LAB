def astar(graph,h,StartNode,GoalNode):
    openSet=set([StartNode])
    closedSet=set()
    g={}
    parents={}
    g[StartNode]=0
    parents[StartNode]=StartNode
    while len(openSet)>0:
        n=None
        for i in openSet:
            if n is None or g[i]+h[i]<g[n]+h[n]:
                n=i
        if n==GoalNode:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(StartNode)
            path.reverse()
            return path
        openSet.remove(n)
        closedSet.add(n)
        for i,j in graph[n].items():
            if i not in openSet and i not in closedSet:
                openSet.add(i)
                parents[i]=n
                g[i]=g[n]+j
            else:
                if g[i]>g[n]+j:
                    g[i]=g[n]+j
                    parents[i]=n
                    if i in closedSet:
                        closedSet.remove(i)
                        openSet.add(i)
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
result=astar(graph,h,StartNode,GoalNode)
if result:
    print(f"Path : {result}")
else:
    print("No path found.")