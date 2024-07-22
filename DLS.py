def Dls(graph,StartNode,GoalNode,DepthLimit,visited):
    if DepthLimit>=0:
        if StartNode==GoalNode:
            print(StartNode)
            return True
        if StartNode not in visited:
            print(StartNode,end=" ")
            visited.add(StartNode)
            for i in graph[StartNode]:
                if Dls(graph,i,GoalNode,DepthLimit-1,visited):
                    return True
    return False

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
visited=set()
print("DLS traversal is : ",end="")
if not Dls(graph,StartNode,GoalNode,DepthLimit,visited):
     print(f"\nGoal node {GoalNode} not found within depth limit.")