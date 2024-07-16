def Dls(graph,StartNode,GoalNode,DepthLimit,visited):
    if visited is None:
        visited=set()
    if StartNode==GoalNode:
        return [StartNode]
    visited.add(StartNode)
    if DepthLimit<=0:
        return None
    for i in graph[StartNode]:
        if i not in visited:
            path=Dls(graph,i,GoalNode,DepthLimit-1,visited)
            if path is not None:
                return [StartNode]+path
    return None             #If no path is found after exploring all neighbors


V=int(input("Enter the number of nodes/vertices : "))
E=int(input("Enter the number of edges : "))
graph={}
for i in range(1,E+1):
    src,des=input(f"Enter edge {i} (source, destination) : ").split()
    if src not in graph:
        graph[src]={}
    if des not in graph:
        graph[des]={}
    graph[src][des]=1
    #graph[des][src]=1    # For undirected graph
StartNode=input("Enter the starting node : ")
GoalNode=input("Enter the goal node : ")
DepthLimit=int(input("Enter the depth limit : "))
visited=None
result=Dls(graph,StartNode,GoalNode,DepthLimit,visited)
if result is not None:
    print("DLS traversal is :",result)
else:
    print("Path not found within depth limit.")